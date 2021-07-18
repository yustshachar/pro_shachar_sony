from os import listdir, path, rename, mkdir, rmdir
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


library = check_library(input('enter library path: '))
max_age = check_max_age(input('enter maximum "age" of the files: '))

namefolder = f'backup{datetime.now().strftime(f"%d%m%y_{max_age[0]}{max_age[1]}")}'
actions = open(f"{library}/actions_{namefolder}.txt", "a")
mkdir(f'{library}/{namefolder}')

for namefile in listdir(library):
    file = f"{library}/{namefile}"
    age_file = datetime.fromtimestamp(path.getmtime(file))
    if date_age(max_age) >= age_file:
        actions.write(f"Last edit date of the file {namefile} is {age_file}. The file has been deleted.\n")
        rename(file, f'{library}/{namefolder}/{namefile}')

if path.isdir(f"{library}/{namefolder}"):
    make_archive(f"{library}/{namefolder}", "zip", f'{library}/{namefolder}')
    rmtree(f'{library}/{namefolder}')

try:
    rmdir(f'{library}/{namefolder}')
except:
    pass


actions.close()
