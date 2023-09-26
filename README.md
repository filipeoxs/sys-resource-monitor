# sys-resource-monitor


# Resource Monitor and Alert System

Este é um projeto de monitoramento de recursos do sistema e sistema de alerta por email desenvolvido em Python. Ele verifica continuamente o uso da CPU, memória e espaço em disco do sistema e envia alertas por email quando limites críticos são atingidos.

## Requisitos

Certifique-se de que você tenha Python instalado em seu sistema. Além disso, você precisará configurar as seguintes variáveis de ambiente:

- `REMETENTE_EMAIL`: Endereço de email do remetente.
- `SENHA_EMAIL`: Senha do remetente (recomenda-se o uso de uma senha de aplicativo).
- `DESTINATARIO_EMAIL`: Endereço de email do destinatário dos alertas.

## Uso

1. Clone o repositório:

   ```bash
   git clone https://github.com/filipeoxs/sys-resource-monitor.git
2. Instale as dependências:
   ```bash
    pip install psutil
3. Configure as variáveis de ambiente com suas credenciais de email.

4. Execute o script:
   ```bash
    python monitor.py

O script monitorará o uso de CPU, memória e espaço em disco e enviará alertas por email quando os limites definidos forem atingidos.
