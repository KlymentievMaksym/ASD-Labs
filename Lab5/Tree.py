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
    def __init__(self, text=""):
        
        self.list = text.split()
        self.edges = None
        self._rearrange()

    def _find_place(self, char, edge=None, typ=str):
        if edge is None:
            edge = self.edges[0]

        not_int = False
        
        try:
            char = typ(char)
        except ValueError:
            not_int = True
        
        if char <= [typ(edge.value), edge.value][not_int]:
            if edge.left is None:
                edge.left = Edge(char)
                self.edges += [edge.left]
            else:
                self._find_place(char, edge.left)

        elif char > [typ(edge.value), edge.value][not_int]:
            if edge.right is None:
                edge.right = Edge(char)
                self.edges += [edge.right]
            else:
                self._find_place(char, edge.right)

    def _rearrange(self):
        for word in self.list:
            if len(self.list) != 1:
                typ = int
                try:
                    word = int(word)
                except ValueError:
                    typ = str
                if self.edges is None:
                    self.edges = [Edge(word)]
                else:
                    self._find_place(word, typ=typ)
            else:
                for char in word:
                    if self.edges is None:
                        self.edges = [Edge(char)]
                    else:
                        self._find_place(char)

    def _draw_edge(self, edge, radius):
        t.pendown()
        t.circle(radius)
        t.write(edge.value, align="center", font=("Arial", 10, "normal"))
        t.penup()

    def _draw_bridge(self, from_where, to_where):
        t.penup()
        t.setpos(*from_where)
        t.pendown()
        t.setpos(*to_where)
        t.penup()

    def draw_edges(self, x=0, y=0, move=20, move_y=0, show_print=False, pensize=3, speed=20):
        t.pen(pensize=pensize, speed=speed)
        t.penup()
        self._draw_edges(x=x, y=y, move=move, move_y=move_y, show_print=show_print)
        self._close_turtle()

    def _draw_edges(self, edge=None, x=0, y=0, move=20, move_y=0, to=None, show_print=False):
        radius = 10
        if edge is None:
            edge = self.edges[0]
            t.setpos(x, y)
            self._draw_edge(edge, radius)
        else:
            if to == "left":
                t.setpos(x, y)
                self._draw_edge(edge, radius)
            elif to == "right":
                t.setpos(x, y)
                self._draw_edge(edge, radius)
        if show_print:
            print(x, y, "edge:", edge.value)
        if edge.left is not None:
            x_from = x
            y_from = y
            from_where = (x_from, y_from)
            x_to = x-move
            y_to = y-[move_y, move][move_y == 0]
            to_where = (x_to+radius*np.sqrt(2), y_to+radius*np.sqrt(2))
            if show_print:
                print("Going from", from_where, "to", to_where)
            
            self._draw_bridge(from_where, to_where)
            if move_y == 0:
                self._draw_edges(edge.left, x-move, y-move, move, to="left")
            else:
                self._draw_edges(edge.left, x-move, y-move_y, move*0.9, move_y, to="left")
        if edge.right is not None:
            x_from = x
            y_from = y
            from_where = (x_from, y_from)
            x_to = x+move
            y_to = y-[move_y, move][move_y == 0]
            to_where = (x_to-radius*np.sqrt(2), y_to+radius*np.sqrt(2))
            if show_print:
                print("Going from", from_where, "to", to_where)

            self._draw_bridge(from_where, to_where)
            if move_y == 0:
                self._draw_edges(edge.right, x+move, y-move, move, to="right")
            else:
                self._draw_edges(edge.right, x+move, y-move_y, move*0.9, move_y, to="right")

    def _close_turtle(self):
        t.hideturtle()
        # t.done()


if __name__ == "__main__":
    

    text = "vklmnoijqrstabcupdefghwxyz"#.upper()
    # text="abcaabs"
    # text = "5 15 10 12 13"
    tree = Tree(text)
    # tree.draw_edges(move=40, move_y=20)
    tree.draw_edges()
