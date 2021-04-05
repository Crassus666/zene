import re

txt = open(r'../scratches/musor.txt', 'r')
fajl = txt.readlines()
txt.close()

class zene:

    adatok = []

    def __innit__(self, csatorna, hossz, eloado, cim):
        self.csatorna = csatorna
        self.hossz = hossz
        self.eloado = eloado
        self.cim = cim



    @staticmethod
    def ido_atvaltas(p_mp):
        ora = p_mp // 3600
        perc = (p_mp - ora * 60 * 60) // 60
        mp = p_mp - (perc * 60 + ora * 3600)
        return ora % 24, perc, mp



minta = re.compile(r'(\d{0,2})\s(\d{0,2})\s(\d{0,2})\s(.*):(.*)')
egyes = 0
kettes = 0
harmas = 0
eric_clapton_mp = 0

for elem in fajl:
    talalat = re.match(minta, elem)
    if talalat and talalat[1] == "1":
        zene.adatok.append(talalat.groups())
        egyes += 1
        if talalat[4] == "Eric Clapton":
            eric_clapton_mp += int(talalat[2])*60+int(talalat[3])
    if talalat and talalat[1] == "2":
        kettes += 1
    if talalat and talalat[1] == "3":
        harmas += 1

print(f'Az egyes adón {egyes}, a másodikon {kettes}, a harmadikon {harmas} számot lehetett hallani.')
print(f'{zene.ido_atvaltas(eric_clapton_mp)[0]}:{zene.ido_atvaltas(eric_clapton_mp)[1]}:{zene.ido_atvaltas(eric_clapton_mp)[2]}')
