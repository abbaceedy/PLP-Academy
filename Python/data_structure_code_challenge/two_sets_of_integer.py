set1 = set()
set2 = set()

print ('Enter five integers')
for i in range(5):
  num = int(input())
  set1.add(set1)

print ('Enter another five integers')
for i in range(5):
  num2 = int(input())
  set2.add(set2)

sets_inter = (set1.intersection(set2))

print(sets_inter)

