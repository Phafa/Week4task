try:
    def basic_operation(x, y):
        summ = x + y
        divison = x / y
        multiplication = x * y
        subtraction = x - y
        return {"addition": summ, "subtraction": subtraction, "multiplication": multiplication, "division": divison}
    basic_operation(1, 1)
except (ValueError, ZeroDivisionError):
    pass 

try:
   def power_operation(base, exponent, **kwargs):
        result = base ** exponent
        if 'modulo' in kwargs:
            modulo = kwargs['modulo']
            result = result % modulo
        return result

   power_operation(1, 1)

except ValueError:
    pass
    

def apply_operation(summ, subtraction, multiplication, divison):
    result = list(map(lambda operate: operate[1], *operate[2], operate[3], operate[4]))
    print(result)
    apply_operation(x + y, x - y, x * y, x / y)

   
    
    









