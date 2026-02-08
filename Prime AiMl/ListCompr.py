# squares = []
# for i in range(6):
#     squares.append(i*i)
# print(squares)

#eg 1.2
#sq= [o/p for i in range()  condn ]
# sq = [i*i for i in range(6)]
# print(sq)

# eg 1.3
#sq= [o/p for i in range()  condn ]
# sq = [i*i for i in range(6) if i%2!=0]
# print(sq)

#eg 2
nums = [-2, -3, 1, 4, -5, 6, 9, 0]
nums2= [0 if nums[i]<0 else nums[i] for i in range(len(nums))]
print(nums2)

nums1 = [-2, -3, 1, 4, -5, 6, 9, 0]
nums1 = [0 if val<0 else val for val in nums]
print(nums1)

words = ["hello", 'python', " amna"]
#print(words[0].upper())
words = [val.upper() for val in words]
print(words[0])