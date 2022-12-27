from fpdf import FPDF
import pandas as pd

pdf=FPDF(orientation='P',unit='mm',format='A4')
pdf.set_auto_page_break(auto=False,margin=0)

df=pd.read_csv('topics.csv')


for index,row in df.iterrows():
        pdf.add_page()
        #Set Header
        pdf.set_font(family="Times",style='B',size=12)
        pdf.set_text_color(0,54,56)
        pdf.cell(w=0,h=12,txt=row['Topic'],align='L',ln=1)
        pdf.line(10,20,200,20)

        # Set the footer
        pdf.ln(260)
        pdf.set_font(family='Times',style='I',size=10)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0,h=10,txt=f"{row['Topic']}",align="R")


        for x in range(row['Pages']-1):
            pdf.add_page()
            pdf.set_text_color(0,54,56)
            pdf.cell(w=0, h=12, txt="", align='L', ln=1)
            #Set the footer
            pdf.ln(260)
            pdf.set_font(family='Times', style='I', size=10)
            pdf.set_text_color(180,180,180)
            pdf.cell(w=0, h=10, txt=f"{row['Topic']}", align="R")

pdf.output('first.pdf')


