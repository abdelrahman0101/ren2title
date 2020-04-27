# Ren2Title
A Python script to rename PDF files to titles or subjects stored in files metadata. Useful for research papers downloaded from online repositories.

This script is based on code from this StackOverflow thread:
https://stackoverflow.com/questions/44598758/how-to-extract-the-title-of-a-pdf-document-from-within-a-script-for-renaming

Modifications include:
* Using the subject field when title is not available.
* Removing any special characters from filename, so the resulting filenames are valid for Linux/Unix and Windows.
* Recursively renaming files in subdirectories.
