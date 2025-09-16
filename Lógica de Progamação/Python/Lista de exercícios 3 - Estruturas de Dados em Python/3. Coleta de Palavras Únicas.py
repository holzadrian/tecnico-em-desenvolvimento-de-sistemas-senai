palavras = []

while True:
    palavra = input("Digite palavras: ")
    if palavra == "fim":
        break
    if palavras not in palavras:
        palavras.append(palavra)
        
palavras.sort()

print("\nTotal de palavras diferentes:", len(palavras))
print("Palavras em ordem alfabética:")
for p in palavras:
    print(p)
    
if "Python" in palavras:
    print("A palavra 'Python' foi digitada.")
else:
    print("A palavra 'Python' NÃO foi diigtada")