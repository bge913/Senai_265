saldo = 0.0

print("Bem-vindo ao Sicredi!")
while True:
    print("\nEscolha uma opção:")
    print("1 - depositar")
    print("2 - Sacar")
    print("3 - Ver saldo")
    print("4 - Sair")
    
    op = input("escolha:")
    if op == "1":
        valor = float(input('Valor para dopisitar: R$'))
        saldo += valor
        print(f'Depositado! Saldo atual: {saldo:.2f}')
    elif op == "2":
        valor = float(input('Valor para sacar: R$'))
        if valor <= saldo:
            saldo -= valor
            print(f'Saque realizdo com sucesso! Saldo atual: {saldo:.2f}')
        else:
            print("saldo insuficiente")
    elif op == "3":
        print(f"Saldo atual: R$ {saldo:.2f}")
    elif op == "4":
        print("obrigado po usar o nosso banco!")
        break
    else:
        print(" opção inválida!")