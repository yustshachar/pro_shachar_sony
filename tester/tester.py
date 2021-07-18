from os import *
from os import listdir, path, rename, mkdir, walk
from dateutil.relativedelta import relativedelta
from datetime import datetime
from shutil import make_archive, rmtree

# for namefile in walk(r"C:\Users\yusts\Desktop\text_program_sony", topdown=True):
#     print(namefile)

# for (root, dirs, files) in walk(r"C:\Users\yusts\Desktop\text_program_sony", topdown=True):
#     print(root)
#     print(dirs)
#     print(files)
#     print('---------------')
#     for file in files:
#         print(fr"{root}\{file}")
#     print('==============================')

# library = r"C:\Users\yusts\Desktop\text_program_sony"
# namefolder = f'backup{datetime.now().strftime(f"%d%m%y_2W")}'
# # C:\Users\yusts\Desktop\text_program_sony\backup180721_2W.zip
# name_zip = f'{library}/{namefolder}'
# print(path.isfile(f'{name_zip}'))


# for namefile in listdir(library):
#     print(namefile)

