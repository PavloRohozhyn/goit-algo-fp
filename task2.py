import turtle
import math

def draw_pythagoras_tree(t, length, depth, angle):
    if depth == 0:
        return
    # main branch
    t.pencolor('brown')
    t.forward(length)
    t.left(angle)
    # left branch
    draw_pythagoras_tree(t, length * math.sqrt(0.6), depth - 1, angle)
    # right branch
    t.right(2 * angle)
    draw_pythagoras_tree(t, length * math.sqrt(0.6), depth - 1, angle)
    # return to main point
    t.left(angle)
    t.backward(length)

def main():
    # tree params
    length = 100
    angle = 45
    depth = int(input("Input recursion level (WE RECOMMENDING MAXIMUM 10): "))
    window = turtle.Screen()
    window.title("Pythagoras tree")
    # setup turtle
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    # go!
    draw_pythagoras_tree(t, length, depth, angle)
    window.mainloop()

if __name__ == "__main__":
    main()