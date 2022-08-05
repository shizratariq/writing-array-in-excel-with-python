import pandas as pd
import pyexcel as pe
rows, cols = (5, 5)
arr=[]
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(i+j)
    arr.append(col)
print(arr)

pe.save_as(array=arr, dest_file_name="example.xlsx")
