programa {
  funcao inicio()
   {
    real numero

    escreva("Um número é múltiplo de 3 e de 5 ao mesmo tempo quando ele pode ser dividido exatamente por 3 e também por 5, ou seja, sem deixar resto em nenhuma das divisões. ")
    escreva("Digite um número para descobrir: ")
    leia(numero)

    se ((numero % 3 == 0) e (numero % 5 == 0))
    {
        escreva("O número é múltiplo de 3 e de 5.")
    }
    senao
    {
        escreva("O número NÃO é múltiplo de 3 e de 5.")
    }
  }
}
