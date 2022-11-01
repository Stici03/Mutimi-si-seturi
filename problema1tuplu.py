e1=("Stici", "Nicolae", "baiat", 9, 10, 9)
e2=("Cucu", "Stefan", "baiat",  7, 8, 9)
e3=("Creciun", "David","baiat",  6, 2, 8)
e4=("Cociuc", "Victor","baiat", 9, 9, 4)
e5=("Turcanu", "Marius","baiat", 10, 9, 8)
qw=[1, 2, 3, 4]
elevi=[list(e1), list(e2), list(e3), list(e4), list(e5)]
for i in range(len(elevi)):
    print(("{elevul} are notele {de} si media {l}").format(elevul=str(elevi[i][0])+" "+ str(elevi[i][1]), de=str(elevi[i][3:]), l=sum(elevi[i][3:])/3))
    if (((9 and 10) in elevi[i][3:]) and 8 not in elevi[i][3:]) and sum(elevi[i][3:])/3>=9.00:
        print("{str} este eminent". format(str=str(elevi[i][0]+" "+ str(elevi[i][1]))))
    elif ((8 and 9 and 10) in elevi[i][3:]) and sum(elevi[i][3:])/3>=8.50:
        print("{str} este proeminent". format(str=str(elevi[i][0]+" "+ str(elevi[i][1]))))
    else:
        print("{str} nu este nici eminent nici proeminent". format(str=str(elevi[i][0]+" "+ str(elevi[i][1]))))
    for k in range(len(qw)+1):
        if k in elevi[i][-3:]:
            print("{numeprenume} este restantier".format(numeprenume=str(elevi[i][0])+" "+ str(elevi[i][1]) ))   
     