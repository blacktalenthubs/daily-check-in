import math
from multiprocessing import heap

print(math.fmod(-10,3))

print(math.floor(3/2))
print(math.ceil(3/2))
print(math.pow(2,3))
print(math.sqrt(2))

#max min

(float("inf"))
float("-inf")

nums = [3,2,5,4,5]
for i,num in enumerate(nums):
    print(num,i)

nums1 = [1,2,3,4,5]
nums2 = [6,7,8,9,10]



for num in zip(nums1,nums2):
    print(num)
nums1.reverse()
print((nums1))

string = "bolofinde"
stt = list(string)
stt.reverse()
print("".join(stt))

arr = [5, 4, 7, 3, 8]
arr.sort()
print(arr)

arr.sort(reverse=True)
print(arr)


names = ["bolofinde","adriel","dammy","michelle","data"]

numbers = [1,1,1,2,2,2,3,3,4,5,6,6,6,6,6,6,7,8,8,8,8,8,9]
names.sort()
print(names)

names.sort(key=lambda x:len(x))
print(names)

def frequency_count(nums):
    dic = {}

    for num in nums:
        if num in dic:
            dic[num]  +=1
        else:
            dic[num] =1
    return dict(sorted(dic.items(),key=lambda x:x[0],reverse=True))


print(frequency_count(numbers))

# 2-D lists
arr = [[0] * 4 for i in range(4)]
print(arr)
print(arr[0][0], arr[3][3])


# Valid numeric strings can be converted
print(int("123") + int("123"))

# And numbers can be converted to strings
print(str(123) + str(123))

print(ord("a"))
print(ord("b"))


from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
print(queue)

queue.popleft()
print(queue)

queue.appendleft(1)
print(queue)

queue.pop()
print(queue)

import heapq

minHeap = []

minHeap2 = []

data = ['b','c','a','d']

for char in data:
    heapq.heappush(minHeap2,data)

heapq.heappush(minHeap,3)
heapq.heappush(minHeap,2)
heapq.heappush(minHeap,4)
heapq.heappush(minHeap,1)
heapq.heappush(minHeap,0)
heapq.heappush(minHeap,6)
heapq.heappush(minHeap,10)
print(minHeap)
#print(minHeap[0])
#print(minHeap2)



while len(minHeap):
    print(heapq.heappop(minHeap))

maxHeap = []


lis = [3,2,4,1,0,6,10]

for num in lis:
    heapq.heappush(maxHeap,-1*num)

while len(maxHeap):
    print(-1*heapq.heappop(maxHeap))

arr = [2, 1, 8, 4, 5]
heapq.heapify(arr)
print(arr)
while arr:
    print(heapq.heappop(arr))