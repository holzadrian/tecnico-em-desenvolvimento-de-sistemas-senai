programa {
  funcao inicio() 
  {
        cadeia nome[5], destino[5]
        inteiro idade[5]
        logico prioridade[5]

        inteiro i

        para (i = 0; i < 5; i++)
        {
            escreva("Digite o nome do passageiro ", i+1, ": ")
            leia(nome[i])

            escreva("Digite o destino do passageiro ", i+1, ": ")
            leia(destino[i])

            escreva("Digite a idade do passageiro ", i+1, ": ")
            leia(idade[i])

            se (idade[i] > 60 ou idade[i] < 5)
            {
                prioridade[i] = verdadeiro
            }
            senao
            {
                prioridade[i] = falso
            }

            escreva()
        }

        escreva("=== Lista de Passageiros ===")
        para (i = 0; i < 5; i++)
        {
            escreva("Passageiro ", i+1, ": ", nome[i], " - Destino: ", destino[i], " - Idade: ", idade[i])
            se (prioridade[i])
            {
                escreva(" - PRIORIDADE! ")
            }
            senao
            {
                escreva(" - Sem prioridade. ")
            }
        }
    }
}