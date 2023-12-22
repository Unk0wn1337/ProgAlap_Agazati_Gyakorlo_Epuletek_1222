def elsoFeladat():
    print("I/A:")
    jatekosNev = str(input("\tJatekos neve:"))
    szerepkor = str(input("\tszerepkor:"))
    print("I/B:")
    if szerepkor == "varazslo":
        print(f"\tUdvozlunk {jatekosNev}, 2 eleted van!")
    elif szerepkor == "harcos":
        print(f"\tUdvozlunk {jatekosNev}, 10 eleted van!")
    else:
        print(f"\tUdvozlunk {jatekosNev}, 8 eleted van!")
