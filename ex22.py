
list_1 = []
list_2 = []
n = int(input())
m = int(input())

for i in range(n):
     list_1.append(int(input()))

for i in range(m):
     list_2.append(int(input()))

set_1 = set(list_1)
set_2 = set(list_2)

result = list(set_1.union(set_2).difference(set_1.intersection(set_2)))

result = sorted(result)

print(result)