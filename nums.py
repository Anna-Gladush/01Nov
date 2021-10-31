num = int(input())
def find_missing_nums(num):

    nums = []
    numb = []

    for i in range(num):
        nums.append(int(input()))
        if i == 0 in nums:
            print("Error")
            break
        elif i > len(nums):
            print("Error")
            break
    # print(nums)

    for x in range(1, len(nums) + 1):
        if x in nums or x == 0:
            pass
        else:
            numb.append(x)
    print(numb)


find_missing_nums(num)
