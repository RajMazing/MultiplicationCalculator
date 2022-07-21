num = int(input('Please, choose how many times you want.\t '))

for i in range(1,(num+1)):
    print('\n')
    for k in range(1,11):
        print(i, 'X', k, '=', i*k)
