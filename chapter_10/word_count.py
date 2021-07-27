def count_words(filename):
    try:
        with open(filename, encoding='UTF-8') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print('No file found')
    else:
        words = contents.split()
        num_words = len(words)
        print('The file ' + filename + ' has ' + str(num_words) + ' words')
    

#filename = 'alice.txt'
#filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
#for filename in filenames:
#    count_words(filename)

###练习加法运算：提示用户输入2个数字，并打印相加的结果。当用户输入的任何一个不是数字的时候都捕获TypeError异常
def add():
    while True:
        print('Please input two numbers:')
        temp1 = input()
        temp2 = input()
        try:
            a = int(temp1)
            b = int(temp2)
        except ValueError:
            if temp1 != 'q' or temp2 != 'q':
                print("You input 'q', now quit")
            else:
                print('You don\'t input a number') 
        else:
            print(a + b)
        
        if temp1 == 'q' or temp2 == 'q':
            break
       
#add()

###练习读取2个文件dogs和cats的内容并打印出来
def read_file(file_name):
    try:
        with open(file_name) as fileobject:
            contents = fileobject.read()
    except FileNotFoundError:
            print('You don\'t have this file')
    else:
        print(contents)

'''
filenames = ['dogs.txt', 'cats.txt']
for filename in filenames:
    read_file(filename)
'''
