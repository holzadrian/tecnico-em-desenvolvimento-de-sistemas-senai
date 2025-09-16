programa {
  funcao inicio() {
    real peso

    escreva ("Seja muito bem-vindo ao elevador do Edifício Porto Belo. Informamos que a capacidade máxima permitida neste elevador é de 120 kg. Por gentileza, poderia informar seu peso para que possamos verificar se o uso do equipamento está dentro dos limites de segurança?")
    leia (peso)

      se ((peso >= 50) e (peso <= 120))
      
      {
      escreva("Com base nas informações fornecidas, confirmamos que o seu peso está dentro dos limites de segurança. Portanto, você pode entrar no elevador com tranquilidade.")
      }

      senao

      {
        escreva("Infelizmente, com base nas informações fornecidas, o seu peso ultrapassa o limite de segurança para o uso do elevador. Pedimos desculpas pela inconveniência e sugerimos o uso de outra forma de acesso.")
      }
    
  }
}
