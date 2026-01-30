# n =5
# fact = 1
# i =1
# while(i < n):
#   fact *= i
#   i +=1
# print(fact)

def calFact(n):
    fact = 1
    for i  in range(1, n+1):
        fact *= i
    return fact
n = int(input("Enter a number : "))
print(calFact(n))