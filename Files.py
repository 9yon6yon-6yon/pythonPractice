
'''files in python'''
# with open('file.txt','r') as f:
#     readByte = f.read(8) # reading first eight letters including a space from the file
#     f.seek(0) #reseting the counter or file to read from the start
#     readLine = f.readline()
#     f.seek(0)
#     readAll = f.readlines()
# print(readByte)
# print(readLine)
# print(readAll)

'''write files'''
# l = ['This is line one', 'this is line 2']

# with open('writeThis.txt', 'w') as f: #overwrite on the file from start
#     f.writelines('\n'.join(l))
# newlines = ['\n','This is another new line e.g 3']
# with open('writeThis.txt','a') as f:
#     f.writelines('\n'.join(newlines))
'''reading with split operation like csv files'''

# xcords= []
# ycords = []

# with open('csv.csv', 'r') as f:
#     data = f.read()
# cordinates = data.split('\n')

# for c in cordinates:
#     x, y = c.split(',')
#     xcords.append(x)
#     ycords.append(y)

# print('X cordinate: ', xcords)
# print('Y cordinate: ', ycords)

'''zip a file'''

# from zipfile import ZipFile

# with ZipFile('filename.zip', 'w') as zip:
#     zip.write('file.txt')
#     print('FileZipped')


'''unzip a file'''

from zipfile import ZipFile

with ZipFile('filename.zip', 'r') as zip:
    zip.extractall()
    print('All files are extracted')
