from docx import Document
from docx.shared import Inches
from docx.shared import RGBColor
import csv

# Create a new Word document
document = Document()

# Add a table to the document with fixed columns and rows
table = document.add_table(rows=27, cols=3)
table.autofit = False

# Change the border color of the table to black
table.style = 'Table Grid'
table.style.border_color = RGBColor(0, 0, 0)

# Set the width of each column
table.columns[0].width = Inches(2)
table.columns[1].width = Inches(2)
table.columns[2].width = Inches(4)

# Set the heading row of the table
heading_row = table.rows[0].cells
heading_row[0].text = 'Title'
heading_row[1].text = 'Price'
heading_row[2].text = 'Location'

# Open the CSV file and read the data
with open('output.csv', newline='',encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row

    # Add each row of data to the table
    for row in reader:
        cells = table.add_row().cells
        cells[0].text = row[0]
        cells[1].text = row[1]
        cells[2].text = row[2]

# Save the Word document
document.save('output.docx')
