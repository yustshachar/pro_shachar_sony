import os
from time import *
from datetime import *

one = os.stat('C:/Users/yusts/Desktop/text_program_sony/pfile2.pptx')
age = one.st_mtime

print()
print(localtime(age).tm_year)
print(localtime(age).tm_mon)
print(localtime(age).tm_mday)

print()
print(datetime(localtime(age).tm_year, localtime(age).tm_mon, localtime(age).tm_mday))
