from fpdf import FPDF
import pandas as pd

pdf =  FPDF(orientation= "P", unit="mm", format= "A4")
pdf.set_auto_page_break(auto =False, margin =0 )

csv_read = pd.read_csv("topics.csv")
for index, row in csv_read.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times",style="B", size= 24)
    pdf.set_text_color(0,0,0)
    pdf.cell(w= 0, h=12, txt= row["Topic"], align="L",ln=1)
    pdf.line(0, 21, 210, 21)
    pdf.ln(266)
    pdf.set_font(family="Times",style="I", size= 8)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R")




    for i in range(row["Pages"]-1):
        pdf.add_page()
        pdf.ln(278)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R")



pdf.output("output.pdf")