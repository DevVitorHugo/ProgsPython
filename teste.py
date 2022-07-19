#Criando programa com varios subprogramas
#importação de biblioteca
import os



#Subprogramas
def valStr():
    nome = 'vitor'
    print ("Meu nome é", nome,)
def valInt():
    idade = 22
    print(f'Minha idade é', idade,)
def valBol():
    aprovado = True
    print(f'Voce foi { aprovado}')
def valFloat():
    nota = 8.75
    print(f'Sua nota foi{nota}')
    

#programa principal
valStr()
valInt()
valBol()
valFloat()

os.system('pause')

print ('Por hoje é só Velhinhooo!!!')
