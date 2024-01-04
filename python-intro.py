8*2.5
#integer division; rounds down
10 // 3
50 > 25

month = 12
day = 11
day_of_week = "Monday"
print (month, day)

degrees_cel = 25
degrees_fah = (9 / 5) * degrees_cel + 32
print(degrees_fah)

a = 98
b = 58
c = 74
average_grade = (a + b + c) / 3
print(average_grade)


def C2F(degrees_c):
  '''docstring comment'''
  degrees_f = (9 / 5) * degrees_c * 32
  return degrees_f

print(C2F(100))
help(C2F)

def salestax_calc(price, tax_rate=0.13):
  tax_amount = price * tax_rate
  return tax_amount

salestax_calc(5)

def total_bill(price, tax_rate=0.13, tip_rate=0.2): #default values must come at the end
  tax = price * tax_rate
  tip = price * tip_rate
  total = price + tax + tip
  return total

total_bill(tip_rate=0.22, price=100)
