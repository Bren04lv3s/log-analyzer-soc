<<<<<<< HEAD
from collections import defaultdict

def analisar_log(nome_arquivo, limite_tentativas=3):
    tentativas = defaultdict(int)
    ips_suspeitos = set()

    try:
        with open(nome_arquivo, 'r') as log:
            for linha in log:
                if "Failed password" in linha:
                    partes = linha.strip().split()
                    ip = partes[-4]  # Pega o IP que aparece antes de 'port'
                    tentativas[ip] += 1

                    print(f"[!] Falha detectada do IP {ip} ({tentativas[ip]} tentativa(s))")

                    if tentativas[ip] == limite_tentativas:
                        print(f"[ALERTA] IP {ip} atingiu o limite de {limite_tentativas} tentativas!")
                        ips_suspeitos.add(ip)

        if ips_suspeitos:
            with open("ips_suspeitos.txt", "w") as saida:
                for ip in ips_suspeitos:
                    saida.write(f"{ip} - {tentativas[ip]} tentativas\n")
            print("\n📄 IPs suspeitos salvos em ips_suspeitos.txt")
        else:
            print("\n✅ Nenhum IP ultrapassou o limite.")

    except FileNotFoundError:
        print(f"[ERRO] Arquivo {nome_arquivo} não encontrado.")
    except Exception as e:
        print(f"[ERRO] Ocorreu um problema: {e}")

if __name__ == "__main__":
=======
from collections import defaultdict

def analisar_log(nome_arquivo, limite_tentativas=3):
    tentativas = defaultdict(int)
    ips_suspeitos = set()

    try:
        with open(nome_arquivo, 'r') as log:
            for linha in log:
                if "Failed password" in linha:
                    partes = linha.strip().split()
                    ip = partes[-4]  # Pega o IP que aparece antes de 'port'
                    tentativas[ip] += 1

                    print(f"[!] Falha detectada do IP {ip} ({tentativas[ip]} tentativa(s))")

                    if tentativas[ip] == limite_tentativas:
                        print(f"[ALERTA] IP {ip} atingiu o limite de {limite_tentativas} tentativas!")
                        ips_suspeitos.add(ip)

        if ips_suspeitos:
            with open("ips_suspeitos.txt", "w") as saida:
                for ip in ips_suspeitos:
                    saida.write(f"{ip} - {tentativas[ip]} tentativas\n")
            print("\n📄 IPs suspeitos salvos em ips_suspeitos.txt")
        else:
            print("\n✅ Nenhum IP ultrapassou o limite.")

    except FileNotFoundError:
        print(f"[ERRO] Arquivo {nome_arquivo} não encontrado.")
    except Exception as e:
        print(f"[ERRO] Ocorreu um problema: {e}")

if __name__ == "__main__":
>>>>>>> d829b555ca599f078f1bd86ef8b4bed0dbbbabb7
    analisar_log("auth.log", limite_tentativas=3)