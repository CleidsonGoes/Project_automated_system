# crie um ambiente virtual

Crie um ambiente virtual e instale o pyautogui e pandas dentro dele. Isso isola o ambiente de desenvolvimento e evita conflitos com o sistema.

# Crie um ambiente virtual:
bash

python3 -m venv venv

## Ative o ambiente virtual:
# No Linux Ubuntu:
bash

source venv/bin/activate

# Instale o pyautogui e pandas:
bash

pip install pyautogui
pip install pandas

# Execute seu script dentro do ambiente virtual.