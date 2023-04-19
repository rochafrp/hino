import os
def menu():
    while True:
        os.system("cls||clear")
        print("\n----------------------------------------\n--Escolha o hino do seu time do coração!--\n------------------------------------------\n(1) América\n(2) Botafogo\n(3) Flamengo\n(4) Fluminense\n(5) Vasco da Gama\n(6) Sair")
        try:
            opcao = int(input("\nQual hino?"))
            hino = ""  
            if opcao == 1: hino = "america"
            elif opcao == 2: hino = "botafogo"
            elif opcao == 3: hino = "flamengo"    
            elif opcao == 4: hino = "fluminense"
            elif opcao == 5: hino = "vasco"
            elif opcao == 6:
                print("Programa encerrado.")
                break
            else:
                print("[ERRO] Essa opção é não existe.")
                continue
            with open(f"{hino}.txt","r",encoding="UTF-8") as file:
                os.system("cls||clear")
                print(file.read())
                print("\nPressione ENTER para uma nova opção")
                input()
        except:
            os.system("cls||clear")
            print("[ERRO] Favor digitar apenas números!")
            input()
if __name__ == "__main__":
    menu()
    