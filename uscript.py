#!/usr/bin/env python3

from time import sleep as sleep
import os

R = '\033[31;1m'  # Rojo
G = '\033[32;1m'  # Verde
Y = '\033[33;1m'  # A;1marillo
B = '\033[34;1m'  # Azul
M = '\033[35;1m'  # Magenta
C = '\033[36;1m'  # Cian
W = '\033[37;1m'  # Blanco
N = '\033[30;1m'  # Negro

# Negrita y subrayado
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

# Fondo
BG_R = '\033[41m'  # Fondo rojo
BG_G = '\033[42m'  # Fondo verde
BG_B = '\033[44m'  # Fondo azul

RESET = '\033[0m'  # Restablecer al estilo normal

_C = W
_B = C
_E = W

_T = f' {_B}[{_C}+{_B}]{_E}'
_A = f' {_B}[{_C}!{_B}]{_E}'
_Q = f' {_B}[{_C}?{_B}]{_E}'
_V = f' {_C}[{_B}*{_C}]{_E}'

_AUTOR = f'\t{_B}[{_C} Json Security{_B} ] {RESET}{_C}'
_GITHUB = f'\t{_B}[{_C} http://github.com/JsonSecurity{_B} ]{RESET}{_C}'
_SCRIPT = f'\t{_B}[{_C} Logo Flutter Changer{_B} ] {RESET}{_C}'

banner = f"""{_C}
                                    ...                            
                                .:odxxd:.                         
                                .ckOOkkkkx,                         
                            .okkkxxxxxd,                         
                            ;xxddddddxxo'                        
                            ;xxxkkOOOO0Ol'.                      
                            'cdOXXXNNNNNNNNNXOxc;;cclc:.            
            ..         .:xXNWNNNNNNNNNNNNNNWWWNXK0OOOx,           
            .lxxoc'.    :ONNNNNNNNNNNNNNNNNNNNNNNNNXKOkk:           
            ;xkkkOko, .oKNXK0OO00KXNXXKK00OO00KXNNNNNKOo.           
        .:xkkkkkkxokXK0kxddxkkkO0OOkkkkxdxkkO0XNNNN0:            
        'oxkkkkkkkk0XKOd:,cdldkkkkkkkkdc;oxodxkOXNXXXd.           
        'okkkkkkkkOKKOxc..',,cxxxxxkkxc,,::;:dxk0XXXX0;          {_AUTOR} 
        ,dkkkkxxxxOK0kd:....,oxxxxxxxxl;''',:dxxOKXXKKl          
        ;oddddooook00kxo:,,:ldddoooooddl:;;coddk0KKK00x;.        {_GITHUB} 
        .,;:::;,'ck0Oxdoooooolccc:::cloooooodxO00OOkOOko;.       
                    .oOOkxdooool;'..'',;lododdxkOOOkkkkkkkkxl.   {_SCRIPT}   
                    ,dkkkkkOkxdc,.',::lxkkOOOOOkddxkxxxxkxxxo.     
                    ,oxkOO0OkdolcccloddkO0K0Okdlcoxxxxxxxddx:     
                    .cdxxxkkxxdoooddxkkOOOOOxoc;coddodddood:     
                        .,cloodddxxxxxxxxxxxxddoc:,..',;:;'.'..     
                        .';:cllllloolooollllc:,.                  
                            ..,;::::::::::::;'.                    
                            .'''.......'''.                      
                            .''.       ..'.                      
                        .....','..      .'''....                  
                        .,,,,,'....      ..',,,,,'.                
                        .....            ......                  
                                                                    
    """

def bar(time=2, message='Loading', large=60):
    print('')
    porcentaje = 0
    bar = _B
    iteration = time / 100
    for p in range(101):
        i = int(large * (p/100))
        barra = '█' * i + '-' * int(large-i)
        
        print(f'\r{_E} {message}:{bar} [{barra}]{_E} {p:.2f}%', end='')
        #if p >= 80 :
        #    bar = _B
        #else:
        #    bar = R
        sleep(iteration)
    print('')

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
