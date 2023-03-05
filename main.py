

from optparse import OptionParser
from os.path import isdir
from sys import platform
from os import system

# effacer l'ecran
def cls(): system('clear') if platform == "linux" else system('cls')
cls()

# section couleur
color = f'\x1b[38;5;{87}m'
gray = f'\x1b[38;5;{241}m'
no_color = '\x1b[37m'


__info__ = f'''{color}python main.py{gray} --help{color} cmd {no_color}| pour voir toute les commandes disponible
{color}python main.py {gray}--help{color} doc {no_color}| pour voir la documentation
{color}python main.py {gray}--help{color} depot {no_color}| pour consulter le depot github
{color}python main.py {gray}--help{color} version {no_color}| verifier la version 
'''
__doc__  = '''usage : cs script vous permet de bien debuter la creation de vos différents et magnifique sites

    command : 
        
        -c ou --path [ chemin du dossier ]
            si vous souhaiter initiliser ce script dans le dossier courant utiliser le symbole / 
            Ex :
                python main.py -c / 
                python main.py --path /main

        si vous souhaiter modifier le nom d'un fichier en particulier 
            --[html, css, js] [nouveau nom]
            Ex : python main.py --path / --html main

        pour ne pas creer un fichier en particulier
            --[html, css, js] [None]
            Ex : python main.py --path / --js None'''
__cmd__  = ''' -c/--path [chemin]
--help [cmd, doc, depot, version]
--html/--css/--js [nom/None]
'''
op  = OptionParser(__info__)

op.add_option('-c','--path',type='string',dest='ch',help='chemin') # chemin
op.add_option('--helps',type='string',dest='help',help='aide') # aide

# command epour changer les noms des différents fichiers
op.add_option('--html',type='string',dest='html',help='html')
op.add_option('--js',type='string',dest='js',help='javascript')
op.add_option('--css',type='string',dest='css',help='css')

res,nul = op.parse_args()
chemin = res.ch

def main(index = [],ch = ''):
    i = 0
    ch = ch+'\\' if ch else '' 
    for lang,value in extension.items():
        name = ch + index[i]
        with open(f'{name}.{lang}',"w") as file : file.write(value)
        i +=1

helps = {
    'cmd':__cmd__,
    "doc" : __doc__,
    'depot':'lien : github',
    'version':'1.001'
}

if res.help in list(helps.keys()):
    for cmd,doc in helps.items():
        if res.help == cmd:
            print(f'{cmd.upper():=^50} ')
            print(doc)
    pass

elif chemin and isdir(chemin):

    # verification des nom des fichier
    names = [res.html,res.css,res.js]
    for i in range(len(names)):
        if not names[i]: names[i] = 'index'
    

    data = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="{names[1]}.css">
</head>
<body>
    <!-- code ici -->
    <script src="{names[2]}.js"></script>
</body>
</html>'''
    
    extension = {
        'html' : data,
        'css' : "*{margin: 0;padding: 0;}",
        'js' :"console.log('bon codage a vous')"
    }

    if 'None' in names:
        ext = list(extension.keys())
        ext_sup = []
        for i in range(len(names)):

            if names[i] == 'None':
                del extension[ext[i]]
                ext_sup.append(ext[i])
            
        names = [i for i in names if 'None' != i]
        
        ext = list(extension.keys())
        if 'html' in ext:
            data = data.split('\n')

            for i in ext_sup:
                if i == 'css':data.pop(7)

                elif i == 'js':
                    for j in range(10,12):
                        if 'script' in data[j]: data.pop(j)
                        
            extension['html'] = "\n".join(data)
    
    
    if chemin ==  '/': main(names)

    else:main(ch=chemin,index=names)
                
    print('\x1b[32m[ True ]\x1b[37m')
else:print(f'{op.usage}')