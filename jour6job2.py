hauteur=int(input("entrer la hauteur de votre triangle:"))
for i in range(hauteur):
    if i==hauteur-1:
        print("/","_"*((hauteur-2)*2),"\\")
    else:
        b=int(hauteur-i-1)
        c=" "*b+"/"+" "*i*2+"\\"
        print(c)
    