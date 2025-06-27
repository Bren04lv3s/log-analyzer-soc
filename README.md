# 🔍 Analisador de Logs com Detecção de Brute Force – Projeto SOC Júnior

Este projeto simula a leitura e análise de um log de autenticação (`auth.log`) para detectar tentativas de login suspeitas (como brute force) a partir de múltiplas falhas consecutivas de senha. Ele conta as tentativas por IP e exporta os que ultrapassam o limite para um arquivo `.txt`.

✅ Ideal para quem está iniciando na área de **cibersegurança**, **monitoramento de logs** e **lógica de correlação usada em SOCs (Security Operations Center)**.

---

## ▶️ Como usar

1. Tenha o Python 3 instalado.
2. Adicione entradas simuladas no arquivo `auth.log` (exemplo incluso).
3. Rode o script no terminal:

```bash
python log_parser.py