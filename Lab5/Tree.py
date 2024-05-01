import turtle as t
import numpy as np

"""
3. Побудувати словник зі слів текстового файлу у вигляді дерева
двійкового пошуку. Вивести його на екран у вигляді дерева. Здійснити пошук
вказаного слова у дереві і у файлі. Якщо слова немає, додати його при
необхідності в дерево і у відповідний файл. Видалити вказане слово з дерева
та файлу. Порівняти час пошуку в дереві та у файлі.
"""


class Edge:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


class Tree:
    def __init__(self, list_of_chars=[]):
        self.list = list_of_chars
        self.edges = None
        self.rearrange()

    def find_place(self, char, edge=None):
        if edge is None:
            edge = self.edges[0]

        if char <= edge.value:
            if edge.left is None:
                edge.left = Edge(char)
                self.edges += [edge.left]
            else:
                self.find_place(char, edge.left)

        elif char > edge.value:
            if edge.right is None:
                edge.right = Edge(char)
                self.edges += [edge.right]
            else:
                self.find_place(char, edge.right)

    def rearrange(self):
        for word in self.list:
            for char in word:
                if self.edges is None:
                    self.edges = [Edge(char)]
                else:
                    self.find_place(char)

    def draw_edge(self, edge, radius):
        t.pendown()
        t.circle(radius)
        t.write(edge.value.capitalize(), align="center", font=("Arial", 10, "normal"))
        t.penup()

    def draw_bridge(self, from_where, to_where):
        t.penup()
        t.setpos(*from_where)
        t.pendown()
        t.setpos(*to_where)
        t.penup()

    def draw_edges(self, edge=None, x=0, y=0, move=30, to=None):
        radius = 10
        if edge is None:
            edge = self.edges[0]
            t.setpos(x, y)
            self.draw_edge(edge, radius)
        else:
            if to == "left":
                t.setpos(x, y)
                self.draw_edge(edge, radius)
            elif to == "right":
                t.setpos(x, y)
                self.draw_edge(edge, radius)

        print(x, y, "edge:", edge.value)
        if edge.left is not None:
            x_from = x
            y_from = y
            from_where = (x_from, y_from)
            x_to = x-move
            y_to = y-move
            to_where = (x_to+radius*np.sqrt(2), y_to+radius*np.sqrt(2))
            print("Going from", from_where, "to", to_where)
            
            self.draw_bridge(from_where, to_where)
            self.draw_edges(edge.left, x-move, y-move, move, "left")
        if edge.right is not None:
            x_from = x
            y_from = y
            from_where = (x_from, y_from)
            x_to = x+move
            y_to = y-move
            to_where = (x_to-radius*np.sqrt(2), y_to+radius*np.sqrt(2))
            print("Going from", from_where, "to", to_where)
            
            self.draw_bridge(from_where, to_where)
            self.draw_edges(edge.right, x+move, y-move, move, "right")


"""
t.pendown()
for char in word:
    t.forward(10)
    t.write(char, align="center", font=("Arial", 12, "normal"))
t.penup()
"""

t.pen(pensize=3, speed=20)
t.penup()

text = "vklmnoijqrstabcupdefghwxyz"
# text="abcaabs"
tree = Tree(text.split())
tree.draw_edges()

t.hideturtle()
t.done()
