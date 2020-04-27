import os
import sys
import re
from pdfrw import PdfReader

if len(sys.argv) < 2:
    path = '.'
else:
    path = str(sys.argv[1])

def renameFileToPDFTitle(path, fileName):
    fullName = os.path.join(path, fileName)
    # Extract pdf title or subject from pdf file
    newName = PdfReader(fullName).Info.Title or PdfReader(fullName).Info.Subject
    if not newName:
        print("No title or subject found in file: '", fileName) 
        return
    # Remove surrounding brackets that some pdf titles have
    newName = newName.strip('()') + '.pdf'
    # Rename for Windows (remove special characters)
    newName = re.sub('[^0-9a-zA-Z\-_. ]+', ' ', newName)
    if len(newName) < 5:
        print("Invalid title for file: '", fileName)
        return
    print("Renaming file: '", fileName, "' to:", newName) 
    newFullName = os.path.join(path, newName)
    os.rename(fullName, newFullName)


def renPdf(directory):
    print("Renaming PDF files in: ", path)
    for fileName in os.listdir(directory):
        # Rename only pdf files
        fullName = os.path.join(directory, fileName)
        if os.path.isdir(fullName):
            # recursive call for subdirectories
            print("Entering subdirectory: ", fullName)
            renPdf(fullName)
        if (not os.path.isfile(fullName) or fileName[-4:] != '.pdf'):
            continue
        renameFileToPDFTitle(directory, fileName)

renPdf(path)
      	
      	
      	 
