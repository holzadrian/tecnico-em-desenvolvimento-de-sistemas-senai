programa {
    funcao inicio() {
        cadeia produtos[64]
        real precos[64]
        inteiro quantidades[64]
        inteiro numeros[64]
        cadeia disponibilidade[64]
        cadeia nomes[64]

        cadeia dispVenda
        cadeia buscaNome
        inteiro menu = 0
        inteiro totalProdutos = 0
        inteiro maxProdutos = 10
        
        para (inteiro i = 1; i <= 63; i++) {
            numeros[i] = 0
            nomes[i] = ""
            quantidades[i] = 0
            precos[i] = 0
            disponibilidade[i] = ""
        }

        escreva("Seja bem vindo(a) ao menu da Tem de Tudo!\n")
        escreva("Digite 1 para CADASTRAR novo produto\n")
        escreva("Digite 2 para LISTAR produtos\n")
        escreva("Digite 3 para ALTERAR produto\n")
        escreva("Digite 4 para REMOVER produto\n")
        escreva("Digite 5 para SAIR\n")
        escreva("Digite o NÚMERO do menu ao qual você quer acessar: ")
        leia(menu)

        enquanto (menu < 5) {
            se (menu == 1) {
                se (totalProdutos >= maxProdutos) {
                    escreva("Limite de produtos atingido!\n")
                } senao {
                    totalProdutos = totalProdutos + 1
                    escreva("Digite o número do produto: ")
                    leia(numeros[totalProdutos])
                    escreva("Digite o nome do produto: ")
                    leia(nomes[totalProdutos])
                    escreva("Digite o valor unitário, usar ponto ao invés de vírgula: ")
                    leia(precos[totalProdutos])
                    escreva("Digite a quantidade: ")
                    leia(quantidades[totalProdutos])
                    escreva("Disponível para venda? (sim ou não) ")
                    leia(dispVenda)
                    enquanto (dispVenda != "não" e dispVenda != "sim") {
                        escreva("Digite apenas sim ou não\n")
                        leia(dispVenda)
                    }
                    disponibilidade[totalProdutos] = dispVenda
                    escreva("Produto cadastrado com sucesso!\n")
                }
            } senao se (menu == 2) {
                se (totalProdutos == 0) {
                    escreva("Nenhum produto cadastrado.\n")
                } senao {
                    para (inteiro i = 1; i <= totalProdutos; i++) {
                        escreva("---- Produto ", i, " ----\n")
                        escreva("Número: ", numeros[i], "\n")
                        escreva("Nome: ", nomes[i], "\n")
                        escreva("Valor unitário: R$ ", precos[i], "\n")
                        escreva("Quantidade: ", quantidades[i], "\n")
                        escreva("Disponível para venda: ", disponibilidade[i], "\n")
                    }
                }
            } senao se (menu == 3) {
                escreva("Digite o número do produto a alterar: ")
                inteiro numProduto
                leia(numProduto)
                inteiro posicao = 0
                para (inteiro i = 1; i <= totalProdutos; i++) {
                    se (numeros[i] == numProduto) {
                        posicao = i
                    }
                }

                se (posicao == 0) {
                    escreva("Produto não encontrado.\n")
                } senao {
                    escreva("Digite o novo preço: ")
                    real novoPreco
                    leia(novoPreco)
                    escreva("Digite a nova quantidade: ")
                    inteiro novaQuantidade
                    leia(novaQuantidade)
                    precos[posicao] = novoPreco
                    quantidades[posicao] = novaQuantidade
                    escreva("Produto atualizado com sucesso!\n")
                }
            } senao se (menu == 4) {
                escreva("Digite o número do produto a remover: ")
                inteiro numProduto
                leia(numProduto)
                para (inteiro i = 1; i <= totalProdutos; i++) {
                    se (numeros[i] == numProduto) {
                        para (inteiro j = i; j < totalProdutos; j++) {
                            numeros[j] = numeros[j + 1]
                            nomes[j] = nomes[j + 1]
                            precos[j] = precos[j + 1]
                            quantidades[j] = quantidades[j + 1]
                            disponibilidade[j] = disponibilidade[j + 1]
                        }
                        totalProdutos = totalProdutos - 1
                        escreva("Produto removido com sucesso!\n")
                    }
                }
            }
            escreva("Deseja retornar ao menu? (sim/não) ")
            cadeia sMenu
            leia(sMenu)
            se (sMenu == "sim") {
                escreva("Seja bem vindo(a) ao menu da Tem de Tudo!\n")
                escreva("Digite 1 para CADASTRAR novo produto\n")
                escreva("Digite 2 para LISTAR produtos\n")
                escreva("Digite 3 para ALTERAR produto\n")
                escreva("Digite 4 para REMOVER produto\n")
                escreva("Digite 5 para SAIR\n")
                escreva("Digite o NÚMERO do menu ao qual você quer acessar: ")
                leia(menu)
            } senao {
                menu = 5
            }
        }

        escreva("Desligando o sistema...\n")
    }
}
