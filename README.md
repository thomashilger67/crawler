# crawler
petit projet pour le cours d'indeation web ENSAI 3A SID fait par Thomas Hilger. Le but est de coder un single-threaded crawler.

## Quickstart 
d'abord, assurez-vous d'avoir l'ensemble des dépendances :  executez à la racine du projet la commande `pip install -r requirements.txt`.
Pour lancer le crawler, il suffit de lancer à la racine du projet la commane `python main.py`

## Explication 

Le crawler est codé dans la fonction mycrawler. les grandes étapes sont :

- on requête l'url d'origine 
- on récupère l'ensemble des liens url disponibles sur ce document.
- pour chaque lien trouvé, on consulte son robots.txt pour connaître les règles de politesse. Si l'on peut crawler le site, on le télécharge puis on passe au prochain lien après 5 seconde d'attente, sinon on passe au prochain lien après 5 secondes d'attente.
- on s'arrête au bout de 50 url téléchargés ou s'il n'y a plus de lien à crawler.
