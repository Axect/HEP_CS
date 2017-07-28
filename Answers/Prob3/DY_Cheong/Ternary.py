class Ternary_Operation():
    def __init__(self, ternary):
        self.ternary= ternary%3
    
    

    def __add__ (self, other): # overrun the addition to use "+"
        sum = self.ternary + other.ternary
        tsum = sum % 3
        
        return Ternary_Operation(tsum)
    
    def __mul__(self, other): #overrun the multiplication to use "*"
        mult = self.ternary * other.ternary
        tmult = mult % 3

        return Ternary_Operation(tmult)

    def __xor__(self, other):
        if self.ternary == 0:
            return "Not defined"

        else:
            if other == 0 : 
                return 1
            
            elif other <0 : 
                return "Not defined"

            else : 
                power = int(other)

                for i in range(1, power+1):
                    self.ternary = self.ternary*self.ternary
                    i = i+1

                return Ternary_Operation(self.ternary % 3)

    def __str__(self):
        return "%i [Ternary]"%(self.ternary)

A = Ternary_Operation(int(input("A? ")))
B = Ternary_Operation(int(input("B? ")))


C = A+B
D = A*B
E = B^2

print(A)
print(C)
print(D)
print(E)


