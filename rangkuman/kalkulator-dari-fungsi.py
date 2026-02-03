ini adalah fungsi kalkulator biasa!

def kalkulator(op, num1,num2):
        if op == "+":
            return num1 + num2
        elif op == "*":
            return num1 * num2
        elif op == "-":
            return num1 - num2
        elif op == "/":
            if num1 == 0:
                return 0
            return num1 / num2
        else:
            return "mohon masukan (nomor) dan (operator) dengan benar!"