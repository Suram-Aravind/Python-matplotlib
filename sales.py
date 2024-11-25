import pandas as pd
import matplotlib.pyplot as plt
# import openpyxl 
data=pd.read_excel(r"/home/systemno62/Documents/python/TSM sales review 1.xlsx",sheet_name="Market wise KH-24 sales",skiprows=2) 

location=data["Market  (PO Name)"]
tot_potential=data["Potential Kh 22 ‘000 PKTs"]
sales=data["Sales KH-22 ‘000PKTs"]
plt.pie(sales,labels=location,autopct='%1.1f%%')
plt.show()
print(data.head(6))