nalunos=int(input("Digite o número total de alunos: "))
mg=0
ap=0
re=0
faf=0
for i in range(nalunos):
  m=0
  n1=int(input("Digite a 1° nota:"))
  n2=int(input("Digite a 2° nota:"))
  m=((2*n2)+n1)/3
  if m>=7:
    mg=mg+m
    ap=ap+1
    print("Aprovado, média:%.2f"%m)
  elif m<4:
    re=re+1
    mg=mg+m
    print("Reprovado, média:%.2f"%m)
  elif m>=4 and m<7:
    faf=faf+1
    af=int(input("Ficou de AF,digite a nota da af:"))
    raf=(af+m)/2
    if raf<5:
      mg=mg+m
      print("Reprovado, média:%.2f"%raf)
    elif raf>=5:
      mg=mg+m
      print("Aprovado, média:%.2f"%raf)

print("Total de alunos:",nalunos,"\nAprovados:",ap,"Reprovados:",re,"Ficaram de AF:",faf,"Média da Turma:%.2f"%mg/nalunos)