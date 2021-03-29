def karakter_sorszam(p_betu, p_szoveg):
    for i in range(len(p_szoveg)):
        if p_szoveg[i] == p_betu:
            return p_szoveg[i+1:]

def ido_atvaltas(p_mp):

    ora = p_mp // 3600
    perc = (p_mp - ora*60*60) // 60
    mp = p_mp-(perc*60+ora*3600)
    return ora%24, perc, mp

txt = open(r'../scratches/musor.txt', 'r')
sor = txt.readline()
sor = txt.readline()
beolvasott_fajl = []

while sor != "":
    beolvasott_fajl.append(sor.strip())
    sor = txt.readline()

txt.close()
#2. feladat *************************************************

csatorana_1 = 0
csatorana_2 = 0
csatorana_3 = 0

for i in range(len(beolvasott_fajl)):
    if beolvasott_fajl[i][0] == "1":
        csatorana_1 += 1
    if beolvasott_fajl[i][0] == "2":
        csatorana_2 += 1
    if beolvasott_fajl[i][0] == "3":
        csatorana_3 += 1

print(f'Az egyes csatornán {csatorana_1}, a kettesen {csatorana_2}, a hármason pedig {csatorana_3} számot lehetett hallgatni.')

#3. feladat**************************************************

splittelt = []
eric_clapton = []

for i in range(len(beolvasott_fajl)):
    splittelt.append(beolvasott_fajl[i].split(" "))
    if splittelt[i][3] == "Eric" and "Clapton" in splittelt[i][4]:
        eric_clapton.append(splittelt[i])

elso_eric = False
eltelt_perc = 0
eltelt_mp = 0


for i in range(len(splittelt)):
    if splittelt[i] == eric_clapton[0]:
        elso_eric = True

    if elso_eric and eric_clapton[0][0] == splittelt[i][0]:
        eltelt_perc += int(splittelt[i][1])
        eltelt_mp += int(splittelt[i][2])

    if  splittelt[i] == eric_clapton[-1]:
        elso_eric = False

print(eltelt_perc, eltelt_mp)
#4. feladat**************************************************

legendaig = []
legendaig_mas_adok = []
legendaig_harmadik_ado = []

for i in range(len(splittelt)):
    legendaig.append(splittelt[i])
    if splittelt[i][3] == "Omega:Legenda":
        break

for i in range(len(legendaig)):
    if legendaig[-i][0] != legendaig[-1][0] and i!=0:
        legendaig_mas_adok.append(legendaig[-i])

for i in range(len(legendaig_mas_adok)):
    if legendaig_mas_adok[i][0] != legendaig_mas_adok[0][0] and i!=0:
        legendaig_harmadik_ado.append(legendaig_mas_adok[i])

print(f'A {legendaig_mas_adok[0][0]}. csatornán ment: {" ".join(legendaig_mas_adok[0][3:])}')
print(f'A {legendaig_harmadik_ado[0][0]}. csatornán ment: {" ".join(legendaig_harmadik_ado[0][3:])}')

#5. feladat**************************************************

irando_fajl = open(r'../scratches/keres.txt', 'w')

szamok = []
input_szoveg = "gaoaf"#input("Adja meg:")
szamok_fuzve = []

for i in range(len(splittelt)):
    szamok.append(" ".join(splittelt[i][3:]).lower())

# for i in range(len(szamok)):
    # pass

for i in range(len(szamok)):
    aktualis_szoveg = szamok[i]
    for j in range(len(input_szoveg)):
        if aktualis_szoveg is None:
            break
        aktualis_szoveg = karakter_sorszam(input_szoveg[j],aktualis_szoveg)
    if aktualis_szoveg is not None:
        irando_fajl.write("{0} {1}\n".format(input_szoveg,szamok[i]))

irando_fajl.close()

#6. feladat**************************************************

egyes_ado = []
idok = []
egyes_musor_ido = 0
egyes_musor_ido_eredeti = 0
aktualis_ora = 0
irando_fajl = open(r'../scratches/idopontok.txt', 'w')

for i in range(len(splittelt)):
    if splittelt[i][0] == "1":
        egyes_ado.append(splittelt[i])
for i in range(len(egyes_ado)):
    idok.append(int(egyes_ado[i][1])*60-60+int(egyes_ado[i][2]))
for i in range(len(idok)):
    a = int(idok[i])
    a+=60
    idok[i] = a

for i in range(len(idok)):
    egyes_musor_ido_eredeti += idok[i]
    irando_fajl.write(f'{ido_atvaltas(egyes_musor_ido_eredeti-idok[i])[0]}:{ido_atvaltas(egyes_musor_ido_eredeti-idok[i])[1]}:{ido_atvaltas(egyes_musor_ido_eredeti-idok[i])[2]}      ')
    egyes_musor_ido += idok[i]
    b = idok[i]
    b -= 60
    idok[i] = b
    irando_fajl.write(f'{ido_atvaltas(egyes_musor_ido-idok[i])[0]}:{ido_atvaltas(egyes_musor_ido-idok[i])[1]}:{ido_atvaltas(egyes_musor_ido-idok[i])[2]}')
    irando_fajl.write(f'        {" ".join(egyes_ado[i][3:])}')
    irando_fajl.writelines((f' (hossza  {ido_atvaltas(idok[i]+60)[0]}:{ido_atvaltas(idok[i]+60)[1]}:{ido_atvaltas(idok[i]+60)[2]})\n'))
    if ido_atvaltas(egyes_musor_ido)[0] != aktualis_ora:
        c = idok[i]
        c += abs(ido_atvaltas(egyes_musor_ido)[1]*60+ido_atvaltas(egyes_musor_ido)[2]-idok[i])+240
        egyes_musor_ido += c
    aktualis_ora = ido_atvaltas(egyes_musor_ido)[0]

irando_fajl.close()








