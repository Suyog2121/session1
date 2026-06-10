#Find Duplicate Elements in a List
_1st = [1, 2, 3, 4, 2, 5, 1]

duplicates = []

for i in _1st:
    if _1st.count(i) > 1 and i not in duplicates:
        duplicates.append(i)

print("Duplicates: ", duplicates)
