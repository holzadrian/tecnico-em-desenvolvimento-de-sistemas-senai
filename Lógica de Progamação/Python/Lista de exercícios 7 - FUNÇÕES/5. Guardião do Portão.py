contador = 0
def abrir_portao():
    global contador
    contador += 1
    if contador == 1:
        print("Pela luz antiga.")
    elif contador == 2:
        print("Pela chave oculta.")
    elif contador == 3:
        print("Pela vontade do código.")
    
abrir_portao()
abrir_portao()
abrir_portao()