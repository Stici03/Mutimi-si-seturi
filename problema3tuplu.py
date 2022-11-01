m1=("Cucu", "Nicu", 20, 188, 78, "m", "celibatar")
m2=("Stici","Nicolae", 18, 178, 80, "m", "casatorit")
m3=("Codreanu","Nelu", 32, 182, 85, "m", "casatorit")
m4=("Ciobanu", "Serafim", 45, 183, 79, "m", "casatorit")
m5= ("Pascari", "Andrei", 16, 189, 90, "m", "celibatar")
m6=("Caraman", "Maria", 33, 165, 67, "f", "celibatar")
m7=("Dediu", "Livia", 17, 180, 69, "f", "casatorit")
m8=("Chetraru", "Chiril", 23, 179, 72, "m", "casatorit")
m9=("Creciun", "Olivia", 29, 175, 78, "f", "celibatar")
m10=("Botnaru", "Inga", 35, 171, 77,"f", "casatorit")
membri=[list(m1), list(m2), list(m3),  list(m4),list(m5), list(m6), list(m7), list(m8),list(m9), list(m10)]
membri1,minori, mmici20, =[], [], []
n=int(input("n= "))
mmare170cm, sub20, fem20singure,mmedie, pers20_50cu_g_mmare_gmedie, mmare18ani, masatot=0, 0, 0, 0, 0, 0,0
if n>10:
    print("eroare")
else: 
    mmici20.extend([x for x in range(1, 20)])
    membri1.extend([membri[i] for i in range(n)])  
    for z in range(len(membri1)):
        print(membri1[z])
        if membri1[z][3]>170:
            mmare170cm+=1
        for qw in range(len(mmici20)):
            if membri1[z][2]==mmici20[qw]:
                sub20+=1
        if (membri1[z][2]>20 and membri1[z][-2]=="f") and membri1[z][-1]=="celibatar":
            fem20singure+=1
        if membri1[z][2]>18:
            mmare18ani+=1
            masatot+=membri1[z][4]
            mmedie=masatot/mmare18ani
        if (membri1[z][2]>20 and membri1[z][2]<50) and membri1[z][4]>mmedie:
            pers20_50cu_g_mmare_gmedie+=1    

    print("""Avem urmatoarele:
{rt} % au varsta mai mica de 20 de ani 
{yu} % au inaltimea mai mare de 170 cm
masa medie a unei persoane este de: {masamedie} kg
procentajul femeilor ce au peste 20 de ani si sunt singure este de: {qwert} %
procentajul persoanelor ce au varsta intre 20 si 50 de ani cu greutatea mai mare decat cea medie este de {trt} % 
""".format(rt=round((sub20/n)*100, 3), 
    yu=round((mmare170cm/n)*100, 3), 
    qwert=round((fem20singure/n*100), 3), masamedie=mmedie, trt=round((pers20_50cu_g_mmare_gmedie/n)*100, 3)))