# Le fix me

## Installation

- pas de procédure d'installation
- pas de requirements.txt ou setup.py? Le site casse avec Django 1.11
- settings.py pas prêt pour un déploiement sur srvz
- gros mélange tabulation/espaces
- "/?q=..." dans les URL _ne_ peut _pas_ fonctionner
- pourquoi avoir django-markdown et django-markdownx?
- les répertoires media et static ne doivent pas être versionné
- à quoi sert django-markdown?

## Python

- plein d'URLs en dur.
- des classes nommées comme des fonctions
- plein de code commenté?
- des commentaires déconnectés du code
- pour afficher les liens suivant/précédant d'un article vous faites un `SELECT * FROM articles`. Puis idem avec les commentaires!!!
- `__unicode__` c'est du Python 2.

## HTML

- Markdown crée des titres h1, h2 par dessus les votres, du coup ça casse toute la logique de la page.
- pas de markdown dans les commentaires??

## UX

- template venant de chez bootstrap (Maquette)
- pas de filtre par mois, année, au autre (propre à un weblog)
- pas de création hors interface d'admin (why not)
- recherche non fonctionnelle
- Lorem Ipsum
- que fait ce lien "logout"?
- poster un commentaire renvoie sur la page d'accueil, dommage.
- ... c'est tout?

PS: wagtail!
