class Number:
    def __init__(self, num, old, new = 0):
        self.num = num
        self.old = old
        self.new = new

n = int(input())
lst = list(map(int, input().split()))
nums = []

for i in range(n):
    nums.append(Number(lst[i], i + 1))

nums.sort(key = lambda x: (x.num, x.old))

for i in range(n):
    nums[i].new = i + 1

nums.sort(key = lambda x: x.old)

for i in range(n):
    print(nums[i].new, end = " ")