series_favoritas = []

print("Por favor, digite suas 5 séries favoritas:")
for i in range(5):
    serie = input(f"Digite a série {i+1}: ")
    series_favoritas.append(serie)

print("\nAqui está sua lista de séries favoritas:")
for i, serie in enumerate(series_favoritas, 1):
    print(f"{i}. {serie}")