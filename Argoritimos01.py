
print("Escreva a nota um");
nota1=int(input());
print("Escreva a nota dois");
nota2=int(input());
print("Escreva o numero de faltas");
faltas=int(input());
print("Escreva o numero de aulas totais");
aulastotais=int(input());
porcentagem_participacao=faltas/aulastotais;
if (6<=((nota1+nota2)/2)<=10) and (porcentagem_participacao<0.25):
    print("passouu super idol the shogun");


else:
    print("reprovou");
