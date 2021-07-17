from os import path
from time import *
from datetime import *

file = 'C:/Users/yusts/Desktop/text_program_sony/pfile2.pptx'

# תאריך שינוי
print(path.getatime(file))
print(datetime(localtime(path.getatime(file)).tm_year, localtime(path.getatime(file)).tm_mon, localtime(path.getatime(file)).tm_mday))

# תאריך יצירה
print(path.getctime(file))