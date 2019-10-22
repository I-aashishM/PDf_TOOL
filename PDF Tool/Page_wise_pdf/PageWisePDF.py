from pdfrw import PdfReader, PdfWriter
pages = PdfReader('Official Ielts Practice Materials 2.pdf').pages
parts = [(15,28)]
for part in parts:
    outdata = PdfWriter(f'pages_{part[0]}_{part[1]}.pdf')
    for pagenum in range(*part):
        outdata.addpage(pages[pagenum-1])
    outdata.write()