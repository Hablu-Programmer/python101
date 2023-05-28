from PyPDF2 import PdfMerger

AllPDF = ["1.pdf", "2.pdf"]

OurMerger =  PdfMerger()

for NewPDF in AllPDF:
    OurMerger.append(NewPDF)

OurMerger.write("Hablu.pdf")
OurMerger.close()