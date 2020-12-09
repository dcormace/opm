from bs4 import BeautifulSoup 
import sys


# Reading the data inside the xml 
# file to a variable under the name 
# data
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    print("Error: no file name")
    exit()

#with open('wordfile/word/document.xml', 'r') as f: 
with open(filename, 'r') as f: 
	data = f.read() 

# Passing the stored data inside 
# the beautifulsoup parser, storing 
# the returned object 
Bs_data = BeautifulSoup(data, "xml") 

# Finding all instances of tag 
# `unique` 
b_unique = Bs_data.find_all('w:t') 

text = ""
text_ant = "Final del formulario"
for data in b_unique:
    #text = data.contents[0]
    text = data.string
    if text.find("Obra del Padre Mario", 0, 22) >= 0:
        if text_ant.find("Final del formulario") >= 0:
            print("===========================================")
            print("Nuevo Posteo")
            print("===========================================")
    print(text)
    text_ant = text


# Using find() to extract attributes 
# of the first instance of the tag 
#b_name = Bs_data.find('child', {'name':'Frank'}) 

#print(b_name) 

# Extracting the data stored in a 
# specific attribute of the 
# `child` tag 
#value = b_name.get('test') 

#print(value) 

