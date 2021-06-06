import turtle


# Aplhabet: A, B
# F: forward
# +: right turn
# -: left turn
# 2d
# A -> -BF+AFA+FB-
# B -> +AF-BFB-FA+

def system(iters, axiom, rules):
    if iters == 0: 
        return axiom
    return create_l_system(iters-1, "".join(rules[i] if i in rules else i for i in axiom), rules)

def draw(instructions, angle, distance):
    for command in instructions:
        if command == 'F': 
            turtle.forward(distance)
        elif command == '+': 
            turtle.right(angle)
        elif command == '-': 
            turtle.left(angle)

def main(iterations, axiom, rules, angle, length=10):
    turtle.speed(100)
    inst = system(iterations, axiom, rules)
    draw(inst, angle, length)
    turtle.hideturtle()
    turtle.exitonclick()

axiom = "A"
rules = {"A":"-BF+AFA+FB-", "B":"+AF-BFB-FA+"}
iterations = 3
angle = 90

main(iterations, axiom, rules, angle)
