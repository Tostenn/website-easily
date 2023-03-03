# Start your website more easily

**ce dépôt** a été conçu pour faciliter et rendre plus dynamique le début de vos différents et merveilleux projets web. Je m'explique, avant de commencer à matérialiser votre projet web vous devez exécuter une série de tâches très pénibles qui commence par la création des fichiers HTML, CSS, JS et ensuite écrite la structure minimale du HTML enfin après cette étape vous devez encore relier c'est différents fichiers entre eux, et là vous vous dit mais tout ça, ça prend du temps moi je veux commencer mon projet toute suite puis soudain vous vous demandez **comment faire pour automatiser ces étapes ?** et à ne plus s'en soucier. Alors si c'est cela votre préoccupation ne vos inquiets par je vais vous aider à surmonter cette étape lisser attentivement la suite de la documentation à la fin de cela vous serait capable de commencer votre projet web en un clic

# Prérequis
+ `Pyhon`
- `module`<br>

   ![](https://raw.githubusercontent.com/Tostenn/Tostenn/main/module_web.png)
> `NB` :  tous les modules utilisés ici sont présents nativement dans python alors pas besoin d'installation

# Installation
+ ## Window
```window
git clone https://github.com/Tostenn/country_capital.git
cd country_capital
python main.py --path /
```
+ ## Linux 
```bash

git clone https://github.com/Tostenn/country_capital.git
cd country_capital
chmod +x *
python main.py -c /

```
# Syntasx
+ _commande d'aide_
```
python main.py --help cmd     | pour voir toute les commandes disponible
python main.py --help doc     | pour voir la documentation
python main.py --help depot   | pour consulter le depot github        
python main.py --help version | verifier la version
```
+ chemin

**`python main.py  -c/--path [chemin]`** Cette commande permet de spécifier le chemin d'initialisation du projet si vous souhaitez initialiser votre projet dans le répertoire courant `/` après la commande <br>
_exemple d'utilisation pour le dossier courant_
```
python main.py --path /
```
+ renommage
--**`html, css, js`** vous permet de modifier les noms des différents fichiers ou de ne pas créer ce fichier avec les mots-clés **`None`**
> **`NB`** par défaut tous les fichiers sont renommés **`index`**
```
python main.py -c / --html main --css style --js None
```
> **`explication`** d'abord nous avons choisi d'initialiser notre projet dans le répertoire courant ensuite nous avons renommé le fichier HTML en maints Puid fichier Css en style et pour finir nous avons utilisé les mots-clés None pour le js ce qui signifie que nous ne voulons pas créer de fichier Javascript

## structure minimal du HTML et relier les diférents fichiers
**`automatique`** et oui on rentre dans la phase automatique du script et ne vous s'en fait pas à ce niveau tout le travail a été déjà fait plus besoin de taper de commande lorsque nous avons tapé cette commande **`python main Py-path /`** automatique il a créés nos différents fichiers et les est relié automatiquement ce n'est pas génial ça il s'est pass' la même chose lorsqu'on a tapé **`python main py -c / --html main --css style --js Nenone`** mais avec une légère différence comme n'a pas créé de fichier Javascript c'est inutile de créer une balise <script> et donc de la cour pas de bug vous vous demander est-ce que ça marche aussi avec le Css et bien que oui si vous décidez de ne créer que les fichiers HTML et Javascript automatique il les relie et n'implique pas la balise <lienk/>


+ _Exemple_
```
python main.py --path /
python main.py --path / --html None
python main.py --help version
```
# ce depot
 
> **__Toute amélioration sera la  `BIENVENUE`__** <br>
> **le script sera diponible le `7 mars à 00h00`**<br>
>**email _`kouyatosten@gmail.com`_**<br>
> **Statut :  `en cour`**
