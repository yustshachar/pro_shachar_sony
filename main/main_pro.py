from os import *
from time import *
from dateutil.relativedelta import relativedelta
from datetime import *
import shutil
from main.functions import functions

def check_max_age(max_age):
    op = ["D", "W", "M", "Y"]
    while max_age[:-1].isnumeric() == False or max_age[-1].isalpha() == False or max_age[-1].upper() not in op:
        max_age = input("Enter a valid value: ")
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


library = input('enter library path: ')
max_age = check_max_age(input('maximum "age" of the files: '))

for namefile in listdir(library):
    file = f"{library}/{namefile}"
    age_file = datetime.fromtimestamp(path.getmtime(file))
    print(namefile)
    if date_age(max_age) >= age_file:
        print("del!!")
        rename(file, f'C:/Users/yusts/Desktop/new_test/{namefile}')
    print()
