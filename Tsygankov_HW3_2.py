# Tsygankov_HW3_2
import turtle


def koch_curve(t, order, edge):
    if order == 0:
        t.forward(edge)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, edge / 3)
            t.left(angle)

def koch_snowflake(t, order, edge):
    for _ in range(edges):
        koch_curve(t, order, edge)
        t.right(360/edges)

def draw_koch_snowflake(order, edge=900):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-edge /4, edge /4)
    t.pendown()  

    koch_snowflake(t, order, edge/(0.5*order))

    window.mainloop()

if __name__ == "__main__":
 edges = int(input("Enter the edges of the Koch snowflake: "))
 order = int(input("Enter the order of the Koch snowflake: "))
 draw_koch_snowflake(order)
