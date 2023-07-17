def find_missing_ranges(nums, lower, upper):
  ranges = []
  current_range = [lower]
  for num in nums:
    if num < current_range[0]:
     
      ranges.append([num, num])
    elif num > current_range[1]:
     
      ranges.append(current_range)
      current_range = [num]
    else:
      current_range[1] = num
  if current_range[0] != upper:
   
    ranges.append(current_range)
  ranges.sort()
  return ranges


if __name__ == "__main__":
  nums = [0, 1, 3, 50, 75]
  lower = 0
  upper = 99
  print(find_missing_ranges(nums, lower, upper))
