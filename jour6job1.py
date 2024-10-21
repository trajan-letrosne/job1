def draw_rectangle(width,height):
    width=int(input("entrez l alargeur de votre rectangle:"))
    height=int(input("entrez la longeur de votre rectangle:"))

    for i in range(height):
        if i==0 or i==height-1:
           print("|","-"*(width-2),"|")
        else:
            print("|"," "*(width-2),"|")
print(draw_rectangle())

