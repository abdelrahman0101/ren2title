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
    try:
        fileInfo = PdfReader(fullName).Info
        if not fileInfo:
            print("No metadata for file: '", fileName) 
            return
        # Extract pdf title or subject from pdf file
        newName = fileInfo.Title or fileInfo.Subject
        if (not newName):
            print("No title or subject found in file: '", fileName) 
            return
        # Remove surrounding brackets that some pdf titles have
        newName = newName.strip('()')
        # Rename for Windows (remove special characters)
        newName = re.sub('[^0-9a-zA-Z\-_. ()]+', ' ', newName)
        if str(newName).lower() in ['', ' ', 'untitled', 'none', 'null']:
            print("Invalid title for file: '", fileName)
            return
        newName = newName + '.pdf'
        print("Renaming file: '", fileName, "' to:", newName) 
        newFullName = os.path.join(path, newName)
        os.rename(fullName, newFullName)
    except:
        print("Error handling file: ", fileName) 

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
      	
      	
      	 
