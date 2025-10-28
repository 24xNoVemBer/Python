n= int(input())
a= list(map(int, input().split()))
stack = []
for x in a:
    if stack and (x+stack[-1]) % 2 == 0:
        stack.pop()
    else:
        stack.append(x)
print(len(stack))