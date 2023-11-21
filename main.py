from sympy import symbols, Eq, solve
a, b, c = symbols('a b c')
eq1 = Eq(10, c)
eq2 = Eq(2, a * 50**2 + b *50+10)
eq3 = Eq(1, a*100**2+b*100+10)
solution = solve((eq1,eq2,eq3),(a,b,c))
print(solution)