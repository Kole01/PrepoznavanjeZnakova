import os
from re import I
from certifi import where 
import cv2 
from glob import glob 
import pandas as pd
import csv



cwd = os.getcwd()
input_dir = os.path.join(cwd, "*.jpg")    
jpgs = glob(input_dir)  

df=pd.read_csv("newcsv.csv")
df_names = df['name']
del df['name']
rows, columns = df.shape

df_class = df['class']
df_x = df['x_center_image']
df_y = df['y_center_image']
df_width = df['width']
df_height = df['height']

for index, row in df.iterrows():
        temp_name = int(df_names.loc[index])
        f = open(str(temp_name)+'.txt','a')
        f.write(str(df_class.loc[index])+' '+str(df_x.loc[index])+' '+str(df_y.loc[index])+' '+str(df_width.loc[index])+' '+str(df_height.loc[index])+'\n')
        f.close
        

