from scripts.modules import *
from socket import gethostbyname, gaierror
from urllib3.exceptions import NewConnectionError

######### Colores ##########
reset = Style.RESET_ALL
gordo = Style.BRIGHT

rojo = Fore.RED
azul = Fore.BLUE
amarillo = Fore.YELLOW
verde = Fore.GREEN
cyan = Fore.CYAN
magenta = Fore.MAGENTA
############################

def fuzz(target, custom_wordlist, show_status, show_chars):
    cnt = 0
    with open(custom_wordlist, 'r') as wordlist:
        directory = wordlist.readlines()
        wordlist.close()
        for dir in directory:
            dir = dir.replace('\n', '')
            if not '#' in dir:
                r = requests.get(f'{target}/{dir}', verify=False)
                # Parameters
                id = cnt
                response = r.status_code
                word = len(r.text) # Count of words contained in the page
                chars = len(r.content) # Character count in the request
                request = f'"{dir}"'
                # Print the result
                if show_status == None and show_chars == None:
                    print(f'{id}:\t  {response}\t\t{word}\t{chars}\t{request}')
                    cnt += 1
                else:
                    if response == show_status and show_chars == None or show_status == None and chars == show_chars:
                        print(f'{id}:\t  {response}\t\t{word}\t{chars}\t{request}')
                    if response == show_status and chars == show_chars:
                        print(f'{id}:\t  {response}\t\t{word}\t{chars}\t{request}')
                        cnt += 1
                    else:
                        cnt += 1