berries = []
k = int(input())
for i in range(k):
     berries.append(int(input()))
n = len(berries)
max_berries = 0
for i in range(n):
    current = berries[i]
    left = berries[(i-1)%n]
    right = berries[(i+1)%n]
        
    total_berries = current + left + right
        
    max_berries = max(max_berries, total_berries)
print(max_berries)