data = True
line = 1
word ="demo"

with open("WordSearch", "r") as f:
    while data:
        data = f.readline()

        if(word in data):
            print(f"{word} found at line {line}")
            break

        line += 1

