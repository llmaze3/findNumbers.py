#author: Lloyd Powell
#returns all vaules between 100 and 1000 where
#(2^i + 2) can be divided by i

nums = [ x for x in range(100, 1001) if  (2 ** x + 2) % x == 0]
print(nums)
