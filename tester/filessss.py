import os
from time import *
from datetime import *

for namefile in os.listdir('C:/Users/yusts/Desktop/text_program_sony'):
    file = os.stat(f"C:/Users/yusts/Desktop/text_program_sony/{namefile}")
    agefile = file.st_mtime
    print(agefile)
