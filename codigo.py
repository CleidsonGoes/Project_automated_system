# Passo 1: Entrar no sistema da empresa
# - https://dlp.hashtagtreinamentos.com/python/intensivao/login

# Instalar o pyautogui para controlar o mouse e teclado para automatizar

import pyautogui
import time
import pandas

# pyautogui.write -> escrever um texto
# pyautogui.click -> clicar com o mouse
# pyautogui.press -> apertar uma tecla
# .hotkey -> para gel.gracy@gmail.com    um atalho de teclado

# abrir o navegador
pyautogui.PAUSE = 1  # pausa em segundos(s) para executar cada comando
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(3)
# acessar o sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
pyautogui.press("F11")

time.sleep(3)  # para pausa em certo momento

# fazer login
# digitar email
pyautogui.click(x=502, y=297)
pyautogui.write("jorgegoes4@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(1)

# Passo 3: Importar a base de dados

tabela = pandas.read_csv("produtos.csv")

# Passo 4: Cadastrar um produto

pyautogui.click(x=546, y=173)
pyautogui.write("Sabonete")
pyautogui.press("tab")
pyautogui.write("Avon")
pyautogui.press("tab")
pyautogui.write("liquido")
pyautogui.press("tab")
pyautogui.write("higiene")
pyautogui.press("tab")
pyautogui.write("1.10")
pyautogui.press("tab")
pyautogui.write("0.60")
pyautogui.press("tab")
pyautogui.write("pouco estoque")
pyautogui.press("tab")
pyautogui.press("enter")
# Passo 5: Repetir o processo de cadastro até acabar os produtos
