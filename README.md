# Minecraft Bedrock Command Line Interface
Ce projet permet aux utilisateurs de générer des crafts, des quêtes et des constructions pour Minecraft Bedrock en utilisant l'API OpenAI. L'utilisateur peut interagir avec le programme via des options de menu.

# Prérequis
Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :

* Python 3.6 ou supérieur

* Les modules Python suivants :

``` os ```

```openai ```

```colorama ```

Vous pouvez installer ces modules en utilisant la commande suivante :

``` pip install openai colorama ```

# Configuration
1. Créez un fichier ```.env``` à la racine de votre projet et ajoutez-y votre clé API OpenAI :

```OPENAI_KEY=your_openai_api_key_here```

2. Chargez les variables d'environnement en ajoutant la ligne suivante dans votre script Python :

```load_dotenv()```

# Utilisation

Lancer le script ```main.py``` pour accéder au menu principal. Voici les fonctions principales :

```menu_menu()```
Affiche le menu principal et dirige l'utilisateur vers les options choisies:

* Craft : Permet de connaître le craft d'un item en interrogeant l'API OpenAI.

* Quest : Génère un défi avec un certain niveau de difficulté en interrogeant l'API OpenAI.

* Build : Génère des instructions pour construire une maison de taille et de style spécifiques en interrogeant l'API OpenAI.

* Help : Affiche l'aide des différentes fonctionnalités.

```menu_craft()```
Demande à l'utilisateur un craft et envoie l'entrée à OpenAI pour obtenir les instructions de craft.

```menu_quest()```
Demande le niveau de difficulté d'un défi et envoie l'entrée à OpenAI pour obtenir un défi original.

```menu_build()```
Demande la taille et le style d'une maison, et envoie l'entrée à OpenAI pour obtenir des instructions de construction.

```menu_help()```
Affiche les descriptions des différentes fonctions du programme.

```main()```
Fonction principale du programme qui lance le menu principal dans une boucle.

# Exemple

Voici un exemple de menu interactif :
```
Où voulez-vous aller ?
1. Craft
2. Quest
3. Build
4. Help

Veuillez entrer un numéro :
```
Les utilisateurs peuvent interagir avec ces options pour obtenir des informations sur le craft, les défis et les constructions dans Minecraft Bedrock.
