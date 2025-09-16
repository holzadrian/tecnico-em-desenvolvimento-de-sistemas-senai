programa
{
    funcao inicio() 
    {
        inteiro numeroBase
        inteiro matriz[3][3]
        inteiro i, j
       
        escreva("Digite o número base para a tabuada: ")
        leia(numeroBase)

        para (i = 0; i < 3; i++)
        {
            para (j = 0; j < 3; j++)
            {
                matriz[i][j] = numeroBase * (i*3 + j + 1)
            }
        }

        escreva("Tabuada do número ", numeroBase, "\n")
        para (i = 0; i < 3; i++)
        {
            para (j = 0; j < 3; j++)
            {
                escreva(matriz[i][j], "\t")
            }
            escreva("\n")
        }
    }
}