from tokenize import Triple
from cv2 import merge
import pandas as pd
import os 
import cv2 
from glob import glob
import csv

data = pd.read_csv('gt.csv') 

file_names = data['name']
file_class = data['class']
file_topRow = data['topRow']
file_bottomRow = data['bottomRow']
file_leftColumn = data['leftCol']
file_rightColumn = data['rightCol']

rows,columns = data.shape
width    = (file_rightColumn - file_leftColumn)/1360
height   = (file_bottomRow - file_topRow)/800
x_center_image = file_leftColumn/1360 + width/2
y_center_image = file_topRow/800 + height/2

df_all = pd.concat([file_names,file_class,x_center_image,y_center_image,width,height], axis=1)
df_all.columns = ['name', 'class', 'x_center_image', 'y_center_image','width','height']
print(df_all)

df_all.to_csv('newcsv.csv',index=False)

        