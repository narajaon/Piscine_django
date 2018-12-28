#!/Users/narajaon/.brew/bin/python3

if __name__ == '__main__':
    file = open('numbers.txt', 'r')
    line = file.readline()
    print(line.replace(',', '\n'), end = '')
    file.close()
