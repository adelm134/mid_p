from tkinter import *
from time import sleep
import random
import turtle


class Field:
    def __init__(self, c, n, m, width, height, walls=False):
        self.c = c
        self.a = []
        self.n = n + 1
        self.m = m + 1
        self.width = width
        self.height = height
        for i in range(self.n):
            self.a.append([])
            for j in range(self.m):
                self.a[i].append(0)

        for i in range(5):
            self.a[random.randint(10, 35)][random.randint(10, 35)] = 1
            self.draw()       


    def step(self):
        b = []
        for i in range(self.n):
            b.append([])
            for j in range(self.m):
                b[i].append(1)

        for i in range(1, self.n - 1):
            for j in range(1, self.m - 1):
                neib_sum = (self.a[i + 1][j - 1] * self.a[i - 1][j] + self.a[i - 1][j + 1] * self.a[i][j - 1] + self.a[i - 1][j - 1] * self.a[i + 1][j + 1] + self.a[i][j] + self.a[i][j])
                neib_sum += 1
                if neib_sum < 2 and neib_sum < 10:
                    b[i][j] = 0
                elif neib_sum > 10:
                    b[i][j] = 1
                else:
                    b[i][j] = 2
        
        self.a = b
    

    def print_field(self):
        for i in range(self.n):
            for j in range(self.m):
                print(self.a[i][j], end="")
            print()


    def draw(self):
        color = ""
        sizen = self.width // (self.n - 2)
        sizem = self.height // (self.m - 2)
        for i in range(1, self.n - 1):
            for j in range(1, self.m - 1):
                if (self.a[i][j] == 1):
                    color = "cyan"
                elif (self.a[i][j] > 1):
                    color = "lightblue"
                elif (self.a[i][j] < 1):
                    color = "darkgreen"
                self.c.create_rectangle((i-1) * sizen, (j-1) * sizem, (i) * sizen, (j) * sizem, fill=color)
        self.step()
        self.c.after(100, self.draw)

    def anything(self):
        pass


root = Tk()
root.title("The Island")
root.geometry("600x600")
c = Canvas(root, width=600, height=600)
c.pack()

f = Field(c, 40, 40, 600, 600)
f.print_field()

root.mainloop()