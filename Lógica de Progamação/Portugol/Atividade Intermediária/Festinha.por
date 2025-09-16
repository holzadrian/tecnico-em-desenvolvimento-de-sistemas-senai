programa {
  funcao inicio() {
        cadeia nome
        real temperatura
        cadeia convite
        inteiro visitantesEntraram = 0
        inteiro visitantesBarrados = 0

        faca
        {
            escreva("Digite o nome do visitante \n(ou 'fim' para terminar): ")
            leia(nome)

            se (nome == "fim")
            {
                pare
            }

            escreva("Digite a temperatura corporal do visitante: ")
            leia(temperatura)

            escreva("O visitante trouxe convite? (sim/não): ")
            leia(convite)

            se (temperatura > 37.5 ou convite != "sim")
            {
                visitantesBarrados = visitantesBarrados + 1
                escreva(nome, " foi barrado.\n")
            }
            senao
            {
                visitantesEntraram = visitantesEntraram + 1
                escreva(nome, " entrou.\n")
            }

        } enquanto (nome != "fim")

        escreva("Total de visitantes que entraram: ", visitantesEntraram, "\n")
        escreva("Total de visitantes barrados: ", visitantesBarrados, "\n")
  }
}
