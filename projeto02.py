import pyautogui
import pyperclip
import webbrowser
import time
import yfinance

ticker = input("Digite o codigo da acao desejada: ")
dados_historicos = yfinance.Ticker(ticker).history(start="2023-01-01", end="2023-12-31")

fechamento = dados_historicos.Close

fechamento_minimo = round(fechamento.min(), 2)
fechamento_maximo = round(fechamento.max(), 2)
fechamento_medio = round(fechamento.mean(), 2)

destinatario = "adm.nas@hotmail.com"
assunto = "Analise de acoes no mercado financeiro"

mensagem = f"""
Prezado gestor financeiro,

Atendo sua solicitacao, seguem os resultados das analises sobre a acao {ticker}:

Valor maxima: R${fechamento_maximo}
Valor minima: R${fechamento_minimo}
Valor medio: R${fechamento_medio}

Para eventuais esclarecimentos estou a disposicao.

Atenciosamente,

Equipe sistemas analise de dados

"""

# abrir o navegador e ir para o gmail
webbrowser.open("www.gmail.com")
time.sleep(3)

# configurando uma pausa de 5 segundos
pyautogui.PAUSE = 3

# para clicar no botao escrever
pyautogui.click(x=72, y=201)

# digitar o email do destinatario e teclar TAB
pyperclip.copy(destinatario)
pyautogui.hotkey("cltr", "v")
pyautogui.hotkey("tab")

# digitar o assunto
pyperclip.copy(assunto)
pyautogui.hotkey("cltr", "v")
pyautogui.hotkey("tab")

# digitar a mensagem
pyperclip.copy(mensagem)
pyautogui.hotkey("cltr", "v")

# clicar no botao enviar
pyautogui.click(x=890, y=685)

# fechar o gmail
pyautogui.click("cltr", "f4")

print("Email enviado com sucesso")

