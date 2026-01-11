n = int(input())
inside = set()

for _ in range(n):
    name, action = input().split()
    if action == "enter":
        inside.add(name)
    elif action == "leave":
        inside.remove(name)
        
for name in sorted(inside, reverse=True):
    print(name)