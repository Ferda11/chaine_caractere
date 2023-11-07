import random
import string

def inverse(mo):
    print("**exo1 retounen yon mo invese")
    mo_inverse=mo[::-1]
    return mo_inverse

def code_aleyatwa(n):
    print("exo2 jenere yon kod ak n alfa")
    kod_jenere=string.ascii_lowercase
    kod = ''.join(random.choice(kod_jenere) for _ in range(n))
    return kod

def kod_aleyatwa_sanrepitisyon(n):
    print("exo3 jenere yon kod ak n alfa san repetisyon")
    
    kod_jenere2=string.ascii_lowercase
    code=random.sample(kod_jenere2,n)
    code=''.join(code)
    return code
def kod_aleyatwa_alfanimerik(n):
    print("exo4 jenere yon kod ak n alfanimerique san repetisyon")
    
    kod_jenere2=string.ascii_lowercase+string.digits
    code=random.sample(kod_jenere2,n)
    code=''.join(code)
    return code

def slug(lis):
    print("**Exo5")
    alfa=string.ascii_lowercase+string.digits+"-"
    slug=""
    for i in lis:
        t=True
        for n in i:
            if not n in alfa:
                t=False
                break
        if t:
            slug+=i
    return slug

def separate(mo6):
    print("**exo6 separe chak let nan yon mo ak yon vigil")
    mo_separe=','.join(mo6)
    return mo_separe

def crypter_mot(mot):
    print("***ex07")
    alfabe = string.ascii_lowercase
    mo_kripte = []

    for lettre in mot:
        if lettre.isalpha(): 
            endeks = alfabe.index(lettre.lower()) + 1  
            mo_kripte.append(str(endeks))
        else:
            mo_kripte.append(lettre)  

    mo_kripte = '-'.join(mo_kripte)  
    return mo_kripte





mo1=inverse("CArine")
print(mo1)
print()
kod1=code_aleyatwa(5)
print(kod1)
print()
kod2=kod_aleyatwa_sanrepitisyon(5)
print(kod2)
print()
kod3=kod_aleyatwa_alfanimerik(5)
print(kod3)
print()
lis_chenn=["Ferda-Carine",'Fleurimond2001','ferdacarinef','carine001']
slug1=slug(lis_chenn)
print(slug1)
print()
mo_separe1=separate("Ecole")
print(mo_separe1)
print()
mot="ferda"
kripte=crypter_mot(mot)
print(kripte)



        
        
    