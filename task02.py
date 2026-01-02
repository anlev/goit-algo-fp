import turtle


def draw_pythagoras_tree(length, level):
    if level == 0:
        return

    turtle.forward(length)

    turtle.left(45)
    draw_pythagoras_tree(length * 0.7, level - 1)

    turtle.right(90)
    draw_pythagoras_tree(length * 0.7, level - 1)

    turtle.left(45)
    turtle.backward(length)


def main():
    level = int(input("Enter recursion level: "))

    turtle.speed(0)
    turtle.left(90)
    turtle.penup()
    turtle.goto(0, -250)
    turtle.pendown()

    draw_pythagoras_tree(120, level)

    turtle.done()


if __name__ == "__main__":
    main()
