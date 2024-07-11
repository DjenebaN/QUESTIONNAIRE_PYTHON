
def majeur(age):
    if age >= 18 :
        return True
    else :
        return False


def info():
    nom = input("Quel est votre nom ? ")
    prenom = input("Quel est ton prénom ? ")
    age =  int (input("Quel est votre âge ? "))
    email = input("Quel est ton email ? ")
    adresse = input("Quel est ton adresse ? ")


    print(" Nom :", nom)
    print(f"Prénom : {prenom}" )
    print(" Email :" + email )
    print(" Adresse :", adresse )
    print ("age : ", age)
    
    if majeur(age) : 
        print(f"{nom}, vous êtes majeur.")
    else : 
        print(nom, "vous êtes mineur.")

if __name__ == "__main__":
    info()
