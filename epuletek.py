import Epulet

f = open("epulet.txt","r",encoding="utf-8")
f.readline()
sorok = f.readlines()
f.close()

def harmasFeladatAB():
    index = 0
    while index < len(sorok):
        index+=1
    print(f"III/A, B:\n\tAz epuletek szama: {index}")


def cHarmas():
    index = 0
    labMagassabMint555 = 0
    while index < len(sorok):
        haz = Epulet.Epulet(sorok[index])
        if haz.magassag > 169:
            labMagassabMint555 += 1
        index+=1
    print(f"III/C\n\tAz 555 labnal magasabb epuletek szama: {labMagassabMint555}")


def dHarmas():
    legoregebbEpulet = 2000
    legoregebbEpuletNeve = ""
    index = 0
    while index < len(sorok):
        haz = Epulet.Epulet(sorok[index])
        if haz.epult < legoregebbEpulet:
            legoregebbEpulet = haz.epult
            legoregebbEpuletNeve = haz.orszag
        index+=1
    print(f"III/D:\n\t A legoregebb epulet orszaga: {legoregebbEpuletNeve}")

