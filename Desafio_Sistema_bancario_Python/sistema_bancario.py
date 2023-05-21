menu = """

[1] Deposito
[2] Saque
[3] Extrato
[4] Finalizar

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
vlr_diario = 0
limite_vlr_diario = 1500
saque_ralizado = 0
deposito = 0
tot_saque = 0


while True:
    
    opcao = int(input(menu))
    
    if opcao == 1:
        
        while True:
        
            vlr_deposito = int(input("Digite o valor a ser depositado: "))         
       
            if vlr_deposito <= 0:
                print("Valor inválido, digite um valor positivo.\n")
                
            else:
                print(f"\nDepósito de R$ {vlr_deposito:.2f} efetuado com sucesso!\n")
                saldo = saldo + vlr_deposito
                deposito = deposito + vlr_deposito
                print(f"Saldo atual de R$ {saldo:.2f}.")
                break    
        
    elif opcao == 2:
        print("Saque")
        
        while True:
            
            vlr_saque = int(input("Digite o valor desejado para saque: "))
            
            if vlr_saque <= saldo:
                
                if vlr_saque < 500.00:
                                        
                    if numero_saques <= LIMITE_SAQUES:
                                            
                        if (vlr_diario + vlr_saque) < limite_vlr_diario:
                           saldo = saldo - vlr_saque
                           numero_saques = numero_saques + 1
                           tot_saque = tot_saque + vlr_saque
                           
                           print(f"Saque no valor de R$ {vlr_saque:.2f} realizado com sucesso!\nNovo saldo bancário é de R$ {saldo:.2f}.")
                           
                        else:
                            print("\nValor diário de saque excedido.")    
                            break
                    else:
                        print("Limite de saques diários excedidos!")     
                        break
                else:
                    print("\nValor desejado é maior que o limite para saque.")
                    break
            else:                    
               print("\nSaldo Insuficiente.") 
               break          
    
            
    elif opcao == 3:
        print("************  Extrato  ************\n")
        if deposito > 0:
           print(f"Depósito(s) realizados : R$ {deposito:.2f}")
           
           if tot_saque > 0:
                  print(f"Saque(s) realizado(s)  : R$ {tot_saque:.2f}")           
            
        else:
            print(f"Não há movimentações para serem apresentadas.\n")
        
        print(f"\nSaldo Atual            : R$ {saldo:.2f}")
        
    
    elif opcao == 4:
        print("Obrigado por utilizar nossos serviços!")
        break
    
    else:
        print("Opção inválida, escolha novamente a opção desejada.") 