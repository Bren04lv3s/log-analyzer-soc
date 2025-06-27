# 🔍 Analisador de Logs com Detecção de Brute Force 

Este projeto simula a leitura e análise de um log de autenticação (`auth.log`) para detectar tentativas de login suspeitas (como brute force) a partir de múltiplas falhas consecutivas de senha. Ele conta as tentativas por IP e exporta os que ultrapassam o limite para um arquivo `.txt`.


---

## ▶️ Como usar

1. Tenha o Python 3 instalado.
2. Adicione entradas simuladas no arquivo `auth.log` (exemplo incluso).
3. Rode o script no terminal:

```bash
python log_parser.py
