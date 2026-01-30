#Range -> range(start, stop, step)

# 1) 2 table
# for i in range(2, 11, 2):
#     print(i)

#2)
# for j in range(1, 10, 1):
#     print(j)

# 3)  Print sum of 1st natural number
sum = 0
for h in range(1, 6+1):
    sum += h
print(sum)

#Functions - block of satements that performs tasks -> 1. Definitions 2) Call functn
def hello():
    print("Whyy")
hello()

def sum(b, d):
    sum = b + d
    return sum
print(sum(34, 56))

def calAvg(num1 , num2, num3):
    sum=num1+num2+num3
    avg = sum/3
    return avg
print(calAvg(34, 49, 92))

def sum(a, b=58):
    return(a + b)
print(sum(5))

#Types of Functions - BuiltIn - print(), input(), type(), range() & User Defined - sum , avg
#lambda Functn
sum = lambda a, b, c: a+b+c
print(sum(15,22,39))


