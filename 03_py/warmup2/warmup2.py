def string_splosion(str):
  x = 0
  ans = ""
  while x < len(str):
    ans += str[:x+1]
    x+=1
  return ans

def array_front9(nums):
  if 9 in nums:
    return nums.index(9) >= 0 and nums.index(9) < 4
  return False

def front_times(str, n):
  return str[:3]*n
print("hello")
