#install PyPDF2 install -pip PyPDF2
from PyPDF2 import PdfFileMerger


#pdfs reffers to all the pdfs tha you want to merge. this part give the merged file name
#and initialise the merge funtion.
pdfs = ["name.pdf", "name2.pdf"] #here you choose name of the pdfs to merge,
output_name = "MergeFile.pdf"
Fusion = PdfFileMerger()

#goes to all the file in the pdfs variable and append them
for pdf in pdfs:
	fusion.append(open(pdf, 'rb'))

with open(output_name, 'wb') as outputfile:
	fusion.write(outputfile)
