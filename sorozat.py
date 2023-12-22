import random

print("II/A,B,C:")
randomDobasLista = []
index = 0
while index < 7:
    randomDobas = random.randint(1, 2)
    if randomDobas == 1:
        randomDobasLista.append("FEJ")
    else:
        randomDobasLista.append("IRAS")
    index += 1


def masodiFeladat():
    index = 0
    while index < len(randomDobasLista):
        if index == 0:
            print(f"\t{randomDobasLista[index]}", end="")
        else:
            print(f"-{randomDobasLista[index]}", end="")
        index += 1


def fejek_szama():
    fejekSzama = 0
    index = 0
    while index < len(randomDobasLista):
        if randomDobasLista[index] == "FEJ":
            fejekSzama += 1
        index += 1
    return fejekSzama


def konzolra_kiir():
    print("II/D,E:")
    print(f"\n\tA fejek szama: {fejek_szama()}.")


def file_kiir():
    f = open("fejek.txt", "w", encoding="utf-8")
    f.write("II/F:")
    f.write(f"\n\tA fejek szama: {fejek_szama()}")
    f.close()
