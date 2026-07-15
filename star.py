import turtle

star = turtle.Turtle()
star.speed(10)

colors =["red","green","blue"]
        
for i in range(60):
    star.color(colors[i % len(colors)])

    star.forward(i*10)
    star.right(144)

turtle.done()
