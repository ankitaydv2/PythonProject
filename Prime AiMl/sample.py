# f = open("sample", "r") #file object
# #data = f.read()
# #print(data)
# data = f.readline()
# print(data)
#
# data = f.readline()
# print(data)
#
# print(type(data))
#
# f.close() # have to close a file , its imp

# f = open("sample", "w") #file object
# f.write("Text to overwrite \n the complete data.")
# f.close()

# WITH KEYWORD
with open("sample", "r") as f:
    print(f.read())
    data = f.read()
    print(len(data))