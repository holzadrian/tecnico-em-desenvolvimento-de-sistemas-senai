print("\nPrimeira partida: ")
jogador1 = int(input("Digite a pontuação do 1° jogador: "))
jogador2 = int(input("Digite a pontuação do 2° jogador: "))
jogador3 = int(input("Digite a pontuação do 3° jogador: "))
print("\nSegunda partida: ")
total1 = jogador1 + int(input("Digite a pontuação do 1° jogador: "))
total2 = jogador2 + int(input("Digite a pontuação do 2° jogador: "))
total3 = jogador3 + int(input("Digite a pontuação do 3° jogador: "))
print("\nPontuação total")
if total1 > total2 and total1 > total3:
    print(f"O vencedor é o Jogador 1 com {total1} pontos")
elif total2 > total3 and total2 > total1:
    print(f"O vencedor é o Jogador 2 com {total2} pontos")
elif total3 > total1 and total3 > total2:
    print(f"O vencedor é o Jogador 3 com {total3} pontos")
print(f"Jogador 1: {total1} pontos")
print(f"Jogador 2: {total2} pontos")
print(f"Jogador 3: {total3} pontos\n")
if total1 == total2 and total1 == total3:
    print("Houve um empate entre todos...")
elif total1 == total2:
    print(f"Houve um empate entre o Jogador 1 e 2")
elif total2 == total3:
    print(f"Houve um empate entre o Jogador 2 e 3")
elif total1 == total3:
    print(f"Houve um empate entre o Jogador 1 e 3")