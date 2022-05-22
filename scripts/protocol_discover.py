from scripts.modules import *

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

def protocol_discover(target, custom_wordlist):
    try:
        with open(custom_wordlist, 'r') as file:
            lines = len(file.readlines())
    except FileNotFoundError:
        print(f'{gordo}{rojo}ERROR{reset}{gordo} : File not found.')
        sys.exit(1)
    print(f'####################\n{gordo}{verde}Target{reset}{gordo} : {rojo}{target}{reset}')
    print(f'{gordo}{cyan}Protocol{reset}{gordo} : ', end='\r')
    if '://' in target:
        protocol = target.split('://')[0]
        if protocol == 'https':
            protocol = 'HTTPS'
        if protocol == 'http':
            protocol = 'HTTP'
        else:
            print(f'{gordo}{rojo}ERROR{reset}{gordo} : The protocol is not correct, make sure you use HTTP or HTTPS.')
            sys.exit(1)
    else:
        try:
            target = f'https://{target}'
            requests.get(target, timeout=2)
            protocol = 'HTTPS'
        except:
            target = target.replace('https://', 'http://')
            try:
                r = requests.get(f'{target}', verify=False)
                protocol = 'HTTP'
            except requests.exceptions.RequestException:
                raise SystemExit(f'{gordo}{rojo}ERROR{reset}{gordo} : The website does not exist or is not operational.')
    print(f'{gordo}{cyan}Protocol{reset}{gordo} : {magenta}{protocol}\n{reset}{gordo}{rojo}Wordlist{reset}{gordo} : {amarillo}{custom_wordlist}{reset}{gordo} [ {cyan}{lines}{reset}{gordo} ]\n{reset}####################\n')
    return target