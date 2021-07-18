from os import listdir, path, rename, mkdir, walk
from dateutil.relativedelta import relativedelta
from datetime import datetime
from shutil import make_archive, rmtree

def check_library(library):
    while not path.isdir(f"{library}"):
        library = input("Enter a valid folder path: ")
    return library

def check_max_age(max_age):
    op = ["D", "W", "M", "Y"]
    while max_age[:-1].isnumeric() == False or max_age[-1].isalpha() == False or max_age[-1].upper() not in op:
        max_age = input("Enter a valid maximum age: ")
    return [int(max_age[:-1]), max_age[-1].upper()]

def date_age(list_age):
    if list_age[1] == "D":
        return datetime.now() - relativedelta(days=list_age[0])
    if list_age[1] == "W":
        return datetime.now() - relativedelta(weeks=list_age[0])
    if list_age[1] == "M":
        return datetime.now() - relativedelta(months=list_age[0])
    if list_age[1] == "Y":
        return datetime.now() - relativedelta(years=list_age[0])

# מקבל כתובת ובודק שהיא קיימת ותקינה
library = check_library(input('enter library path: '))
# מקבל גיל ובודק שהוא בפורמט ותקין
max_age = check_max_age(input('enter maximum "age" of the files: '))

# יוצר שם ייחודי לקבצים שיוצר בהמשך
namefolder = f'backup{datetime.now().strftime(f"%d%m%y_{max_age[0]}{max_age[1]}")}'
# יוצר קובץ טקסט ייחודי
name_log = f"{library}/actions_{namefolder}.txt"
c=1
while path.isfile(f"{name_log}"):
    name_log = f"{library}/actions_{namefolder}-{c}.txt"
    c+=1
actions = open(name_log, "a")
# יוצר תיקייה ייחודית בתיקיית הפרוייקט
create_name = f'./{namefolder}'
t = 1
while path.isdir(f"{create_name}"):
    create_name = f'./{namefolder}-{t}'
    t+=1
mkdir(f'{create_name}')

# עובר על כל הקבצים בכל התיקיות תחת אותה סיפרייה
for (root, dirs, files) in walk(f"{library}", topdown=True):
    for fileid in files:
        # פרטי הקובץ הספיציפי - כתובת וגיל
        file = fr"{root}\{fileid}"
        age_file = datetime.fromtimestamp(path.getmtime(file))
        # בודק את גיל הקובץ לעומת גיל המחיקה
        if date_age(max_age) >= age_file:
            actions.write(f"Last edit date of the file {root}\\{fileid} is {age_file}. The file has been deleted.\n")
            # בודק האם יש כבר קובץ בשם הזה ואם כן מוסיף לו מספר
            name_new = f'{create_name}/{fileid}'
            i=1
            while path.isfile(f"{name_new}"):
                name_new = f'{create_name}/{i}_{fileid}'
                i+=1
            rename(file, f'{name_new}')

# אם התיקייה ריקה סימן שלא מחקנו כלום ומוחק את התיקייה
if len(listdir(f"{create_name}")) == 0:
    rmtree(f'{create_name}')
    actions.write("No files deleted")
else:
    # אם היא מלאה יוצר קובץ זיפ ייחודי מהתיקייה ומוחק אותה
    n = 1
    name_zip = f'{library}/{namefolder}.zip'
    while path.isfile(f'{name_zip}'):
        name_zip = f'{library}/{namefolder}-{n}'
    make_archive(f"{name_zip}", "zip", f"{create_name}")
    rmtree(f'{create_name}')

actions.close()