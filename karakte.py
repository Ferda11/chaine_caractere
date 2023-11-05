chaine=input("Antre yon chaine karakte:")
if  not chaine==" ":
    print(chaine.lower())
    
    print("*** exo kote wap antre yn chaine ak espas kap retounen yon lis**")
chaine_caractere=input("Antre yon chaine:")
eleman=chaine_caractere.split()
print(eleman)
print()

print("***Enonse 3 li la pou mete chak premye let mo yo en majiskil***")
fraz=input("Antre yon fraz :")
fraz1=fraz.title()
print(fraz1)

print("***nan yn chen wap antre nap afiche yn fraz ak premye let chak mo ou te antre yo**")
chaine_premye=input("Antre yn chen karakte :")
chaine1=chaine_premye.split()
mots=[mot[0] for mot in chaine1 ]
fraz_premyeLet=''.join(mots)
print(fraz_premyeLet)
print()
print(" exo5 pou ranplase tout a pa @")
phrase="ayiti ayibobo ayiti ka libere"
print(phrase)
phrase_nouv=phrase.replace("a","@")
print(phrase_nouv)
print()
print("**exo6 invese yon chenn karakte**")

phrase6=input("antre yn fraz :")
print(phrase6)
phrase_inverse=phrase6[::-1]
print(phrase_inverse)
print() 
print("**exo7 afiche index premye karakte (a) ki nan yon chenn**")
phrase7=input("Antre yon fraz:")
index=phrase7.find("a")
if index>=0:
    print("premye a ki nan fraz la jwenn li nan index",index)
else:
    print("pa gen a nan fraz la")

print()
print("** exo8 afiche total tout index karakte(a ou A) ki nan yon fraz")

fraz8=input("Antre yn fraz:")
somme=0

for index, caractere in enumerate(fraz8):
    if caractere == "a" or caractere == "A":
        somme+=index

print(f"total tout index karakte (a )ak (A )ki nan fraz sa se : {somme}")
print()

print("** exo9 afiche lis tout index karakte(a) ki nan yon fraz")

fraz9=input("Antre yn fraz:")
positions = []

for index, caractere in enumerate(fraz9):
    if caractere == "a" :
        positions.append(index)

if positions:
    print(f"total tout index karakte (a )ki nan fraz sa se : {positions}")
else:
    print("pa gen (a)  nan fraz la.")

print()
print("** exo10  retire tout espase ki nan yon chen")
chaine_espas=input("Antre yon chaine caratere:")
chaine_sansEspas=chaine_espas.replace(" ","")
chaine_colle=''.join(chaine_sansEspas)
print(chaine_colle)


    
