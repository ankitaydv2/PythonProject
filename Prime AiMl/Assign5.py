from textwrap import indent
import json
# names = [input(f"Enter Names{i+1}: ") for i in range(5)]
#
# with open("names", 'w') as f:
#     json.dump(names, f, indent = 4)

with open("names" , 'r') as f:
    print(f.read())

