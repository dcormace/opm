from docx import Document
from docx.opc.constants import RELATIONSHIP_TYPE as RT

print(" This program changes the hyperlinks detected in a word .docx file \n")


document = Document("my_word_file.docx")

rels = document.part.rels

for rel in rels:
   if rels[rel].reltype == RT.HYPERLINK:
      print("\n Origianl link id -", rel, "with detected URL: ", rels[rel]._target)
      #new_url=input(" Pls input new URL: ")
      #rels[rel]._target=new_url

out_file="my_word_file" + "-out.docx"

document.save(out_file)

print("\n File saved to: ", out_file)
