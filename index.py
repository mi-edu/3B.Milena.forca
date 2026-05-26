
import random


palavras = [
    "python",
    "programacao",
    "sistema",
    "algoritmo",
    "teclado",
    "internet",
    "computador",
    "desenvolvedor",
    "software",
    "terminal"
]


forca = [
"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",

"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",

"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",

"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",

"""
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",

"""
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""",

"""
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
"""
]

recorde = 0

def escolher_palavra():
    """Escolhe uma palavra aleatória."""
    return random.choice(palavras)

def mostrar_palavra(palavra, letras_acertadas):
    """Mostra a palavra com letras descobertas."""
    resultado = ""

    for letra in palavra:
        if letra in letras_acertadas:
            resultado += letra + " "
        else:
            resultado += "_ "

    return resultado

def jogar():
    global recorde

    palavra_secreta = escolher_palavra()

    letras_acertadas = []
    letras_tentadas = []
    letras_erradas = []

    vidas = 6
    pontos = 0

    print("=" * 40)
    print("        JOGO DA FORCA - PYTHON")
    print("=" * 40)
    print("Descubra a palavra secreta!")
    print()

    while vidas > 0:

        print(forca[6 - vidas])

        print("Palavra:", mostrar_palavra(
            palavra_secreta,
            letras_acertadas
        ))

        print("Letras tentadas:", letras_tentadas)
        print("Letras erradas:", letras_erradas)

        print("Vidas:", vidas)
        print("Pontos:", pontos)
        print("Recorde:", recorde)

        print("-" * 40)

        letra = input("Digite uma letra: ").lower()

        
        if len(letra) != 1:
            print("Digite apenas UMA letra.\n")
            continue

        if not letra.isalpha():
            print("Digite apenas letras.\n")
            continue

        if letra in letras_tentadas:
            print("Você já tentou essa letra.\n")
            continue

        letras_tentadas.append(letra)

        
        if letra in palavra_secreta:
            print("Boa! A letra existe na palavra.")
            letras_acertadas.append(letra)
            pontos += 10

        else:
            print("Ops! Essa letra não está na palavra.")
            letras_erradas.append(letra)
            vidas -= 1
            pontos -= 2

        print()

        
        venceu = all(
            letra in letras_acertadas
            for letra in palavra_secreta
        )

        if venceu:
            print("=" * 40)
            print("PARABÉNS! VOCÊ VENCEU!")
            print("A palavra era:", palavra_secreta)
            print("Pontuação final:", pontos)

            
            if pontos > recorde:
                recorde = pontos
                print("NOVO RECORDE!")

            print("=" * 40)
            break

    
    if vidas == 0:

        print(forca[6])

        print("=" * 40)
        print("FIM DE JOGO!")
        print("A palavra era:", palavra_secreta)
        print("Pontuação final:", pontos)

        
        if pontos > recorde:
            recorde = pontos
            print("NOVO RECORDE!")

        print("=" * 40)


while True:

    jogar()

    resposta = input(
        "\nDeseja jogar novamente? (s/n): "
    ).lower()

    if resposta != "s":
        print("\nObrigado por jogar!")
        break
