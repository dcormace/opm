import docx

doc = docx.Document("my_word_file.docx")

all_paras = doc.paragraphs
len(all_paras)

for para in all_paras:
    print(para.text)
    print("-------")

