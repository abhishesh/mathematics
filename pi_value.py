# Calculate the value of pi till 1000 Digits
# Taken from https://en.wikipedia.org/wiki/Bailey-Borwein-Plouffe_formula


from decimal import Decimal, getcontext

getcontext().prec = 1000
print sum(1/Decimal(16)**n * (Decimal(4)/(8*n+1) - Decimal(2)/(8*n+4) - Decimal(1)/(8*n+5) - Decimal(1)/(8*n+6)) for n in range(1000))