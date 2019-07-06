import random # bibliotecas que  você tem que immportar
import operator



def problem(): # funçõe 1
	operador = {
	'+': operator.add,
	'-': operator.sub
	}
	a = random.randint(10,99)
	b = random.randint(10,99)
	escolha_operacao = random.choice(list(operador.keys()))
	resposta = operador.get(escolha_operacao) (a,b)
	print(f'quanto e {a} {escolha_operacao} {b}')
	return resposta


def questao ():  #funçõe 2
	gerador = problem()
	palpite = int(input())
	return palpite == gerador


def jogo ():# funçõe 3
	score = 0
	nome = str(input("qual é seu nome?:"))
	print(f"seja bem-vindo {nome}, vamos praticar um pouco... ")
	for e in range(101):
		if questao() == True:
			score +=1
		else:
			print("...")
	print(f"a rodada acabou {nome} voce  acertou {score} vezes ...")


def call(): # função que juntas todas as outras e faz a mágica haha
	start = str(input("Deseja jogar ? [Y/N] "))
	if start == "y" :
	 	 	jogo()
	else:
			print("ok, ate ....")

call() # chamada da função mestre!
