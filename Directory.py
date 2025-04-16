import os
import shutil
# folders = ['scripts','libs','data']

# for f in folders:
#     try:
#         shutil.rmtree(f)#delete folders
#         # os.makedirs(f)#creating folders
#     except OSError as err:
#         print(err)
'''detailed directory structure'''
# img = ['img1.jpg']
# # print(os.getcwd()) # to get the current directory path the code is running
# base = os.getcwd()
# newPath = os.path.join(base,img[0])
# print(newPath)

# '''sub-folders tree'''
# folders = ['scripts','libs','data']
# subfolders = ['pre','post']

# for folder in folders:
#     try:
#         os.makedirs(folder)
#     except OSError as err:
#         print(err)
# for f in subfolders:
#     path = os.path.join(base,folders[0],f)
#     try:
#         os.makedirs(path)
#     except OSError as err:
#         print(err)
# os.listdir(os.path.join(base,'data'))


'''bulk rename'''

# import os

# direcList = os.listdir()
# print(direcList)

# try:
#     os.rename(direcList[0], 'Renamed.py')
# except OSError as err:
#     print(err)

'''filtered search'''

import os 
dirlist = os.listdir()
filelist = [ x for x in dirlist if x.endswith('py')]
print(filelist)