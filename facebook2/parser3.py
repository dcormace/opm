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
b_unique = Bs_data.find_all(['w:instrText','w:t']) 

index = 0
while index < len(b_unique):

    data = b_unique[index]

    if data.name == 't':
        if data.string.find("Obra del Padre Mario", 0, 22) >= 0:
            print("Encontre un nuevo POSTEO!!!!!!!!!!!!!!!!!!!!!!!!")
            print("-------------------------------")


    if data.name == 'instrText':
        if data.string.find("padremariopantaleo") < 0:
            data_next = b_unique[index+1]
            if data_next.name == 't':
                print("Encontre un nuevo comentario!!!!!!!!!!!!!!!!!!!!!!!!")
                print("-------------------------------")
                print(data_next.string)
        index = index + 1

    if data.name == 't':
        print(data.string)

    index = index + 1

