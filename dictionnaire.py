print("**Exo1 rekipere vale nan yon diksyone gras ak kle yo")
dictio={'nom':'Fleurimond','prenom':'Ferda-Carine','age':'21'}
liste=[]
for kle in dictio.keys():
    vale=dictio.get(kle)
    if vale is not None:
        liste.append(vale)
print("Lis vale yo se:",liste)
print()
print("**Exo3 pakouri yon diksyone epi afiche tout kle yo")
for i in dictio.keys():
    print(i)
print()
print("** exo4 pakouri yon diksyone epi afiche tout vale yo")
for i in dictio.values():
    print(i)
print()
print("**exo5 pakouri yon disksyone pou kreye yon kopi sou li")
dictio1={}
for cle,valeur in dictio.items():
    dictio1[cle]=valeur  
print("kopi diksyone a:",dictio1)












