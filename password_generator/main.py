import random
import string


def generated_password(characters):
    alle_zeichen = string.ascii_letters + string.digits
    password = ""
    for _ in range(characters):
        password_stelle = random.randint(0, len(alle_zeichen)-1)
        password_neues_zeichen = alle_zeichen[password_stelle]
        password = password + password_neues_zeichen
    return password


print("\nWelcome to the PyPassword Generator!")
characters = int(input("How many characters would you like in your password?: "))

password = generated_password(characters)
print(f"\ndein neues password ist '{password}'\n")
