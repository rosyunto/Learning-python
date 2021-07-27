print('Pleaes input two numbers, I will divide them.')
print('Enter q to quit')

while True:
    first_number = input('First number:')
    if first_number == 'q':
        break
    second_number = input('Second number:')
    if second_number == 'q':
        break
    #处理除以0异常
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print('you can\'t divide by 0')
    else:
        print(answer)
    
    