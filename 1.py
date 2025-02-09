def draw_line(a, b, c):
    if c:
        print(a * b)
    else:
        for i in range(a):
            print(b)

draw_line(20, "@", True)
draw_line(20, "@", False)


