import turtle


# F: forward
# +: right turn
# -: left turn

# Coch snowflake
# axiom = "F--F--F"
# rules = {"F":"F+F--F+F"}
# iterations = 4
# angle = 60

def draw_l_system(instructions, angle, distance):
    for command in instructions:
        if command == 'F': 
            turtle.forward(distance)
        elif command == '+': 
            turtle.right(angle)
        elif command == '-': 
            turtle.left(angle)

def create_l_system(iters, axiom, rules):
    if iters == 0: 
        return axiom
    return create_l_system(iters-1, "".join(rules[i] if i in rules else i for i in axiom), rules)

def main(iterations, axiom, rules, angle, length=8):
    turtle.speed(100)
    inst = create_l_system(iterations, axiom, rules)
    draw_l_system(inst, angle, length)
    turtle.hideturtle()
    turtle.exitonclick()

axiom = "F--F--F"
rules = {"F":"F+F--F+F"}
iterations = 2
angle = 60

main(iterations, axiom, rules, angle)
