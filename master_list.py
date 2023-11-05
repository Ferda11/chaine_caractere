print("**exo1 liste element divisible par2")
n=100
liste=[]
for i in range(0,n):
    if i%2==0:
        liste.append(i)
print("la liste de elements divisible par2 de 0-100 est:",liste)
print()

print("**Exo2 convertit lis int an list str")
list_int=[1,2,3,5,10,22]
list_str=[str(i)for i in list_int]
print("La liste convertit est:",list_str)
print()

print("**Exo3 conversion list_chaine lower en upper")
list_minuscule=["papa","maman","frere","soeur"]
print("La liste en minuscule",list_minuscule)
list_majuscule=[i.upper()for i in list_minuscule]
print("La liste convertit en majuscule est:",list_majuscule)
print()

print("**Exo 4 creation d'une nouvelle liste avec les elements dont les inex sont divisible par3")
liste_indexe=[19,23,45,42,7,8,9,0,10,70]
print("la liste originale:",liste_indexe)
liste_indexe_divisible3=[]
for index,el in enumerate(liste_indexe):
    if index%3==0:
        liste_indexe_divisible3.append(el)
print("La nouvelle liste avec les elements dont les index sont divisible par 3 est:",liste_indexe_divisible3)
print()

print("**Exo5 creer une nouvelle liste ")
list_complete=[1,2,3,4,5,6,7,8,9]
liste_trois=[]
for i in range(0,len(list_complete),3):
    tipl=tuple(list_complete[i:i+3])
    liste_trois.append(tipl)
print("La liste avec les 3 elements dans un tuple est:",liste_trois)
    
