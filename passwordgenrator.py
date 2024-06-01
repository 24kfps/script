import string, secrets

chrs = string.ascii_letters
numbers = string.digits

choose = input("What do you want to generate password/pin ?: ")
lenght = input("Choose your password/pin lenght: ")

password_in_chrs = ''.join(secrets.choice(chrs) for i in range (int(lenght)))
password_in_numbers = ''.join(secrets.choice(numbers) for i in range (int(lenght)))

print("*******************Python Password Generator*******************")

if choose == "password":
    print(password_in_chrs)

if choose == "pin":
    print(password_in_numbers)