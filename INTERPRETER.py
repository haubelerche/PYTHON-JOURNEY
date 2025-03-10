#prompt user for arithmetic expression
expression = input("Expression: ")
x, y, z = expression.split(" ")
#output res as a floating point value
xmoi = float(x)
zmoi = float(z)
if y == "+":
    res = xmoi + zmoi
if y == "-":
    res = xmoi - zmoi
if y == "*":
    res = xmoi * zmoi
if y == "/":
    res = xmoi / zmoi
print(res)
