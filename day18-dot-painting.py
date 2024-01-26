import turtle
import random

class PyTurtle(turtle.Turtle):
    def __init__(self, pointer_shape):
        super(PyTurtle, self).__init__(pointer_shape)
        self.shape(pointer_shape)

    def prepare_colors(self, colors):
        self.color_list = []
        for _ in range(colors):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            self.color_list.append((r, g, b))

    def make_dot_painting(self, shapes, sides, colors, dot_size, gap_size):
        turtle.colormode(255)
        self.prepare_colors(colors)
        self.hideturtle()
        self.speed(0)
        self.penup()
        distance = dot_size + gap_size
        self.goto(distance * -shapes / 2, distance * -shapes / 2)
        self.pendown()
        initial_angle = (sides - 2) * 180 / sides
        turn_angle = 180 - initial_angle
        steps = 1
        self.left(initial_angle)
        while steps < shapes + 1:
            for _ in range(sides):
                for _ in range(steps):
                    self.pencolor(random.choice(self.color_list))
                    self.dot(dot_size)
                    self.penup()
                    self.forward(distance)
                    self.pendown()
                self.right(turn_angle)
            steps += 1
    
tim = PyTurtle("turtle")
tim.make_dot_painting(10, 4, 10, 25, 15)
screen = turtle.Screen()
screen.exitonclick()
