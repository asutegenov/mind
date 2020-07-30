import math

class Expressions():
    
    def mult(self, first, second):
        return float(first) * float(second)
    
    def div(self, first, second):
        if float(second) == 0:
            return "Нельзя делить на ноль!"
        elif float(first) == float(second):
            return 1
        else:
            return float(first)/float(second)
    
    def sub(self, first, second):
        return float(first)-float(second)
    
    def sub_abs(self, first, second):
        return math.fabs(float(first)-float(second))

    def add(self, first, second):
        return float(first) + float(second)

