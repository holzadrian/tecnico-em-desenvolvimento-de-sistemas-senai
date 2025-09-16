programa 
{
    funcao inicio() 
    {
      inteiro a, b, c, maior
   
   escreva("Digite o número do primeiro guerreiro: ")
   leia (a)

   escreva("Digite o número do segundo guerreiro: ")
   leia (b)

   escreva("Digite o número do terceiro guerreiro: ")
   leia (c)

   se ((a > b) e (a > c))
   {
    maior = a
   }
   senao se ((b > a) e (b > c))
   {
    maior = b
   }
   senao
   {
    maior = c
   }
    
    escreva("O ganhador é: ", maior)
  }
}
