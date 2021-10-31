num = int(input("Print the number of items in the list "))
def is_monotonic(num):
    nums=[]
    for i in range(num):
        nums.append(int(input("Print the numbers themselves ")))
        if i == 0 in nums:
            print("Error")
            break
        elif i > len(nums):
            print("Error")
            break
    print(nums)
    print(bool(nums == sorted(nums) or (nums == sorted(nums, reverse=True))))


is_monotonic(num)
