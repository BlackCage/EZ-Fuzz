# EZ Fuzz

> ***EZ Fuzz*** es una herramienta creada en Python que permite realizar fuzzing sobre una web de una manera rápida y sencilla.
## Instalación
```bash
# Clonar el repositorio
git clone https://github.com/BlackCage/EZ-Fuzz
# Movernos al directorio
cd EZ-Fuzz/
# Iniciamos el script para instalar los módulos necesarios
python3 ezFuzz.py
```
## Uso
- **-t**, **--target**
	- Especifica una URL para comenzar a fuzzear.
		- `python3 ezFuzz.py -t https://google.es`
	
- **-w**, **--wordlist**
	- Especifica el diccionario que deseas utilizar.
		- `python3 ezFuzz.py -t https://google.es -w wordlist.txt`
	
- **-st**, **--showstatus**
	- Filtra solo por el código de estado que tú quieras.
		- `python3 ezFuzz.py -t https://google.es -w wordlist.txt -st 200`
	
- **-sc**, **--showchar**
	- Filtra solo por el número de caracteres que tú quieras.
		- `python3 ezFuzz.py -t https://google.es -w wordlist.txt -sc 10650`

## Combinaciones
Sí, puedes combinar las opciones, es decir, puedes filtrar por código de estado y caracteres al mismo tiempo, aunque hay algunas que **no están permitidas**.
### NO PERMITIDAS
- `python3 ezFuzz.py`
	- A no ser que sea la primera vez para instalar los módulos necesarios dará error, ya que no se ha especificado ningún objetivo.
 
## ¿Dónde funciona?
|    OS   |   Tested   |
|:-------:|:----------:|
| Linux   |      ✔️     |
| Windows |      ✔️     |
| Mac     | Not Tested |

___

###### Versión : 0.0.1
