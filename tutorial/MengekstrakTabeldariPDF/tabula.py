#readme: http://python.openthinklabs.com/2018/05/mengekstrak-tabel-dari-pdf.html
import PyPDF2
from tabula import convert_into

PDFFilename = "pdf/PKM-2018-5-Bidang-Pendanaan-Surat-Lampiran.pdf"
pfr = PyPDF2.PdfFileReader(open(PDFFilename, "rb"))

from_page = 2
to_page   = 10

writer = PyPDF2.PdfFileWriter()
while (from_page < to_page):
    pg = pfr.getPage(from_page)
    from_page = from_page+1
    writer.addPage(pg)

NewPDFFilename = "pdf/TblSkemaPenugasanPKM2018.pdf"
with open(NewPDFFilename,"wb") as outputStream:
  writer.write(outputStream)

NewCSVFilename = "csv/TblSkemaPenugasanPKM2018.csv"
convert_into(NewPDFFilename, NewCSVFilename, output_format="csv", pages="all")

#judul-judul PKM
from_page = 10
to_page   = 209

writer = PyPDF2.PdfFileWriter()
while (from_page < to_page):
    pg = pfr.getPage(from_page)
    from_page = from_page+1
    writer.addPage(pg)

NewPDFFilename = "pdf/TblPendanaanPKM2018.pdf"
with open(NewPDFFilename,"wb") as outputStream:
  writer.write(outputStream)

NewCSVFilename = "csv/TblPendanaanPKM2018.csv"
convert_into(NewPDFFilename, NewCSVFilename, output_format="csv", pages="all")
