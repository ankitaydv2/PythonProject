#CONCATENATE - add the Strings
#1
# word1 = "I Love "
# word2 = "Python"
# print(word1+word2)

#2
# word = "WithoutYou"
# for ch in word:
#     print(ch)

#3
# in Python Strings are immutable. (1) Slicing (2) Formatting
#str = "Python"
#str[str idx : end idx]

#4
# word = "I study from JECRC college "
# print(word[4: 18])

#5 Formatting - dynamic Strings(var & vals) -> (1) format()- placeholder {}, placeholder value , (2) f-strings
# num1 = 5
# num2 = 10
# sum = num1 + num2
# print("Sum is {}".format(sum))
# print("Language is {}".format("Python"))

#6 Index based formatting
# a = 3
# b = 4
# sum = a+b
# print("Sum of {0} & {1} is {2}".format(a,b, sum))
# print("Sum of {1} & {0} is {2}".format(a,b,sum))

#7 Value Based Formatting
# print("Values of vars {a} & {b}".format(a = 5, b =10))

#8
num1 = 6
num2 = 54
print(f"Sum of {num1} & {num2} is {num1 + num2}")


