#file_name = 'pi_digits.txt'
file_name = 'pi_million_digits.txt'
with open(file_name) as file_object:
 #读取整个文件内容,返回的是str 
    #contents = file_object.read()
    #print(contents)
#逐行读取
    #for line in file_object:
        #print(line.rstrip())
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string[:52] + '......')
print(len(pi_string))
birth = input('You birthday?')
if birth in pi_string:
    print('Your birthday appears in the first million digits of pil')
else:
    print('Your birthday does not appear in the first million digits of pil')


###练习1打印文件中的内容
'''
file_name = 'learning_python.txt'
with open(file_name) as f:
    contents = f.read()
    print(contents.replace('python', 'C'))

    #for data in f:
    #    print(data)
    
    #data_lines = f.readlines()
'''
