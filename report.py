import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
from openpyxl.drawing.image import Image

# Step 1: Load data from Excel
data = pd.read_excel(r"/home/systemno62/Documents/python/TSM sales review 1.xlsx", 
                     sheet_name="Market wise KH-24 sales", 
                     skiprows=2)

# Step 2: Extract relevant columns
location = data["Market  (PO Name)"]
sales = data["Sales KH-22 ‘000PKTs"]

# Step 3: Create the Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(sales, labels=location, autopct='%1.1f%%', startangle=140)
plt.title('Market-wise Sales Distribution')

# Step 4: Save the Pie Chart as an Image (PNG)
chart_image_path = '/home/systemno62/Documents/python/sales_pie_chart.png'
plt.savefig(chart_image_path)

# Step 5: Load the existing Excel file with openpyxl
wb = openpyxl.load_workbook(r"/home/systemno62/Documents/python/TSM sales review 1.xlsx")
ws = wb["Market wise KH-24 sales"]  # Specify the sheet where you want to insert the chart

# Step 6: Insert the Image into the Excel Sheet
img = Image(chart_image_path)
ws.add_image(img, 'E5')  # Specify the cell where the image should be inserted (E5 in this case)

# Step 7: Save the workbook with the new image inserted
wb.save(r"/home/systemno62/Documents/python/TSM sales review updated.xlsx")

# Show the pie chart (optional)
plt.show()

# Print first few rows for reference
print(data.head(6))
