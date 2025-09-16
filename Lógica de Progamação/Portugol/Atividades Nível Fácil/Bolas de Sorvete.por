programa {
  funcao inicio() 
  {
    inteiro bolas, total, i

        total = 0

        para (i = 1; i <= 10; i = i + 1)
        {
            escreva("Cliente ", i, ": quantas bolas de sorvete deseja? ")
            leia(bolas)
            total = total + bolas
        }

        escreva("\nTotal de bolas de sorvete vendidas: ", total)
  }
}
