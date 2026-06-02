import random 

simbolos = ["👍","🐬","🫀","🏀","🍪"]
saldo = 20.0
print("=== Kassinão do Senai ===\n")
while saldo >= 2:
    input("\npressione ENTER para  girar (custa R$ 2)...")
    saldo -= 2

    resultado = [random.choice(simbolos) for _ in range(3)]
    print(" | ".join(resultado))

    if resultado[0] == resultado[1] == resultado[2]:
        premio = 20
        saldo += premio
        print(f" JACKPOT!!! Você ganhou R$ {premio}!")

    elif resultado[0] == resultado[1] or resultado[1] == resultado [2] or resultado[0] == resultado[2]:
        premio2 = 10
        saldo += premio2
        print(f" meio Jackpot!!! Você ganhou R$ {premio2}!")

    else:
        print("não foi dessa vez...")

        print(f"saldo atual: R$ {saldo:.2f}")