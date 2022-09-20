def nth_power(exponent):
    def pow_of(base):
        return pow(base,exponent)
    return pow_of
square=nth_power(3) #the square is holding the inner function 
print(square(5))