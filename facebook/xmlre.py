#specific to extracting information from word documents
import os
import zipfile
#other tools useful in extracting the information from our document
import re
#to pretty print our xml:
import xml.dom.minidom

os.listdir('.')

document = zipfile.ZipFile('my_word_file.docx')
#document will be the filetype zipfile.ZipFile

ZipFile.read(name, pwd=None)

document.namelist()

link_list = re.findall('http.*?\<',xml_str)[1:]
link_list = [x[:-1] for x in link_list]


