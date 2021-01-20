from bs4 import BeautifulSoup 
import sys


# Reading the data inside the xml 
# file to a variable under the name 
# data
if len(sys.argv) > 1:
    filename = sys.argv[1]
    year = sys.argv[2]
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

line_number = 1
index = 0
while index < len(b_unique):

    data = b_unique[index]

    if data.name == 'instrText':
        index = index + 1
        #if data.string.find("padremariopantaleo") < 0:
        data = b_unique[index]

        fandestacado = ' '
        if data.name == 't' and data.string.find('Fan destacado') >= 0:
            fandestacado = data.string
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
            if index >= len(b_unique):
                exit()
            data = b_unique[index]
            while data.name == 't' and data.string.find('Me gusta', 0, 9) < 0:
                comentario = comentario + data.string
                index = index + 1
                if index >= len(b_unique):
                    exit()
                data = b_unique[index]
            
            comentario = comentario.replace(';', ',')
            comentario = comentario.replace('"', '')
            print(str(year) + " ; " + str(line_number) +  " ; C ; " + nombre.replace(';', ',') + " ; " + fandestacado + " ; " + comentario)
            line_number += 1

    elif data.name == 't':
        if data.string.find("bra del Padre Mario", 0, 22) >= 0:
            #print("Encontre un nuevo POSTEO!!!!!!!!!!!!!!!!!!!!!!!!")
            #print("-------------------------------")
            index = index + 3
            data = b_unique[index]
            while data.name != 't':
                index = index + 1
                if index >= len(b_unique):
                    exit()
                data = b_unique[index]

            posteo = ''
            fecha = ''
            while data.string.find('comentario', 0, 14) < 0 and data.string.find('Me gusta', 0, 14) < 0:
                if data.name == 't':
                    if data.string.find("Fecha", 0, 8) >= 0:
                        fecha = data.string
                        while data.string.find(")") < 0:
                            index += 1
                            data = b_unique[index]
                            fecha += data.string
                        for tmp in ["(","Fecha",":",")"]:
                            fecha = fecha.replace(tmp,"")
                        posteo = ''
                    else:
                        posteo = posteo + data.string

                index = index + 1
                if index == len(b_unique):
                    exit()

                #print(index, len(b_unique))
                data = b_unique[index]
                while data.name != 't':
                    index = index + 1
                    if index >= len(b_unique):
                        exit()
                    data = b_unique[index]
            
            comentarios = ""
            if data.string.find('comentario', 0, 14) > 0:
                comentarios = data.string
                index += 1
                if index >= len(b_unique):
                    exit()
                data = b_unique[index]

            compartido = ""
            if data.string.find("compartid", 0, 25) > 0:
                compartido = data.string
                index += 1
                if index >= len(b_unique):
                    exit()
                data = b_unique[index]

            posteo = posteo.replace(';',',')

            if posteo.find("Responder", 0, 15) >= 0:
                posteo = posteo.replace("Responder","")
                print(str(year) + " ; " + str(line_number) +  " ; C ; Obra del Padre Mario ;  ; " + posteo)
            else:
                print(str(year) + " ; " + str(line_number) + " ; P ; " + fecha + " ; " + comentarios + " ; " + compartido + " ; Obra del Padre Mario ; " + posteo)
            line_number += 1


        index = index + 1

    else:
        index = index + 1

