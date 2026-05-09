set1 = set(map(int, input("Enter elements of Set 1: ").split()))
set2 = set(map(int, input("Enter elements of Set 2: ").split()))

print("\nUnion:", set1.union(set2))

print("Intersection:", set1.intersection(set2))

print("Symmetric Difference:", set1.symmetric_difference(set2))

print("Is Set1 subset of Set2?", set1.issubset(set2))