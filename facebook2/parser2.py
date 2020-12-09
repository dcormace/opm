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
b_unique = Bs_data.find_all(['w:hyperlink','w:r']) 

text = ""
text_ant = "Final del formulario"
for index, data in enumerate(b_unique):

    if data.name == 'hyperlink':
        #print("es un r........................")
        tag = data.find('w:t')
        if tag is not None:
            if tag.string.find("Obra del Padre Mario", 0, 22) >= 0:
                #print("que tiene un t.....................................")
                print("Encontre un nuevo POSTEO!!!!!!!!!!!!!!!!!!!!!!!!")
                print(tag.string)
                print("-------------------------------")

    if data.name == 'r':
        #print("es un r........................")
        tag = data.find('w:instrText')
        if tag is not None:
            #print("que tiene instrText..........................")
            data_next = b_unique[index+3]
            if data_next.name == 'hyperlink':
                #print("el siguiente es un hyperlink..............................")
                tag_next = data_next.find('w:t')
                if tag_next is not None:
                    #print("que tiene un t.....................................")
                    print("Encontre un nuevo comentario!!!!!!!!!!!!!!!!!!!!!!!!")
                    print(tag_next.string)
                    print("-------------------------------")

    if data.name == 'r':
        #print("es un r........................")
        tag = data.find('w:instrText')
        if tag is not None:
            #print("que tiene instrText..........................")
            data_next = b_unique[index+2]
            if data_next.name == 'r':
                #print("el siguiente es un hyperlink..............................")
                tag_next = data_next.find('w:t')
                if tag_next is not None:
                    if tag_next.string.find("Obra del Padre Mario", 0, 22) >= 0:
                        #print("que tiene un t.....................................")
                        print("Encontre un nuevo xxxxxPOSTEO!!!!!!!!!!!!!!!!!!!!!!!!")
                        print(tag_next.string)
                        print("-------------------------------")


    if data.name == 'r':
        textos = data.find_all('w:t')
        for texto in textos:
            print(texto.string)


# Using find() to extract attributes 
# of the first instance of the tag 
#b_name = Bs_data.find('child', {'name':'Frank'}) 

#print(b_name) 

# Extracting the data stored in a 
# specific attribute of the 
# `child` tag 
#value = b_name.get('test') 

#print(value) 

