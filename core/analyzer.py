# core/analyzer.py

from collections import defaultdict
import os

def analisar_log(caminho_log, caminho_saida, limite_tentativas=3):
    tentativas = defaultdict(int)
    ips_suspeitos = set()

    if not os.path.exists(caminho_log):
        print(f"[ERRO] Arquivo de log não encontrado: {caminho_log}")
        return

    try:
        with open(caminho_log, 'r') as log:
            for linha in log:
                if "Failed password" in linha:
                    partes = linha.strip().split()
                    ip = partes[-4]
                    tentativas[ip] += 1

                    print(f"[!] Falha detectada do IP {ip} ({tentativas[ip]} tentativa(s))")

                    if tentativas[ip] == limite_tentativas:
                        print(f"[ALERTA] IP {ip} atingiu o limite de {limite_tentativas} tentativas!")
                        ips_suspeitos.add(ip)

        if ips_suspeitos:
            with open(caminho_saida, 'w') as saida:
                for ip in ips_suspeitos:
                    saida.write(f"{ip} - {tentativas[ip]} tentativas\n")
            print(f"\n📄 IPs suspeitos salvos em {caminho_saida}")
        else:
            print("\n✅ Nenhum IP ultrapassou o limite de tentativas.")

    except Exception as e:
        print(f"[ERRO] Ocorreu um problema ao analisar o log: {e}")