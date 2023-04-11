import math
import random as rand

taille_de_mot = 4
N = 10000 #nombre de_mots
k = 5 #nombre fonction de hachage
TabFBa = [[0] * taille_de_mot for i in range(N)]#10000 mots tires au hasard


def remplir(tab):
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            tab[i][j] = rand.randint(97, 122)


def afficher(tab):
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            print(chr(tab[i][j]), end=' ')
        print()

def hashage_extraction(tab_):
    sum = ""
    for i in range(len(tab_)):
        #traduit en binaire, on concatene
        binaire = bin(tab_[i])[2:]
        sum = binaire[1]+binaire[2]+binaire[5]
    result = int(sum, 2) #puis on convertie en base decimale
    return result
    
        

def hashage_fct(tab_): #exemple intuitif de fonction de hachage
    sum = 0
    for i in range(len(tab_)):
        sum = sum + tab_[i]
    n = sum + len(tab_)
    n = n % 26
    return n

  


# hashage par compression
def hash_compression(tab_):
    tabBin = [0 for i in range(len(tab_))]
    for i in range(len(tab_)):
        tabBin[i] = bin(tab_[i])[2:]
        #print(bin(tab_[i])[2:])
    resultatXoR = 0
    for i in range(0, len(tab_)):
        #On met un XOR ENTRE Les lettres du mot, sous forme de code binaire
        resultatXoR = bin(resultatXoR)[2:]
        resultatXoR = int(resultatXoR, 2) ^ int(tabBin[i], 2) #Bitwise XOR	x ^ y
    return resultatXoR % 26


# hashage par division
def hash_devision(tab_):
    sum = ""
    for i in range(len(tab_)):
        #traduit en binaire, on concatene
        binaire = bin(tab_[i])[2:]
        sum = sum + binaire
    varDiv = int(sum, 2) #puis on convertie en base decimale
    result = varDiv % 26 #puis on calcule le modulo h(e) = e mod N, telque N = 26 dans ce cas
    return result


# hashage par multiplication
def hash_multip(tab):
    teta = 0.6
    mult = 0
    sum = ""
    for i in range(len(tab)):
        # mult = tab[i]*teta
        binaire = bin(tab[i])[2:]
        sum = sum + binaire
    mult = int(sum, 2)
    result_mult = mult * teta
    result_mult = result_mult % 1 #on garde la partie decimale du r = e*teta, telque r=result_mult ici
    result_mult = result_mult * 26 
    result_mult = math.floor(result_mult) #on garde la partie entiere
    return result_mult

def hachage(tab_):
    for i in range(len(tab_)):
        bloomFiltre = [0 for i in range(26)]
        #on calcule les cles avec 5 fonctions de hashage
        H1 = hashage_fct(tab_[i])
        H2 = hash_compression(tab_[i])
        H3 = hash_multip(tab_[i])
        H4 = hash_devision(tab_[i])
        H5 = hashage_extraction(tab_[i])
        #on place des 1 dans le tableaux de filtre de bloom 
        bloomFiltre[H1] = 1
        bloomFiltre[H2] = 1
        bloomFiltre[H3] = 1
        bloomFiltre[H4] = 1
        bloomFiltre[H5] = 1
    print(bloomFiltre)


def contient(a, b):
    #on verifie si le tableau contient le mot 
    if b == a:
        print('true, le mot appartient')
        return True
    else:
        print('false, le mot n\'appartient pas')
        return False


def fauxPositive():
    #methode pour calculer les faux positifs
    P = math.pow((1 - math.exp((-10000 * k / N))), k)
    print(P)

print("Remplissage du tableau avec ",N," mots contenant ",taille_de_mot," lettres :\n")
remplir(TabFBa)
print("affichage des mots :\n")
#afficher(TabFBa)

print("Representation du filtre apres insertion des cles :\n")
hachage(TabFBa)

print("\ntaux de faux positive :\n")
fauxPositive()
