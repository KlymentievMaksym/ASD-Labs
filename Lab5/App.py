import Tree as t
import time


class UI:
    def __init__(self):
        self.actions = {
            "-1": self.help,
            "0": self.exit,
            "1": self.tree,
            "2": self.draw_tree
        }

    def start(self):
        self.ask = input("What to do?\n>>> ")
        self.ask = self.ask.split()
        ask = self.ask.pop(0)
        if ask in self.actions:
            try: 
                self.actions[ask](*self.ask)
            except t.t.Terminator:
                print("Tree was terminated. Restart please!")
                self.exit()
        else:
            print("Wrong input")
            self.start()

    def help(self):
        print("""
-1. Help
0. Exit
1. Enter text
2. Draw tree

Can draw tree only once!
              """)
        self.start()

    def tree(self):
        self.answear = input("Enter text: ")
        self.tree = t.Tree(self.answear)
        self.start()

    def draw_tree(self, speed=20):
        try:
            self.tree.draw_edges(speed=speed)
            time.sleep(len(self.answear)*0.6)
        except AttributeError:
            print("No tree to draw")
            self.start()
            return
        t.t.bye()
        # Open a new window
        self.start()

    def exit(self):
        exit()


if __name__ == "__main__":
    UI().start()
    # a = t.Tree("5 15 10 12 13")
    # a.draw_edges()
