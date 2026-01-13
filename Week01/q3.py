# Order of Operations: Define 4 variables a, b, c, d and give them the values 1, 2, 3, 4. The fully bracketed version of
# e = a * c - b / d is
# e = (a * c) - (b / d)
# Given the following line of code, give the Fully-Bracketed Version of:
# e = a - b ** c // d + a % c

a = 1
b = 2
c = 3
d = 4

e = ((a - (b ** c)) // d) + (a % c)
print(e)
