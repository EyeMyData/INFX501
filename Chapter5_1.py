def NumberSummary():
    total = 0
    count = 0
    average = 0
    while True:
        try:
            x = input('Enter a number :')
            if x == 'done':
                break
            total = total + int(x)
            count = count + 1
            average = float(total)/float(count)
        except ValueError:
            print('Invalid input')
    print(total, count, average)
    print('Total is ',total)
    print('Valid entries ',count)
    print('Average is ',average)

NumberSummary()

