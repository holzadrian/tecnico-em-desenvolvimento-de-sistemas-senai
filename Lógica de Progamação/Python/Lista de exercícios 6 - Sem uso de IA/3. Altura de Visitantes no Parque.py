podem = 0
npodem = 0
for i in range(1, 6):
    altura = float(input(f"Digite a altura do {i}: "))
    if altura > 1.40:
        podem += 1
    else:
        npodem += 1
print(f"{podem} Podem entrar no baguio")
print(f"{npodem} N podi entrar na budega")