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

with open(filename, 'r') as f: 
	data = f.read() 

# Passing the stored data inside 
# the beautifulsoup parser, storing 
# the returned object 
Bs_data = BeautifulSoup(data, "xml") 

# Finding all instances of tag 
b_unique = Bs_data.find_all(['w:hyperlink','w:instrText','w:t']) 

index = 0
while index < len(b_unique):

    data = b_unique[index]

    if data.name == 'instrText':
        index = index + 1
        #if data.string.find("padremariopantaleo") < 0:
        data = b_unique[index]

        if data.name == 't' and data.string.find('Fan destacado') >= 0:
            index = index + 1
            data = b_unique[index]

        if data.name == 'hyperlink':
            tags = data.find_all('w:t')
            if len(tags) > 0:
                #print("Encontre un nuevo comentario!!!!!!!!!!!!!!!!!!!!!!!!")
                #print("-------------------------------")
                nombre = ''
                for tag in tags:
                    nombre += tag.string
                    index = index + 1

            comentario = ''
            index = index + 1
            data = b_unique[index]
            while data.name == 't' and data.string.find('Me gusta', 0, 9) < 0:
                comentario = comentario + data.string
                index = index + 1
                data = b_unique[index]

            print("C ; " + nombre.replace(';', ',') + " ; " + comentario.replace(';', ','))

    elif data.name == 't':
        if data.string.find("Obra del Padre Mario", 0, 22) >= 0:
            #print("Encontre un nuevo POSTEO!!!!!!!!!!!!!!!!!!!!!!!!")
            #print("-------------------------------")
            index = index + 3
            data = b_unique[index]
            posteo = ''
            while data.name == 't' and data.string.find('comentario', 0, 14) < 0 and data.string.find('Me gusta', 0, 14) < 0:
                posteo = posteo + data.string
                index = index + 1
                data = b_unique[index]
            print("P ; Obra del Padre Mario ; " + posteo.replace(';',','))

        index = index + 1

    else:
        index = index + 1

