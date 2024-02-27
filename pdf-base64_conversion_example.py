# The puprose of this code is to decode a base64 bytes, convert it to a pdf, and store it as a pypdf reader object
# so it can be used for further code. We will validate this works by using the reader object to write a new pdf
# file to disk

import pypdf as pdf
import base64
from io import BytesIO

input_pdf = "C:\\Users\\rokso\\Documents\\Example.pdf"
output_pdf = "C:\\Users\\rokso\\Documents\\Base64_2.pdf"

with open(input_pdf, 'rb') as file:

    #encode a pdf file for testing the decode process
    encFile = base64.b64encode(file.read())
    #If you are so inclined to see the encoding, so be it
    #print(encFile)

    #-----BEGIN DECODE CODE------
    #decode the encoded file
    decFile = base64.b64decode(encFile)

    #OPTIONAL: You can use this code to directly write the base64 decoded pdf file to a file
    #file_result = open(output_pdf, 'wb') 
    #file_result.write(decFile)

    

    #THE CODE: Write the decoded b64 bytes to the pypdf reader. Convert the decoded bytes to a file-like object
    file_object = BytesIO(decFile)
    file_object.seek(0)
    #Pass the file-like object into the pypdf reader
    reader = pdf.PdfReader(file_object)
    ##COMPLETE: You can use reader object to modify the PDF via code


    #FOR VALIDATION: using the reader(with the pdf file) write a new pdf to disk
    writer = pdf.PdfWriter()
    for pg in reader.pages:
        writer.add_page(pg)

    writer.write(output_pdf)
    #You should have the same pdf file
