with open('synd.txt' , 'r') as file:
    print('[')
    for _ in range(32):
        
        print('[\'' + ''.join(file.readline().split('\n')).replace(' ', '') + '\']', end='')
        print(',')
    print(']')