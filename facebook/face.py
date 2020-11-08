

def process_post(post):
    print("Processing Post.................")
    text_to_ignore = ["Me gustaComentarCompartir","Ver comentarios anteriores","Más antiguos", "Principio del formulario", "Final del formulario", "•", "", "◦"]

    text_init_comments = "Comentarios"
    flag_init_comments = False

    for i, line in enumerate(post):
        #print(i, " - ", line)

        flag_ignore = False
        for text in text_to_ignore:
            if text in line:
                flag_ignore = True

        if not flag_ignore:
            if text_init_comments in line:
                flag_init_comments = True
        
            if i == 1:
                print("fecha: ", line)
            elif flag_init_comments:
                print("comments section : ", line)
            else:
                print(line)

    print("-"*50)



filename = "OPM_descarga FB con formato 20 oct (2).txt"
with open(filename) as f:
    content = f.readlines()

    flag_new_post = False
    post = list()
    for line in content:
        line = line.rstrip('\n')
        if "Obra del Padre Mario Pantaleo" in line:
            flag_new_post = True
            if len(post):
                process_post(post)
            post.clear()

        post.append(line)
        if flag_new_post:
            flag_new_post = False

    process_post(post)


