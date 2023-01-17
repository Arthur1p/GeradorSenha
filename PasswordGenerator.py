import string
import random

digitos = list(string.ascii_letters + string.digits + "!@#$%&*()")

def generate_password():
    password_length = int(input("Qual o tamanho que deseja para a senha: "))

    random.shuffle(digitos)

    senha = []

    for x in range(password_length):
        senha.append(random.choice(digitos))

    random.shuffle(senha)

    senha = "".join(senha)

    print(senha)

option = input("Voce quer gerar uma senha? (S/N): ")

if option == 'S':
    generate_password()
elif option == "N":
    print('Progama encerrado')
    quit()
else:
    print("Digite uma opção valida")