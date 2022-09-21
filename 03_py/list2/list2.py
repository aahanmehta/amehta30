def count_evens(nums):
  count = 0
  for i in nums:
    if i % 2 == 0:
      count += 1
  return count

def big_diff(nums):
  return max(nums) - min(nums)

def centered_average(nums):
  x, y, z = max(nums), min(nums), 0
  for i in nums:
    z += i
  z = z - y
  z = z - x
  return int(z/(len(nums)-2))

def sum13(nums):
  ct, i = 0, 0
  while i < len(nums):
    if nums[i] == 13:
      i+=2
    else:
      ct+=nums[i]
      i+=1
  return ct

def sum67(nums):
  inBetween = False
  sum = 0
  for i in nums:
    if i == 6:
      inBetween = True
    if not inBetween:
      sum+=i
    if i == 7:
      inBetween = False
  return sum

def has22(nums):
  for i in range(len(nums) -1):
    if nums[i] == 2 and nums[i+1] == 2:
      return True
  return False
