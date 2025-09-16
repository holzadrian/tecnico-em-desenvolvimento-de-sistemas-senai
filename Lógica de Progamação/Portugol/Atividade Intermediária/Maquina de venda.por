programa
{
    funcao inicio()
    {
        inteiro codigo, quantidade, i
        real total, pagamento, troco
        real preco[4] 

        preco[1] = 2.50 
        preco[2] = 4.00 
        preco[3] = 6.75 

        para (i = 1; i <= 5; i++)
        {
            escreva("=== Cliente ", i, " ===\n")
            escreva("Produtos disponíveis:\n")
            escreva("1 - Água (R$ ", preco[1], ")\n")
            escreva("2 - Refrigerante (R$ ", preco[2], ")\n")
            escreva("3 - Suco (R$ ", preco[3], ")\n")

            escreva("Digite o código do produto (1 a 3): ")
            leia(codigo)

            se (codigo < 1 ou codigo > 3)
            {
                escreva("Código inválido!\n\n")
            }
            senao
            {
                escreva("Digite a quantidade desejada: ")
                leia(quantidade)

                total = preco[codigo] * quantidade
                escreva("Total a pagar: R$ ", total, "\n")

                escreva("Digite o valor pago: R$ ")
                leia(pagamento)

                se (pagamento >= total)
                {
                    troco = pagamento - total
                    escreva("Pagamento aceito. Troco: R$ ", troco, "\n\n")
                }
                senao
                {
                    escreva("Valor insuficiente! Compra cancelada.\n\n")
                }
            }
        }
    }
}
