
from PyPDF2 import PdfFileMerger

pdfs = ['final_marksheet_upto_7thSem.pdf', '8th_Semester.pdf']

merger = PdfFileMerger(strict = False)

for pdf in pdfs:
    merger.append(pdf)

merger.write("final_marksheet_upto_8thSem.pdf")
merger.close()