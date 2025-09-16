def converter_moeda(valor, para):
    if para == "dólar":
        resultado = valor / 5
    elif para == "real":
        resultado = valor * 5

    return resultado

dolar = converter_moeda(100, "dólar")
real = converter_moeda(100, "real")
print (dolar)
print (real)