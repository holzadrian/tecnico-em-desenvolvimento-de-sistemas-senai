programa {
  funcao inicio() {
   
        inteiro i, dado, pontos1, pontos2

        pontos1 = 0
        pontos2 = 0

        escreva("Jogador 1 - jogadas:\n")
        para (i = 1; i <= 3; i = i + 1)
        {
            escreva("Digite o resultado da ", i, "ª jogada: ")
            leia(dado)
            pontos1 = pontos1 + dado
        }

        escreva("\nJogador 2 - jogadas:\n")
        para (i = 1; i <= 3; i = i + 1)
        {
            escreva("Digite o resultado da ", i, "ª jogada: ")
            leia(dado)
            pontos2 = pontos2 + dado
        }

        escreva("\nTotal do Jogador 1: ", pontos1)
        escreva("\nTotal do Jogador 2: ", pontos2, "\n")

        se (pontos1 > pontos2)
        {
            escreva("Jogador 1 venceu!")
        }
        senao se (pontos2 > pontos1)
        {
            escreva("Jogador 2 venceu!")
        }
        senao
        {
            escreva("Empate!")
        }
    }
}

  
