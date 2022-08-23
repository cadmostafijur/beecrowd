#1043 - Triangle

a,b,c=map(float,input().split())
if a+b>c and b+c>a and c+a>b:
  p=(a+b+c)
  print("Perimetro = %.1f"%p)
else:
  A = 0.5 * (a + b) * c
  print("Area = %.1f"%A)