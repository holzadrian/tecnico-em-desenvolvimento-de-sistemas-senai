programa {
  funcao inicio() {
    inteiro numero, contador, i

     escreva ("Digite qualquer número inteiro e direi a você se esse número é primo ou não. ")
     leia (numero)

     contador = 0

     para (i = 1; i <= numero; i = i + 1)
      {
      se (numero % i == 0)
      {
        contador = contador + 1
      }
     }

     se (contador == 2)
     {
       escreva("O número ", numero, " é primo!")
     }
      senao
      {
       escreva("O número ", numero, " não é par!")
      }
  }
}
