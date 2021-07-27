###处理Filenotfounderror异常

file_name = 'alice.txt'

try:
    with open(file_name,encoding = 'UTF-8') as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print('file not found')
else:
    words = contents.split()
    num_words = len(words)
    print('There are ' + str(num_words) +' in ' + file_name )

    
