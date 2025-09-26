num = int(input())

for i in range(num):
    if i == 0 or i == (num-1):
        print('*' * num)
    else:
        print('*',end='')
        print('.'* (num-2) , end='')
        print('*')