nums = list(map(int, open("20.txt").readlines()))

# give each num its order
# nums = list(zip(nums, range(len(nums))))
nums = list(zip([n * 811589153 for n in nums], range(len(nums))))

# print(nums)

for a in range(10):
    for i in range(len(nums)):
        # find where this num is now
        for k, (n, p) in enumerate(nums):
            if p != i:
                continue

            # newpos = k + n
            # while newpos >= len(nums):
            #     newpos -= len(nums) - 1
            # while newpos <= 0:
            #     newpos += len(nums) - 1

            newpos2 = (k + n) % (len(nums) - 1)
            if newpos2 == 0:
                newpos2 = len(nums) - 1

            # if newpos != newpos2:
            #     print(newpos, newpos2)
            # print(k, n, newpos)

            # print([k for k,v in nums])
            del nums[k]
            nums.insert(newpos2, (n, p))
            # print([k for k,v in nums])
            # print(nums)
            break


# print(nums)
# for num in nums:

for k, (n, p) in enumerate(nums):
    if n == 0:
        k1 = k + 1000
        k2 = k + 2000
        k3 = k + 3000
        sol = nums[k1 % len(nums)][0] + nums[k2 % len(nums)][0] + nums[k3 % len(nums)][0]
        print(sol)
        
        
