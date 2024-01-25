import turtle
import random

class PyTurtle(turtle.Turtle):
    def __init__(self, pointer_shape):
        super(PyTurtle, self).__init__(pointer_shape)
        self.pointer_shape = pointer_shape
        self.shape(self.pointer_shape)
        self.penup()
        self.goto(-50, 200)
        self.pendown()

    def change_color(self):
        r_pen = random.randint(0, 255)
        g_pen = random.randint(0, 255)
        b_pen = random.randint(0, 255)
        r_fill = random.randint(0, 255)
        g_fill = random.randint(0, 255)
        b_fill = random.randint(0, 255)
        turtle.colormode(255)
        self.pencolor((r_pen, g_pen, b_pen))
        self.fillcolor((r_fill, g_fill, b_fill))
        
    def draw_polygons(self, start_size, end_size, side_length):
        self.side_length = side_length
        for size in range(end_size, start_size - 1, -1):
            self.change_color()
            total_angle = (size - 2) * 180
            self.turn_angle = 180 - total_angle / size
            self.begin_fill()
            for _ in range(size):
                self.forward(self.side_length)
                self.right(self.turn_angle)
            self.end_fill()
                
tim = PyTurtle("turtle")
tim.draw_polygons(3, 20, 50)

screen = turtle.Screen()
screen.exitonclick()
