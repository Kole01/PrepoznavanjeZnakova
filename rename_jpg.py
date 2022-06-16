from operator import index
import os 
import cv2 
from glob import glob 

cwd = os.getcwd()
input_dir = os.path.join(cwd, "*.jpg")    
jpgs = glob(input_dir)   

counter = 0
for jpg in jpgs:
    
    name, ext = os.path.splitext(os.path.join("", jpg))
    os.rename(name+ext,str(counter)+ext)
    counter = counter + 1  