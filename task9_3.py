l1 = list(map(int, input().split()))


s1 = set({})

for i in l1:
    if i in s1: 
        print(f"{i}: Yes")
    else: 
        s1.add(i)
        print(f"{i}: No")
