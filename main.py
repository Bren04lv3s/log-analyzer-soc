# main.py

from core.analyzer import analisar_log
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    while True:
        print("\n==== LOG ANALYZER SOC ====")
        print("1 - Analisar log de autenticação")
        print("2 - Ver IPs suspeitos detectados")
        print("3 - Limpar tela")
        print("0 - Sair")

        escolha = input("\nDigite a opção desejada: ")

        if escolha == "1":
            log_path = "data/auth.log"
            output_path = "output/ips_suspeitos.txt"
            analisar_log(log_path, output_path, limite_tentativas=3)
        elif escolha == "2":
            try:
                with open("output/ips_suspeitos.txt", "r") as arquivo:
                    print("\n📄 IPs suspeitos detectados:")
                    print(arquivo.read())
            except FileNotFoundError:
                print("\n[!] Nenhum arquivo de saída encontrado.")
        elif escolha == "3":
            limpar_tela()
        elif escolha == "0":
            print("Encerrando o analisador...\n")
            break
        else:
            print("[X] Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()