import re

txt = open(r'musor.txt', 'r')
fajl = txt.readlines()
txt.close()


class Radio_ado:

    adok = {}

    def __init__(self, csatorna):
        self.lejatszasi_lista = []
        self.csatorna = csatorna
        self.__class__.adok[self.csatorna] = self

    def __repr__(self):
        return f'Csatorna: {self.csatorna}, lejátszási lista {self.lejatszasi_lista}'

class Zene:

    adatok = []

    def __init__(self, csatorna, hossz, eloado, cim):
        self.csatorna = csatorna
        self.hossz = hossz
        self.eloado = eloado
        self.cim = cim
        self.__class__.adatok.append(self)

    def __repr__(self):
        return f'Csatorna: {self.csatorna}, hossz: {self.hossz}, előadó: {self.eloado}, cím: {self.cim}'

    @staticmethod
    def ido_atvaltas(p_mp):
        ora = p_mp // 3600
        perc = (p_mp - ora * 60 * 60) // 60
        mp = p_mp - (perc * 60 + ora * 3600)
        return ora % 24, perc, mp

minta =  re.compile(r'(\d{1,2})\s(\d{1,2})\s(\d{1,2})\s(.+):(.+)')

Radio_ado("1")
Radio_ado("2")
Radio_ado("3")

for elem in fajl:

    talalat = re.match(minta, elem)

    if talalat:

        dal = Zene(talalat.group(1), int(talalat.group(2)) * 60 + int(talalat.group(3)), talalat.group(4), talalat.group(5))
        Radio_ado.adok[talalat[1]].lejatszasi_lista.append(dal)

for i in Radio_ado.adok.keys():
    print(f'{len(Radio_ado.adok[i].lejatszasi_lista)}')

elso_c = True
elso_c_szam = None
utolso_c_szam = None


for dal_index in range(len(Radio_ado.adok["1"].lejatszasi_lista)):
    dal = Radio_ado.adok["1"].lejatszasi_lista[dal_index]
    if dal.eloado == "Eric Clapton":
        if elso_c:
            elso_c = False
            elso_c_szam = dal_index
        else:
            utolso_c_szam = dal_index
        print(dal, dal_index)

eltelt_ido = 0

for dal in Radio_ado.adok["1"].lejatszasi_lista[elso_c_szam:utolso_c_szam+1]:
    eltelt_ido += dal.hossz
    print(dal)

print(f"{Zene.ido_atvaltas(eltelt_ido)[0]:02d}:{Zene.ido_atvaltas(eltelt_ido)[1]}:{Zene.ido_atvaltas(eltelt_ido)[2]}")

#4. feladat

egyes = []
kettes = []
harmas = []

for dal in Zene.adatok:
    if dal.csatorna == "1":
        egyes.clear()
        egyes.append(dal.eloado+":"+dal.cim)
    if dal.csatorna == "2":
        kettes.clear()
        kettes.append(dal.eloado+":"+dal.cim)
    if dal.csatorna == "3":
        harmas.clear()
        harmas.append(dal.eloado+":"+dal.cim)
    if dal.cim == "Legenda" and dal.eloado == "Omega":
        if egyes != dal.csatorna :
            print(f'Az egyes csatornán szólt: {egyes[0]}')
        if kettes != dal.csatorna :
            print(f'A kettes csatornán szólt: {kettes[0]}')
        if harmas != dal.csatorna :
            print(f'A harmas csatornán szólt: {harmas[0]}')


