# #1 Words occur in string
word = "artificial intelligence"
count = 0
for ch in word:
    if(ch == 'l'):
        count+=1
print(count)

#2 Print Vowels
word = "artificial intelligence"
count = 0

for ch in word:
    if ch in "aeiou":
        count += 1

print("Total vowels", count)
