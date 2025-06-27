# 🔐 Log Analyzer SOC – Ferramenta de detecção de brute force com Python

Este projeto foi desenvolvido como parte do meu aprendizado e prática na área de **Cibersegurança**, simulando o comportamento de uma **ferramenta SOC básica** para detectar **tentativas de força bruta** por meio da análise de logs SSH.

---

## 🧰 O que a ferramenta faz

- Lê arquivos de log (`auth.log`) simulando logs do sistema
- Detecta tentativas de login com senha inválida via SSH
- Conta tentativas por IP
- Emite alertas se o IP ultrapassar o limite (default: 3 tentativas)
- Exporta os IPs suspeitos para `ips_suspeitos.txt`
- Possui interface interativa via terminal

---

## 🗂️ Estrutura do projeto

```
log-analyzer-soc/
├── core/
│   └── analyzer.py
├── data/
│   └── auth.log
├── output/
│   └── ips_suspeitos.txt
├── imagens/
│   └── execucao_log_parser.png
├── main.py
├── log_parser.py
└── README.md
```

---



## ▶️ Como executar

1. **Clonar o repositório**
```bash
git clone https://github.com/Bren04lv3s/log-analyzer-soc.git
cd log-analyzer-soc

python main.py

==== LOG ANALYZER SOC ====
1 - Analisar log de autenticação
2 - Ver IPs suspeitos detectados
3 - Limpar tela
0 - Sair