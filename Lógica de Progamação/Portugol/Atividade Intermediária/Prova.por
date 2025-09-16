programa {
     inclua biblioteca Util --> u  
  funcao inicio() 
  {
        inteiro i, numero1, numero2, resposta, pontos, acertos, erros
        
        pontos = 0
        acertos = 0
        erros = 0

        para (i = 1; i <= 10; i++)
        {
            numero1 = u.sorteia(1, 10)
            numero2 = u.sorteia(1, 10)

            escreva("Pergunta ", i, ": Qual é o resultado de ", numero1, " x ", numero2, "? ")
            leia(resposta)

            se (resposta == numero1 * numero2)
            {
                pontos = pontos + 1 
                acertos = acertos + 1
                escreva(" ✔️ Resposta CORRETA! \n ")
            }
            senao
            {
                pontos = pontos - 1 
                erros = erros + 1
                escreva(" ❌  Resposta ERRADA! \n ")
            }

            escreva()
        }

        escreva("Total de acertos: ", acertos, ("\n") )
        escreva("Total de erros: ", erros, ("\n") )
        escreva("Pontuação final: ", pontos, ("\n") )

        se (pontos >= 6)
        {
            escreva(" ✔️ Parabéns você foi APROVADO! ")
        }
        senao
        {
            escreva(" ❌ Parabéns você foi REPROVADO! ")
        }
    }
}
