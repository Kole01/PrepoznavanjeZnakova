import os 
import cv2 
from glob import glob 

cwd = os.getcwd()
input_dir = os.path.join(cwd, "*.ppm")    
ppms = glob(input_dir)   


for ppm in ppms: 
    name, ext = os.path.splitext(os.path.join("", ppm))
    cv2.imwrite(name+".jpg", cv2.imread(ppm))
    os.remove(name+'.ppm')