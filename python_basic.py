import random


menu = """
                  PPPPPPPPPPPPPPPPP    lllllll                            tttt                             iiii  
                  P::::::::::::::::P   l:::::l                         ttt:::t                            i::::i 
                  P::::::PPPPPP:::::P  l:::::l                         t:::::t                             iiii  
                  PP:::::P     P:::::P l:::::l                         t:::::t                                    
                  P::::P     P:::::P   l::::l    aaaaaaaaaaaaa   ttttttt:::::ttttttt     zzzzzzzzzzzzzzzzz iiiiiii 
                  P::::P     P:::::P   l::::l    a::::::::::::a  t:::::::::::::::::t     z:::::::::::::::z i:::::i 
                  P::::PPPPPP:::::P    l::::l    aaaaaaaaa:::::a t:::::::::::::::::t     z::::::::::::::z   i::::i 
                  P:::::::::::::PP     l::::l             a::::a tttttt:::::::tttttt     zzzzzzzz::::::z    i::::i 
                  P::::PPPPPPPPP       l::::l      aaaaaaa:::::a       t:::::t                  z::::::z    i::::i 
                  P::::P               l::::l    aa::::::::::::a       t:::::t                 z::::::z     i::::i 
                  P::::P               l::::l   a::::aaaa::::::a       t:::::t                z::::::z      i::::i 
                  P::::P               l::::l   a::::a    a:::::a      t:::::t    tttttt     z::::::z       i::::i 
                  PP::::::PP           l::::::l a::::a    a:::::a      t::::::tttt:::::t    z::::::zzzzzzzz i::::::i
                  P::::::::P           l::::::l a:::::aaaa::::::a       tt::::::::::::::t  z::::::::::::::z i::::::i
                  P::::::::P           l::::::l  a::::::::::aa:::a        tt:::::::::::tt z:::::::::::::::z i::::::i
                  PPPPPPPPPP           llllllll   aaaaaaaaaa  aaaa          ttttttttttt   zzzzzzzzzzzzzzzzz iiiiiiii
----------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------
  _  _                                                                   _                                               _             
 | \| |  _  _   _ _    __   __ _     _ __   __ _   _ _   ___   ___    __| |  ___     __ _   _ __   _ _   ___   _ _    __| |  ___   _ _ 
 | .` | | || | | ' \  / _| / _` |   | '_ \ / _` | | '_| / -_) (_-<   / _` | / -_)   / _` | | '_ \ | '_| / -_) | ' \  / _` | / -_) | '_|
 |_|\_|  \_,_| |_||_| \__| \__,_|   | .__/ \__,_| |_|   \___| /__/   \__,_| \___|   \__,_| | .__/ |_|   \___| |_||_| \__,_| \___| |_|  
                                    |_|                                                    |_|
----------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------

          [1] Conversor de criptomonedas                                  [4] Adivina el número (juego) 

          [2] Prueba de números primos                                    [5] Generador de contraseñas 
           
          [3] Identificador de palíndromos                                [6] Piedra, papel o tijeras (juego)


"""


menu2 = """
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
   __                                                          ____                      _          
 /  __\                                                       /  __\                    | |         
| /  \/  ___   _ __  __   __  ___  _ __  ___   ___   _ __    | /  \/ _ __  _   _  _ __  | |_   ___  
| |     / _ \ | '_ \ \ \ / / / _ \| '__|/ __| / _ \ | '__|   | |    | '__|| | | || '_ \ | __| / _ \ 
| \__/\| (_) || | | | \ V / |  __/| |   \__ \| (_) || |      | \__/\| |   | |_| || |_) || |_ | (_) |
 \____/ \___/ |_| |_|  \_/   \___||_|   |___/ \___/ |_|       \____/|_|    \__, || .__/  \__| \___/ 
                                                                            __/ || |                
                                                                           |___/ |_|                

-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
Bienveido!!! 
Este programa te ayuda a convertir tus dólares a las 5 principales criptomonedas que del mercado. 
Para hacerlo deberas elegir la moneda que deseas y los dólares con los que cuentas.

¡¡¡IMPORTANTE!!!
**Los valores que se usaron pueden cambiar, ya que el mercado crypto es muy volatil.**
**Los valores usados hacen referencia a la fecha: 30 de octubre del 2021**

    [1] Bitcoin
    [2] Ethereum
    [3] Cardano
    [4] Solana
    [5] Litecoin

"""


menu3 = """
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
        _   _     __                                         _____        _                        
       | \ | |   /_/                                        | ___ \      (_)                       
       |  \| | _   _  _ __ ___    ___  _ __   ___   ___     | |_/ / _ __  _  _ __ ___    ___   ___ 
       | . ` || | | || '_ ` _ \  / _ \| '__| / _ \ / __|    |  __/ | '__|| || '_ ` _ \  / _ \ / __|
       | |\  || |_| || | | | | ||  __/| |   | (_) |\__ \    | |    | |   | || | | | | || (_) |\__ \\
       \_| \_/ \__,_||_| |_| |_| \___||_|    \___/ |___/    \_|    |_|   |_||_| |_| |_| \___/ |___/

-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
Bienvenido!!!
En este programa podrás determinar si un número es primo o no.
Recuerda que los números primos son aquellos que números enteros que solo son divisibles para 1 y para si 
mismos.                                                                                     
"""


menu4 = """
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
            ______         _   _            _                                     
            | ___ \       | | /_/          | |                                    
            | |_/ /  __ _ | | _  _ __    __| | _ __   ___   _ __ ___    ___   ___ 
            |  __/  / _` || || || '_ \  / _` || '__| / _ \ | '_ ` _ \  / _ \ / __|
            | |    | (_| || || || | | || (_| || |   | (_) || | | | | || (_) |\__\\
            \_|     \__,_||_||_||_| |_| \__,_||_|    \___/ |_| |_| |_| \___/ |___/
                                                                            
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
Bienvenido!!!
Este programa te ayudará a identificar palíndromos dentro de palabras y frases.
Un palíndromo es una palabra o frase que puede leerse de la misma forma al derecho a al revés.
Un ejemplo de palíndromo es: Luz azul = luza Zul 
"""


menu5 = """
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
      ___       _  _         _                         _     _   _     __                                 
     / _ \     | |(_)       (_)                       | |   | \ | |   /_/                                  
    / /_\ \  __| | _ __   __ _  _ __    __ _      ___ | |   |  \| | _   _  _ __ ___    ___  _ __   ___  
    |  _  | / _` || |\ \ / /| || '_ \  / _` |    / _ \| |   | . ` || | | || '_ ` _ \  / _ \| '__| / _ \ 
    | | | || (_| || | \ V / | || | | || (_| |   |  __/| |   | |\  || |_| || | | | | ||  __/| |   | (_) |
    \_| |_/ \__,_||_|  \_/  |_||_| |_| \__,_|    \___||_|   \_| \_/ \__,_||_| |_| |_| \___||_|    \___/ 

-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------                                                                                                
Bienvenido!!!
En este juego la computadora elegirá un número al azar entre el 1 y el 100.

Para ganar el juego necesitas adivinar que número eligió la computadora, para hacerlo se te brindará pistas
donde si necesitas buscar un número más grande la maquina te dirá "Ups!!! Busca un número más grande" y en
el caso de necesitar un número más pequeño te dirá "Ups!!! Busca un número más pequeño".

Recuerda que solo tienes 5 intentos para encontrar el número.
Con cada intento fallido perderas una vida: ❤️❤️❤️❤️❤️
"""


menu6 = """
-----------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------
     _____                       _                                 _                              ___             
    /  __ \                     | |                               | |                            /__/              
    | /  \/ _ __   ___   __ _   | |_  _   _     ___   ___   _ __  | |_  _ __   __ _  ___   ___  _ __    __ _ 
    | |    | '__| / _ \ / _` |  | __|| | | |   / __| / _ \ | '_ \ | __|| '__| / _` |/ __| / _ \| '_ \  / _` |
    | \__/\| |   |  __/| (_| |  | |_ | |_| |  | (__ | (_) || | | || |_ | |   | (_| |\__ \|  __/| | | || (_| |
     \____/|_|    \___| \__,_|   \__| \__,_|   \___| \___/ |_| |_| \__||_|    \__,_||___/ \___||_| |_| \__,_|
                                                                                                       
------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
Bienvenido!!!
Este programa te permitirá crear una nueva contraseña de forma segura, por ello para crear la contraseña se utilizan: 
 - Letras mayúsculas
 - Letras minúsculas
 - Números
 - Símbolos especiales

La contraseña se creará de forma aleatoria.
"""


menu7 = """
--------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------
  ______  _            _                                              _           _    _   _                    
  | ___ \(_)          | |                                            | |         | |  (_) (_)                   
  | |_/ / _   ___   __| | _ __   __ _      _ __    __ _  _ __    ___ | |   ___   | |_  _   _   ___  _ __   __ _ 
  |  __/ | | / _ \ / _` || '__| / _` |    | '_ \  / _` || '_ \  / _ \| |  / _ \  | __|| | | | / _ \| '__| / _` |
  | |    | ||  __/| (_| || |   | (_| | _  | |_) || (_| || |_) ||  __/| | | (_) | | |_ | | | ||  __/| |   | (_| |
  \_|    |_| \___| \__,_||_|    \__,_|( ) | .__/  \__,_|| .__/  \___||_|  \___/   \__||_| | | \___||_|    \__,_|
                                      |/  | |           | |                              _/ |                   
                                          |_|           |_|                             |__/                    
--------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------
Bienvenido!!!
En este juego tendrás que competir contra la computadora, ella elegirá una opción de forma aleatoria para jugar contigo.

Tienes tres opciones para escoger:

    [1] Piedra 🪨
    [2] Papel 📃
    [3] Tijera ✂️

"""


def cryptocurrency(tipe_cryptocurrency, dollar_value):
    dollar = float(input("Cuantos dólares tienes?: "))
    crypto = dollar / dollar_value
    dollar = int(dollar)
    crypto = round(crypto, 8)
    crypto = str(crypto)
    print("Tus " + str(dollar) + " dólares equivalen a " + str(crypto) + " " + str(tipe_cryptocurrency))


def primality_test(option3):
    for i in range(1, option3 + 1):
        valor = option3 % i
        if i == 1 or i == option3:
            continue
        if valor == 0:
            return False
        else:
            return True


def palindrome_identifier(word):
    word = word.replace(" ", "")
    word = word.lower()
    inverted_word = word[::-1]
    if word == inverted_word:
        return True
    else:
        return False


def play_num():
    random_num = random.randint(1, 100)
    num = int(input("Elige un número entre el 1 y el 100: "))
    life = 5
    while num != random_num:
        if num < random_num:
            print("Ups!!! Busca un número más grande")
            life -= 1
        elif num > random_num:
            print("Ups!!! Busca un número más pequeño")
            life -= 1
        if life == 0:
            print("Oh oh perdiste")
            break
        print("Tienes", life, "vidas ❤️")
        num = int(input("Elige otro número: "))
    if num == random_num:
        print("Ganaste!!!")
    

def password_generator():
    print(menu6)
    range_password = int(input("¿Cuántos caracteres quieres que tenga tu contraseña?: "))
    capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbols = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    characters = capital_letters + lowercase + symbols + numbers

    password = []

    for i in range(range_password):
        caracter_random = random.choice(characters)
        password.append(caracter_random)
    
    password = "".join(password)
    return password


def rock_paper_scissor(option7):
    option_computer = (1, 2, 3)
    option_computer = random.randint(0, 2)
    while option7 != 1 and option7 != 2 and option7 != 3:
            print("Error!!! ⚠️ \nEscoge una opción que se encuentre dentro del menu")
            option7 = int(input("Elige una opción entre 1, 2 y 3 para empezar: "))
            continue
    if option7 == 1:
        if option_computer == 2:
            print("Tu elección fue piedra 🪨\nLa elección de la computadora fue papel 📃\nEl 📃 le gana a 🪨\nPerdiste!!! 😵 Suerte para la próxima")
        elif option_computer == 3:
            print("Tu elección fue piedra 🪨\nLa elección de la computadora fue tijera ✂️\nLa 🪨 le gana a la ✂️\nGanaste!!! 🎉 Eres un campeón!!!")
        else: 
            print("Tu elección fue piedra 🪨\nLa elección de la computadora fue piedra 🪨\nLos dos obtuvieron piedra 🪨\nEsto fue un empate!!! 😲")
    elif option7 == 2:
        if option_computer == 1:
            print("Tu elección fue papel 📃\nLa elección de la computadora fue piedra 🪨\nEl 📃 le gana a 🪨\nGanaste!!! 🎉 Eres un campeón!!!")
        elif option_computer == 3: 
            print("Tu elección fue papel 📃\nLa elección de la computadora fue tijera ✂️\nLa ✂️ le gana al 📃\nPerdiste!!! 😵 Suerte para la próxima")
        else: 
            print("Tu elección fue papel 📃\nLa elección de la computadora fue papel 📃\nLos dos obtuvieron papel 📃\nEsto fue un empate!!! 😲")
    else:
        if option_computer == 1:
            print("Tu elección fue tijera ✂️\nLa elección de la computadora fue piedra 🪨\nLa 🪨 le gana a la ✂️\nPerdiste!!! 😵 Suerte para la próxima")
        elif option_computer == 2:
            print("Tu elección fue tijera ✂️\nLa elección de la computadora fue papel 📃\nLa ✂️ le gana al 📃\nGanaste!!! 🎉 Eres un campeón!!!")
        else: 
            print("Tu elección fue tijera ✂️\nLa elección de la computadora fue tijera ✂️\nLos dos obtuvieron tijera ✂️\nEsto fue un empate!!! 😲")


def run():
    option = int(input( menu + "Escoge una opción: "))
    if option == 1:
        print(menu2)
        option2 = int(input("Elige una opción: "))
        while option2 != 1 and option2 != 2 and option2 != 3 and option2 != 4 and option2 != 5:
            print("Error!!! Escoge una opción que se encuentre dentro del menu")
            option2 = int(input("Elige una opción: "))
            continue
        if option2 == 1:
            cryptocurrency("Bitcoin", 61700)
        elif option2 == 2:
            cryptocurrency("Ethereum", 4320)
        elif option2 == 3: 
            cryptocurrency("Cardano", 1.98)
        elif option2 == 4:
            cryptocurrency("Solana", 195)
        else:
            cryptocurrency("Litecoin", 192)
    elif option == 2:
        print(menu3)
        option3 = int(input("Escribe un número para comprobarlo: "))
        if primality_test(option3): 
            print("El número 🔢" + str(option3) + "🔢 es primo")
        else:
            print("El número 🔢" + str(option3) + "🔢 no es primo")
    elif option == 3:
        print(menu4)
        option4 = int(input("Escribe el número 1 si entendiste: "))
        while option4 != 1:
            print("Error!!! Escoge la opción correcta para continuar")
            option4 = int(input("Escribe el número 1 si entendiste: "))
            continue
        word = input("Escribe una frase o palabra: ")
        true_palindrome = palindrome_identifier(word)
        if true_palindrome == True:
            print("La frase/palabra 🤙🏽 " + str(word) + " 🤙🏽 es un palíndromo.")
        else: 
            print("La frase/palabra 😲 " + str(word) + " 😲 no es un palíndromo.")
    elif option == 4: 
        print(menu5)
        play_num()
    elif option == 5:
        password = password_generator()
        print("Tu nueva contraseña es: 🔒" + str(password) + "🔒 no olvides guardarla bien para no olvidarla.")
    elif option == 6:
        print(menu7)
        option7 = int(input("Elige el número de la opción que elegiste: "))
        rock_paper_scissor(option7)


if __name__ == "__main__":
    run()