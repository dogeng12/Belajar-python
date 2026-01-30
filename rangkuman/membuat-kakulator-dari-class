#ini adalah class kalkulator

class class_kalkulator:
    #ini adalah atribut class
    def __init__(self, num1, operator, num2):
        self.num1 = num1
        self.operator = operator
        self.num2 = num2
        
    #ini adalah method operasi matematika
    def kalkulator(self):
        #operator = self.operator
        if self.operator == "+":
            return self.num1 + self.num2
        elif self.operator == "*":
            return self.num1 * self.num2
        elif self.operator == "-":
            return self.num1 - self.num2
        elif self.operator == "/":
            if self.num1 == 0:
                return 0
            return self.num1 / self.num2
        else:
            return 0   
           
kalkulator1 = class_kalkulator(8,"+",9)
kalkulator2 = class_kalkulator(3,"-",4)
kalkulator3 = class_kalkulator(8,"*",6)
kalkulator4 = class_kalkulator(0,"/",0)

print(kalkulator1.kalkulator())
print(kalkulator2.kalkulator())
print(kalkulator3.kalkulator())
print(kalkulator4.kalkulator())