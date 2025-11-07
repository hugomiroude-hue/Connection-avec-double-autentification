import getpass
import random
import os


essai = 0
password = "securepassword123"
mdp = ""


def connection():
    essai = 0
    password = "securepassword123"
    while essai < 3:
        mdp = getpass.getpass("Enter your password: ")
        essai += 1
        if mdp == password:
            if essai >= 3:
                code_pin()
            else:
                print("Password correct. You may proceed.")
                break
        else:
            if essai < 3:
                print("Incorrect password. Try again.")
            else:
                print("too many incorrect attempts. Access denied.")

def code_pin():
    pin = random.randint(1000, 9999)
    print("\nUn code PIN à 4 chiffres a été créé.")
    bureau = os.path.join(os.path.expanduser("~"), "Desktop")
    dossier = bureau if os.path.isdir(bureau) else os.getcwd()
    chemin = os.path.join(dossier, "code pin")
    os.makedirs(chemin, exist_ok=True)

    with open(os.path.join(chemin, "PIN.txt"), "w") as f:
        f.write(f"PIN : {pin}")

    print("Le PIN a été écrit dans le fichier 'PIN.txt'.")
    print("Vous avez 2 essais pour le saisir.")

    essais_pin = 0
    while essais_pin < 2:
        user = input("Entrez le PIN : ")
        essais_pin += 1
        if user == str(pin):
            print("PIN correct. Accès final accordé.")
            return
        else:
            print("PIN incorrect.")
    
    with open(os.path.join(chemin, "bruteforce_detected.txt"), "w") as f:
        f.write("2 échecs de saisie du PIN : brute force détecté.\n")
    print("\nÉchec des 2 essais PIN. Tentative de brute force détectée.")

connection()