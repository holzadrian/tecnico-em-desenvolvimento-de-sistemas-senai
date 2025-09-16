import random

# Variáveis globais
vida1 = 100
vida2 = 100
aniquilado1 = False
aniquilado2 = False
jogador1 = ""
jogador2 = ""

def exibir_status():
    print(f"{jogador1} esta com {vida1} de vida")
    print(f"{jogador2} esta com {vida2} de vida\n")
    # Mostre o nome e a vida atual dos dois jogadores
    pass

def escolher_magia():
    print("---- Ações ----")
    print("1. Kamehameha (Causa 15 a 30 de dano)")
    print("2. Genki Dama (Causa 10 a 20 de dano + 25% de chance de ANIQUILAR o inimigo)")
    print("3. Semente dos Deuses (Recupera 10 a 25 pontos de vida)\n")
    escolha = int(input("Escolha alguma ação: "))
    return escolha
    # Mostre o menu de magias e peça a escolha do jogador (1, 2 ou 3)
    # Retorne a escolha
    pass

def kamehameha(alvo):
    dano = random.randint(15, 30)
    global vida1, vida2
    if alvo == 1:
        vida2 -= dano
        print(f"\n{jogador1} usou Kamehameha no {jogador2} causando {dano} de dano.\n") 
    else:
        vida1 -= dano
        print(f"\n{jogador2} usou Kamehameha no {jogador1} causando {dano} de dano.\n") 
    # Sorteie o dano entre 15 e 30 e aplique ao alvo
    # Mostre o dano causado
    pass

def genki_dama(alvo):
    dano = random.randint(10, 20)
    global vida1, vida2, aniquilado1, aniquilado2
    if alvo == 1:
        vida2 -= dano
        print(f"\n{jogador1} usou Genki Dama no {jogador2} causando {dano} de dano.\n")
        if random.random() < 0.25:
            aniquilado2 = True
            print (f"{jogador2} foi ANIQUILADO!")
    else:
        vida1 -= dano
        print(f"\n{jogador2} usou Genki Dama no {jogador1} causando {dano} de dano.\n")
        if random.random() < 0.25:
            aniquilado1 = True
            print (f"{jogador1} foi ANIQUILADO!")
    # Sorteie o dano entre 10 e 20 e aplique ao alvo
    # Sorteie chance de congelar (25% de chance)
    # Se congelar, marque o alvo como congelado e informe ao jogador
    pass

def aplicar_cura(jogador):
    cura = random.randint(10, 25)
    global vida1, vida2
    if jogador == 1:
        vida1 += cura
        print(f"\n{jogador1} comeu uma semente dos deuses curando {cura} de vida.\n") 
    else:
        vida2 += cura
        print(f"\n{jogador2} comeu uma semente dos deuses curando {cura} de vida.\n") 
    # Sorteie o valor da cura entre 10 e 25
    # Some na vida do jogador (não pode passar de 100)
    # Mostre quanto foi recuperado
    pass

def turno(jogador):
    global aniquilado1, aniquilado2, vida1, vida2

    if aniquilado1 == True:
        vida1 -= vida1
        return
    
    elif aniquilado2 == True:
        vida2 -= vida2
        return
     
    else:
        exibir_status()
        if jogador == 1:
            print(f"É a vez de {jogador2}!\n")
        else:
            print(f"É a vez de {jogador1}!\n")

        escolha = escolher_magia()

        if escolha == 1:
            if jogador == 1:
                kamehameha(2)
            else:
                kamehameha(1)
        elif escolha == 2:
            if jogador == 1:
                genki_dama(2)
            else:
                genki_dama(1)
        elif escolha == 3:
            if jogador == 1:
                aplicar_cura(1)
            else:
                aplicar_cura(2)
        
        

    # Verifique se o jogador está congelado → Se estiver, informe e remova o congelamento
    # Caso contrário:
    # Peça a escolha da magia
    # Execute a magia correta
    pass

# Programa Principal
print("=== Batalha de Magos ===")
jogador1 = input("Digite o nome do primeiro jogador: ")
jogador2 = input("Digite o nome do segundo" \
" jogador: ")

# Peça os nomes dos jogadores

turno_num = 1

# Enquanto os dois jogadores estiverem vivos:
while vida1 > 0 and vida2 > 0:
    print(f"\n===== TURNO {turno_num} =====")
    
    turno(1)
    if vida2 <= 0:
        break

    turno(2)
    if vida1 <= 0:
        break

    turno_num += 1
    # Mostre o status
    # Execute o turno do Jogador 1
    # Verifique se o Jogador 2 ainda está vivo
    # Execute o turno do Jogador 2

# Após o jogo terminar:
print("\n===== FIM DE JOGO =====")
exibir_status()
if vida1 <= 0:
    print(f"{jogador2} é o MAGO DOS MAGOS!")
else:
    print(f"{jogador1} é o MAGO DOS MAGOS!")
# Mostre o status final
# Informe quem venceu