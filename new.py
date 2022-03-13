# Create a circle
from ctypes import alignment
from tkinter.ttk import Style
import turtle 
import math
while True:
    user_radius = int(input("Radius: "))
    # Display Radius
    if user_radius > 1 or user_radius < 201:

        def display_radius():
                tur = turtle.Turtle()
                tur.hideturtle()
                tur.goto(user_radius,0)

        # Display a circle   

        def drawCircle(x,y,user_radius):
                tur = turtle.Turtle()
                tur.pu()
                tur.goto(x,y-user_radius)
                tur.pd()
                tur.circle(user_radius)
                tur.hideturtle()
        # Display text on the window view

        def display_text():
                style = ('Arial', 20, 'normal')
                turtle.up()  # get rid of line
                turtle.setposition(-95,220)
                turtle.hideturtle()
                turtle.write('HAPPY PI DAY!', font=style)
        
        # calculate area of circle 

        area = round((math.pi * (user_radius ** 2)),3)
        circumference = round((2 * math.pi * user_radius),3)
        def result_area():
            style = ('Arial', 15, 'normal')
            turtle.up() 
            turtle.setposition(-250,-200)
            turtle.write(f'Area :{area}', font=style)
        
        def result_circumference():
            style = ('Arial', 15, 'normal')
            turtle.up() 
            turtle.setposition(50,-200)
            turtle.write(f"Circumference :{circumference}", font=style)
        break
    else:
        style = ('Arial', 20, 'normal')
        turtle.write('Invalid Input', font=style)
        turtle.hideturtle()
        wn = turtle.Screen()
        wn.exitonclick()
        
        break

# Call python function 

display_text()
display_radius()
drawCircle(0,0,user_radius)
result_area()
result_circumference()
turtle.mainloop()







