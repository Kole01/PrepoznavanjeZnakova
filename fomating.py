import pandas as pd
  

dataframe1 = pd.read_csv("gt.txt", delimiter=';')
  
dataframe1.to_csv('gt.csv', index = None)