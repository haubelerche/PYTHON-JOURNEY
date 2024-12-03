import sys


def main():
    if len(sys.argv) < 4:
        print("Usage: " + sys.argv[0] + " OPERAND OPERATOR OPERAND")
        return

try:
        a = float(sys.argv[1])
        op = sys.argv[2]
        b = float(sys.argv[3])
except ValueError:
    print("Invalid input. Please provide valid numbers and operator.")
    return

if op == '+':
        res = a + b
elif op == '-':
        res = a - b
elif op == '*':
        res = a * b
elif op == '/':
        res = a / b
else:
    print("Invalid operator: '{}'".format(op))
    return

    print(res)

if __name__ == "__main__":
    main()
