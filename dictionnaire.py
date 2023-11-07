print("**Exo1 rekipere vale nan yon diksyone gras ak kle yo")
dictio={'nom':'Fleurimond','prenom':'Ferda-Carine','age':'21'}
liste=[]
for kle in dictio.keys():
    vale=dictio.get(kle)
    if vale is not None:
        liste.append(vale)
print("Lis vale yo se:",liste)
print()
print("**Exo2 verifye si yon vale gen akolad devan ak deye")
chenn=input("Antre yon vale:")
if chenn.startswith("{") or chenn.endswith("}"):
    print("vale sa gen akolad")
else:
    print("vale sa pa gen akolad")
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
print()
print("**Exo6 ajoute underscore devan tout vale ki se chenn yo nan yon diksyone")
diksyone={'Nom':"Fleurimond",'Prenom':"Midjesly",'age':19,}
diksyone2={}
for cle1,val in diksyone.items():
    if isinstance(val,str):
        val=" _"+val
    diksyone2[cle1]=val
print(diksyone2)
print()
print("**Exo7kreye yon nouvo diksyone ak digit yo")
diksyone3={'a':"12",'b':"abc",'c':"31"}
diksyone4={}
for cle2,val2 in diksyone3.items():
    if val2.isdigit():
        diksyone4[cle2]=val2
print(diksyone4)
print()
print("**Exo8 mete yon diksyone sou fom lis kote chak eleman yo ap yon tuple")
lis_dict=[]
for cle3,val3 in diksyone3.items():
   tip=(cle3,val3)
   lis_dict.append(tip)
print(lis_dict)
print()
print("** pakouri yon lis tipl pou metel sou fom diksyone")
diksyone5={}
for el in lis_dict:
    cle4,val4=el
    diksyone5[cle4]=val4
print(diksyone5)
    