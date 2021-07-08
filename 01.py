'''
Objetivos:

1) Clicar no Try Again para continuar jogando.
2) Tentar outra técnica para conseguir uma pontuação maior.
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint
import time
browser = webdriver.Firefox(executable_path = 'geckodriver.exe')
browser.get('https://gabrielecirulli.github.io/2048/')


corpo_pagina = browser.find_element_by_tag_name('body')




# seleciona o jogo clicando na tela para poder enviar as teclas
browser.find_element_by_class_name('grid-container').click()

# fica enviado teclas para o jogo
while True:
	s = {0: Keys.UP, 1: Keys.RIGHT, 2: Keys.DOWN, 3: Keys.LEFT}
	for i in range(3):
		corpo_pagina.send_keys(s[i])
	time.sleep(0.5)
	try:
		browser.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div/a[2]').click()
	except:
		print('[erro] botão não encontrado')
	else:
		print('[ok] botão encontrado')

