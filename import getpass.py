import getpass

def connection():
    mdp_correct = "securepassword123"
    mdp = getpass.getpass("Enter your password: ")
    if mdp == mdp_correct:
        print("Access granted.")
    else:
        print("Access denied.")
connection()