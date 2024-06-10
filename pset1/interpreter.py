def interpreter():
    math_input = input("Expression: ")
    split_input = math_input.split(" ")
    x = int(split_input[0])
    y = split_input[1]
    z = int(split_input[2])

    symbol(x,y,z)

def symbol(x,y,z):
    if y == '+':
        ans = x + z
    elif y == '-':
        ans = x - z
    elif y == '*':
        ans = x * z
    else:
        ans = x / z

    print(f"{ans:.1f}")


interpreter()
