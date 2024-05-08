import turtle as t
import numpy as np
import time

"""
3. Побудувати словник зі слів текстового файлу у вигляді дерева
двійкового пошуку. Вивести його на екран у вигляді дерева. Здійснити пошук
вказаного слова у дереві і у файлі. Якщо слова немає, додати його при
необхідності в дерево і у відповідний файл. Видалити вказане слово з дерева
та файлу. Порівняти час пошуку в дереві та у файлі.
"""


class Edge:
    def __init__(self, value, left=None, right=None, index=0):
        self.value = value
        self.left = left
        self.right = right
        self.index = index

    def __str__(self):
        return str(self.value)


class Tree:
    def __init__(self, text=""):
        self.index = 0
        self.list = text.split()
        self.edges = None
        self._rearrange()

    def find_in_file(self, word, add_if_not_found=False, typ=int):
        for edge in self.edges:
            if typ(edge.value) == typ(word):
                return edge
        if add_if_not_found:
            return self._find_place(word, typ=typ)
        return -1

    def find_in_tree(self, word, edge=None, add_if_not_found=False, typ=int):
        if edge is None:
            edge = self.edges[0]
        if typ(edge.value) == typ(word):
            return edge
        if typ(word) <= typ(edge.value):
            if edge.left is None:
                if add_if_not_found:
                    return self._find_place(word, typ=typ)
                return -1
            else:
                return self.find_in_tree(word, edge.left, add_if_not_found, typ=typ)
        elif typ(word) > typ(edge.value):
            if edge.right is None:
                if add_if_not_found:
                    return self._find_place(word, typ=typ)
                return -1
            else:
                return self.find_in_tree(word, edge.right, add_if_not_found, typ=typ)
        # return 0

    def delete_in_tree(self, word, edge=None, typ=int, prev_edge=None, prev_state=None):
        if edge is None:
            edge = self.edges[0]

        if typ(edge.value) == typ(word):
            if edge.left is None and edge.right is None:
                self.edges.remove(edge)
                if prev_state == "left":
                    prev_edge.left = None
                elif prev_state == "right":
                    prev_edge.right = None
            elif edge.left is None and edge.right is not None:
                self.edges.remove(edge)
                if prev_state == "left":
                    prev_edge.left = edge.right
                elif prev_state == "right":
                    prev_edge.right = edge.right
            elif edge.right is None and edge.left is not None:
                self.edges.remove(edge)
                if prev_state == "left":
                    prev_edge.left = edge.left
                elif prev_state == "right":
                    prev_edge.right = edge.left
            else:
                next_edge = self._min(edge.right)
                self.delete_in_tree(next_edge.value, typ=typ)
                # self.edges.remove(next_edge)
                self.edges[self.edges.index(edge)] = next_edge
                # self.edges.remove(edge)
                if prev_state == "left":
                    prev_edge.left = next_edge
                elif prev_state == "right":
                    prev_edge.right = next_edge
                next_edge.left = edge.left
                next_edge.right = edge.right
            return 0

        if typ(word) <= typ(edge.value):
            if edge.left is None:
                return -1
            else:
                self.delete_in_tree(word, edge.left, typ=typ, prev_edge=edge, prev_state="left")
        elif typ(word) > typ(edge.value):
            if edge.right is None:
                return -1
            else:
                self.delete_in_tree(word, edge.right, typ=typ, prev_edge=edge, prev_state="right")

    def _min(self, edge=None):
        if edge is None:
            edge = self.edges[0]
        if edge.left is None:
            return edge
        else:
            return self._min(edge.left)

    def _find_place(self, char, edge=None, typ=str):
        if edge is None:
            edge = self.edges[0]

        not_typ = False

        try:
            char = typ(char)
        except ValueError:
            not_typ = True

        if char <= [typ(edge.value), edge.value][not_typ]:
            if edge.left is None:
                edge.left = Edge(char, index=self.index)
                self.index += 1
                self.edges += [edge.left]
            else:
                self._find_place(char, edge.left, typ=typ)

        elif char > [typ(edge.value), edge.value][not_typ]:
            if edge.right is None:
                edge.right = Edge(char, index=self.index)
                self.index += 1
                self.edges += [edge.right]
            else:
                self._find_place(char, edge.right, typ=typ)

    def _rearrange(self):
        for word in self.list:
            if len(self.list) != 1:
                typ = int
                try:
                    word = int(word)
                except ValueError:
                    typ = str
                if self.edges is None:
                    self.edges = [Edge(word, index=self.index)]
                else:
                    self._find_place(word, typ=typ)
            else:
                for char in word:
                    if self.edges is None:
                        self.edges = [Edge(char, index=self.index)]
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

    def draw_edges(self, x=0, y=0, move=20, move_y=0, show_print=False, pensize=3, speed=20, mult=0.9):
        t.pen(pensize=pensize, speed=speed)
        t.penup()
        self._draw_edges(x=x, y=y, move=move, move_y=move_y, show_print=show_print, mult=mult)
        self._close_turtle()

    def _draw_edges(self, edge=None, x=0, y=0, move=20, move_y=0, to=None, show_print=False, mult=0.9):
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
                self._draw_edges(edge.left, x-move, y-move, move, to="left", mult=mult)
            else:
                self._draw_edges(edge.left, x-move, y-move_y, move*mult, move_y, to="left", mult=mult)
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
                self._draw_edges(edge.right, x+move, y-move, move, to="right", mult=mult)
            else:
                self._draw_edges(edge.right, x+move, y-move_y, move*mult, move_y, to="right", mult=mult)

    def _close_turtle(self):
        t.hideturtle()
        if __name__ == "__main__":
            t.exitonclick()
        # time.sleep(3)
        # t.done()


if __name__ == "__main__":
    i = 2
    match i:
        case 0:
            # text = "vklmnoijqrstabcupdefghwxyz"#.upper()
            text = "bfs"
            tree = Tree(text)
            tree.find_in_tree("a", add_if_not_found=True, typ=str)
            tree.find_in_tree("v", add_if_not_found=True, typ=str)
            tree.find_in_tree("g", add_if_not_found=True, typ=str)
            # tree.delete_in_tree("v", typ=str)
            # tree.delete_in_tree("s", typ=str)
            tree.draw_edges()
        case 1:
            text = "8 3 1 6 4 7 10 14 13"
            tree = Tree(text)
            tree.delete_in_tree(3, typ=int)
            # tree.draw_edges(move=40, move_y=20, mult=0.75)
            # tree.draw_edges()
            start_tree = time.time()
            print(tree.find_in_tree(3, typ=int))
            end_tree = time.time()

            start_file = time.time()
            print(tree.find_in_file(3, typ=int))
            end_file = time.time()
            result = (end_tree-start_tree) - (end_file-start_file)
            if result > 0:
                print("Tree is faster than file", abs(result))
            elif result == 0:
                print("File and tree are equal", abs(result))
            else:
                print("File is faster than tree", abs(result))
        case 2:
            text = "12 5 2 11 6 8 18 19"
            tree = Tree(text)
            # tree.delete_in_tree(5, typ=int)
            tree.draw_edges(move=40, move_y=20, mult=0.75)
            # tree.draw_edges()
