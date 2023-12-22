import Epulet


def negyedikFeladat():
    f = open("epulet.txt","r",encoding="utf-8")
    f.readline()
    adatok = f.readlines()
    f.close()
    sorok = 0
    magasabbMint555Lab = 0
    legoregebbEpulet = 2000
    legoregebbEpuletOrszag = ""
    index = 0
    while index < len(adatok):
        sorok += 1
        Haz = Epulet.Epulet(adatok[index])
        if Haz.magassag > 169:
            magasabbMint555Lab += 1
        if Haz.epult < legoregebbEpulet:
            legoregebbEpuletOrszag = Haz.orszag
        index+=1
    print("III/A,B:")
    print(f"\tAz epuletek szama: {sorok}.")
    print("III/C:")
    print(f"\tAz 555 labnal magasabb epuletek szama: {magasabbMint555Lab}.")
    print("III/D:")
    print(f"\tA legoregebb epulet orszaga: {legoregebbEpuletOrszag}.")
