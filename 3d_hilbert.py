from math import sin, cos, sqrt
import turtle


p = 3 # the number of iterations used in constructing the Hilbert curve
n = 3 # the number of dimensions

def rotate(x: float, y: float, r: float):
    return x * cos(r) - y * sin(r), x * sin(r) + y * cos(r)

def binary_repr(num: int, width: int) -> str:
    return format(num, 'b').zfill(width)

def integer_transpose(h: int):
    global p, n
    return [int(binary_repr(h, p * n)[i::n], 2) for i in range(n)]

def hilbert_point(distance: int):
    global p, n
    x = integer_transpose(int(distance))
    z = 2 << (p - 1)
    # Gray decode by H ^ (H/2)
    t = x[n - 1] >> 1
    # Corrected error in Skilling's paper on the following line. The appendix had i >= 0 leading to negative array index.
    for i in range(n - 1, 0, -1):
        x[i] ^= x[i-1]
    x[0] ^= t
    # Undo excess work
    q = 2
    while q != z:
        p = q - 1
        for i in range(n - 1, -1, -1):
            if x[i] & q:
                x[0] ^= p # invert
            else:
                t = (x[0] ^ x[i]) & p
                x[0] ^= t
                x[i] ^= t
        q <<= 1
    return x

def hilbert_points(distances: int):
    ''''''
    return list(map(hilbert_point, distances))

points = hilbert_points(list(range(512)))

pointer = turtle.Turtle()
pointer.pencolor('green')
# Turn off move time, makes drawing instant,
turtle.tracer(0, 0)
pointer.up()

FOV = 200
counter = 0

while True:
    # Clear screen
    pointer.clear()
    # Draw
    for point in points:
    # Get the X, Y, Z coords out of the vertex iterator,
        x, y, z = point
        # Rotate
        x, z = rotate(x, z, counter)
        y, z = rotate(y, z, counter)
        x, y = rotate(x, y, counter)
        # Perspective formula
        z += 5
        f = FOV / z
        sx, sy = x * f, y * f
        # Move to and draw point
        pointer.down()
        pointer.goto(sx, sy)
        pointer.dot(3)
        pointer.hideturtle()
        pointer.up()

    # Update
    turtle.update()
    counter += 0.025