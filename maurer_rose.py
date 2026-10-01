import turtle
import math
import colorsys

# Screen Setup for Instagram Reels (9:16 Aspect Ratio)
screen = turtle.Screen()
screen.setup(width=540, height=960)
screen.bgcolor("#020205")  # Deep dark background for max contrast
screen.title("Day 03: Vibrant Maurer Rose - Coding With Vishesh")

# Tracer update speed set for slow & smooth 25-30 second animation
screen.tracer(1, 4)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(2)  # Thicker glowy lines

# Maurer Rose Dynamic Parameters
n = 6       # Petals count
d = 71      # Angular step degree
radius = 230

# Loop for ~25-30 Seconds Execution
for i in range(361):
    k = i * d
    r = radius * math.sin(math.radians(n * k))
    
    # Polar to Cartesian coordinate mapping
    x = r * math.cos(math.radians(k))
    y = r * math.sin(math.radians(k))
    
    # Ultra Vibrant High-Saturation Neon Color Gradient
    hue = (i * 0.0055) % 1.0
    rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)  # Max Saturation (1.0) & Value (1.0)
    t.pencolor(rgb)
    
    if i == 0:
        t.penup()
        t.goto(x, y)
        t.pendown()
    else:
        t.goto(x, y)

# Secondary Petal Outer Glow Layer
t.pensize(1.2)
for j in range(361):
    angle = math.radians(j)
    r_outer = radius * math.sin(n * angle)
    x_out = r_outer * math.cos(angle)
    y_out = r_outer * math.sin(angle)
    
    hue_out = (0.5 + j * 0.003) % 1.0
    t.pencolor(colorsys.hsv_to_rgb(hue_out, 1.0, 1.0))
    
    if j == 0:
        t.penup()
        t.goto(x_out, y_out)
        t.pendown()
    else:
        t.goto(x_out, y_out)

screen.update()
turtle.done()