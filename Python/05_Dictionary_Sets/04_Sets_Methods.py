#Sets Method

set1 = {34,66,78,1,56,1,34,101}

set1.add(201)
print(set1)

set1.remove(1)
print(set1)

set2={1001,2002,7007,3003,34,101}
set3=set1.union(set2)
print(set3)

set4=set1.intersection(set2)
print(set4)

set2.update(set1)
print(set2)

print(set1)
print(set2)
print(set1.issubset(set2))
print(set1.issuperset(set2))
print(set2.issuperset(set1))