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
print()

print("* exo6*Supprimer les doublons d'une liste")
liste_origin=[22,10,10,34,56,56,34,12,21,12,56]
list_sansDoublon=list(set(liste_origin))
print("La liste sans doublon est:",list_sansDoublon) 
print()

print("**exo7 creation d'une liste avec des elements communs de deux listes")
liste1=[0,1,2,3,4,5,6,7,8,9,10]
liste2=[20,10,4,7,12,3,6,30,9,8,0,31,1]
print("Les deux listes , liste1:",liste1,"liste2:",liste2)

liste3=[]
for i in liste1:
    if i in liste2:
        liste3.append(i)
print("la nouvelle liste avec les elements communs:",liste3)
print()

print("**exo8 creation d'une liste avec des elements distingue de deux listes")
liste_1=[0,1,2,3,4,5,6,7,8,9,10]
liste_2=[20,10,4,7,12,3,6,30,9,8,0,31,1]
print("Les deux listes , liste1:",liste1,"liste2:",liste2)

liste_distenge1=[]
liste_distenge2=[]
for i in liste_1:
    if  not i in liste_2:
        liste_distenge1.append(i)
for j in liste_2:
    if not j in liste_1:
        liste_distenge2.append(j)
liste_distenge=liste_distenge1+liste_distenge2              
print("la nouvelle liste avec les elements distingues:",liste_distenge)
print()

print("**exo9 creation de deux listes avec les cles et les valeurs d'un dictionnaire")
dictionnaire={'Nom':"Fleurimond",'Prenom':"Ferda","sexe":"Feminin",'Age':21}
liste_cle=list(dictionnaire.keys())
liste_valeur=list(dictionnaire.values())
print("La liste contenant les cles :",liste_cle)
print()
print("La liste contenant les valeurs:",liste_valeur)
print()

print("**exo10 reunion de trois listes sans doublon")
liste10=[1,2,3,4,5,6,7,8,9]
liste11=[3,4,5,6,7,8]
liste12=[0,6,7,8,12]
liste_ensemble=list(set(liste10)| set(liste11)| set(liste12))
print("La reunion des listes sans aucun doublon:",liste_ensemble)
        
        
    

    
    
