from scripts.fuzz import *
from scripts.modules import *
from scripts.protocol_discover import protocol_discover

################### GLOBAL VARIABLES ###################
colorama.init(autoreset=True)
parser = argparse.ArgumentParser()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

######### Arguments ########
parser.add_argument('-t', '--target', required=False)
parser.add_argument('-st', '--showstatus', required=False, type=int, help='Show only the selected status code')
parser.add_argument('-sc', '--showchars', required=False, type=int, help='Show only the selected number of chars')
parser.add_argument('-w', '--wordlist', required=False, help='Specify the dictionary you want')
args = parser.parse_args()
############################

target = args.target
show_status = args.showstatus
custom_wordlist = args.wordlist
show_chars = args.showchars
########################################################

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

def def_handler(sig, frame):
    sys.exit(f'\n{gordo}{verde}Bye!')
signal.signal(signal.SIGINT, def_handler) # Ctrl+c

if target == None:
    print(f'{gordo}{rojo}ERROR{reset}{gordo} : You have to specify a target.')
    sys.exit(1)

if __name__ == '__main__':
    if custom_wordlist == None:
        custom_wordlist = 'directory-list-2.3-medium.txt'
    target = protocol_discover(target, custom_wordlist)
    print('ID\tRESPONSE\tWORDS\tCHARS\tREQUEST')
    fuzz(target, custom_wordlist, show_status, show_chars)