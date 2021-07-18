from os import *
from time import *
from datetime import *
import shutil

library = input('enter library path: ')
max_age = input('maximum "age" of the files: ')

# if max_age[-1].isalpha() and max_age[:-1].isnumeric():
#     op = ["D", "W", "M", "Y"]
#     if max_age[-1].upper() in op:

for namefile in listdir(library):
    file = f"{library}/{namefile}"
    age = datetime.fromtimestamp(path.getmtime(file))
    # age = datetime(localtime(path.getmtime(file)).tm_year, localtime(path.getmtime(file)).tm_mon, localtime(path.getmtime(file)).tm_mday)
    if datetime.now().date() - age.date() <= timedelta(days=3):
        print("del!")
    print(namefile)
    print(age)
    print()

# יצירת תקייה
# mkdir(f'{library}/new_folder')

# מחיקת תיקייה
# rmdir(f'{library}/new_folder')

# יצירת קובץ זיפ מתקייה במיקום
# shutil.make_archive('C:/Users/yusts/Desktop/text_program_sony','zip','C:/Users/yusts/Desktop/text_program_sony')

# העברת מיקום הקובץ (פשוט שינוי הכתובת)
# rename('C:/Users/yusts/Desktop/text_program_sony/pfile2.pptx', 'C:/Users/yusts/Desktop/text_program_sony/zip_new.zip/pfile2.pptx')
