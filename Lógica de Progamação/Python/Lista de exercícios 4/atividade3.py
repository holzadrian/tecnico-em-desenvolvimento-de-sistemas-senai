palavras_magicas = set()

while True:
    palavra = input("Digite uma palavra mágica (ou 'acabar' para encerrar): ").strip().lower()
    
    if palavra == "acabar":
        break

    palavras_magicas.add(palavra)

quantidade = len(palavras_magicas)
mais_longa = max(palavras_magicas, key=len) if palavras_magicas else ""
tem_abracadabra = "abracadabra" in palavras_magicas

print("\n Relatório das Palavras Mágicas ✨")
print(f"Total de palavras únicas: {quantidade}")
print(f"Palavra mágica mais longa: {mais_longa}")
print(f"'abracadabra' está na lista? {'Sim' if tem_abracadabra else 'Não'}")
