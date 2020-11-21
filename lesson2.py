ages = [10, "da", 90, 15]
ages.append(91)
ages.extend([1, 1,])

# print(ages)
# print(ages[2])
# print(ages[3])

nums = []

d = 1
while d < 5:
    num = int(input())
    nums.append(num)
    d = d + 1
    # print(nums, d)
print(nums)

d = 0

while d < 5:
    nums[d] = int(input())
    d = d + 1

print(nums)
