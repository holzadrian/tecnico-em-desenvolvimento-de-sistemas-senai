programa {
  funcao inicio() {

        inteiro numero, i, pares

        pares = 0

        para (i = 1; i <= 5; i = i + 1)
        {
        escreva("Digite o ", i, "° número: ")
        leia (numero)

        se (numero % 2 == 0)
        {
          pares = pares + 1
        }
        }
        escreva("Você digitou ", pares, " números pares.")
  }
}
