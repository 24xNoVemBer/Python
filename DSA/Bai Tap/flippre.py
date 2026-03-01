s = input().strip()

steps = 0
flipped = False

for i in s:
    current = i

    if flipped:
        if current == 'A':
            current = 'B'
        else:
            current = 'A'

    if current == 'B':
        steps += 1
        flipped = not flipped
    if flipped:
        steps += 1
print(steps)
