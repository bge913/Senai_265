programa {
  funcao inicio() {
    
  }
}
    real n1, n2, n3, n4
    real soma, media
    cadeia resultado

    escreva("Nota1: ")
    leia(n1)
    escreva("Nota2: ")
    leia(n2)
    escreva("Nota3: ")
    leia(n3)
    escreva("Nota4: ")
    leia(n4)
    soma = n1 + n2 + n3 + n4
    media = soma / 4.0
    se (media >= 7.0)
    {
      resultado = "aprovado"
    }
      senao se (media >= 5.0)
    {
        resultado = "Recuperacao"
    }
        senao
        {
        resultado = "Reprovado"
    }
    escreva("nota 1: ",n1, "\n")
    escreva("nota 2: ",n2, "\n")
    escreva("nota 3: ",n3, "\n")
    escreva("nota 4: ",n4, "\n")
}