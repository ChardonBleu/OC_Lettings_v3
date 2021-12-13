## Résumé


![Docker Image Version (latest by date)](https://img.shields.io/docker/v/bleudecampan/oc_lettings?label=latest_docker_image)
![CircleCI](https://img.shields.io/circleci/build/github/ChardonBleu/oc_lettings/master?token=780d03a1061212406396dd2462d5cfd6ace8922f)  
![GitHub repo size](https://img.shields.io/github/repo-size/ChardonBleu/oc_lettings?color=informational)
![GitHub last commit](https://img.shields.io/github/last-commit/ChardonBleu/oc_lettings)



![Epicevent logo](https://user.oc-static.com/upload/2020/09/18/16004295603423_P11.png "Epicevent logo")



Projet 13 de la formation DA python d'Openclassrooms.  
Site web d'Orange County Lettings. Mise en place d'un pipeline CI/CD avec Circleci et Heroku

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/ChardonBleu/oc_lettings.git`

#### Créer l'environnement virtuel

- `cd /path/to/oc_lettings`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Variables d'environnement

- Renommer le fichier .env_exemple en .env
- Dans ce fichier renseigner votre DSN Sentry pour un logging du projet en developpement.

#### Exécuter le site

- `cd /path/to/oc_lettings`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/oc_lettings`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/oc_lettings`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/oc_lettings`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(<Nom table>);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`      


## Utilisation locale de l'application avec Docker

### Prérequis

- Repository cloné en local
- Docker

Si ce n'est pas déjà fait, installer Docker: `https://docs.docker.com/get-docker/`.  
Sur Linux, installer également Docker Compose (il est compris dans Docker Desktop pour Mac et Windows):  `https://docs.docker.com/compose/install/ `.

### Windows

Attention: sur windows il faut au préalable avoir activé WSL2 (sous-système linux). Il faut aussi activer Hyper-V backend, ce qui nécessite Windows10 pro ou Windows11 pro. `https://docs.docker.com/desktop/windows/install/`.

Dans VSCode installer les extensions Remote Development et Docker.

Ouvrir le projet necessitant Docker dans VSCode. Le terminal propose alors un powershell et il apparait alors un nouveau petit rectangle coloré en bas à gauche.    
![Alt text](readme_img/VSCode_windows.jpg?raw=true "Projet ouvert dans VSCode avec windows")  
En cliquant sur ce retangle on peut réouvrir ce projet dans wsl.  
Le terminal propose alors un bash linux.  
  
![Alt text](readme_img/VSCode_folders.jpg?raw=true "Projet ouvert dans VSCode avec ubuntu de wsl2")  

En allant dans Fichier --> Ouvrir le dossier ... on peut naviguer dans tous les répertoires, y compris ceux du sous-système Linux.

Un bash Ubuntu est également disponible dans les applications:  

![Alt text](readme_img/bash_Ubuntu.jpg?raw=true "Bash Ubuntu") 

### Faire tourner l'application locale dans un conteneur  

Dans un terminal se mettre dans le répertoire racine de l'application (celui contenant les fichiers Dockerfile et docker-compose.yml) et lancer le conteneur:  
`docker-compose up`  
L'application est alors disponible en local sur `localhost:8000`.

## Pipeline CI/CD CircleCI avec déploiement sur Heroku

### Prérequis


- Compte GitHub avec accès en lecture au repository de l'application.
- Compte DockerHub avec un dépot public.
- Compte Circleci avec un projet lié au dépot GitHub de l'application.
- Compte Heroku.
- Compte Sentry avec un projet pour cette application.

Récupérer sur DockerHub l'acces Token et le noter.  
Récupérer sur Heroku l'API Key dans les settings de votre compte Heroku.  
Récupérer le DSN du projet Sentry.  

Si les données ont été modifiées localement, il est possible de les sauvegarder afin de pouvoir les charger dans la base de données de production à l'issue du déploiement:
`python manage.py dumpdata > dumps/data.json`  

Dans le terminal créer un nouveau projet Heroku:
`heroku apps:create <nom de mon app>`

Dans les settings de CircleCI ajouter les variables d'environnement nécessaires pour le pipeline:  

![Alt text](readme_img/var_env_circleci_2.jpg?raw=true "Projet ouvert dans VSCode avec ubuntu de wsl2")  

DOCKER_LOGIN correspond à votre username sur DockerHub.  
DOCKER_PASSWORD correspond à votre Token acces sur DockerHub.  
HEROKU-API_KEY est l'API Key récupérée sur votre compte Heroku.  
HEROKU_APP_NAME est le nom que vous avez choisi pour votre application sur Heroku.  
SECRET_KEY est la secret key de production de settings.py de l'application Django.  
SENTRY_DSN est le DSN de votre projet Sentry.

Faire une modification dans un fichier de l'application dans une nouvelle branche.  
Pousser cette branche sur GitHub. Le pipeline lance le contrôle des tests et du linting.  
Si les tests passent, merger cette branche dans master puis pousser master sur le repository GitHub.  
Le pipeline exécute alors la conteneurisation puis le déploiement si la conteneurisation passe.
La dernière image taguée avec le SHA1 du commit CircleCI est sauvegardée sur DockerHub.

![Alt text](readme_img/Pipeline_deploy.jpg?raw=true "Projet ouvert dans VSCode avec ubuntu de wsl2") 

Le site est alors disponible sur Heroku:  
https://<nom_de_mon_app>.herokuapp.com/

Juste après déploiement il est possible de créer un nouveau superuser:  
`heroku run python manage.py createsuperuser`

Les données peuvent enfin être chargée dans le base de données de production:  
`heroku run python manage.py loaddata dumps/data.json`

Il est possible, dans un terminal, de lancer en local le conteneur du DockerHub avec la dernière image taguée:  
`docker run -d -p 8000:8000 <votre user name docker>/<nom du depot>:<SHA1>`  


Ressources utilisées
---

Ressources web:

La documentation officielle de Docker:

- https://docs.docker.com/compose/install/  

- https://testdriven.io/blog/docker-best-practices/

Le cours Openclassrrom:  

- https://openclassrooms.com/fr/courses/2035766-optimisez-votre-deploiement-en-creant-des-conteneurs-avec-docker

- https://openclassrooms.com/fr/courses/2035736-mettez-en-place-lintegration-et-la-livraison-continues-avec-la-demarche-devops

Les vidéos de Thierry Chappuis:

- Fondamentaux et bonnes pratiques pour dockeriser votre application django: https://www.youtube.com/watch?v=R3FBAE_LQ7E

- Déployer votre application sur Heroku: https://www.youtube.com/watch?v=nkw6OIaD-7Y&t=145s et https://www.youtube.com/watch?v=iAw8KfCiNoE&t=610s

Autres vidéos:

- Pycon'21 SPONSOR WORKSHOP / Angel Riviera / CircleCl:  https://www.youtube.com/watch?v=WMQvbD0Rdv4

- CI/CD | Continuous integration tutorial: https://www.youtube.com/watch?v=jzir3eYCCw4

La documentation  de Circleci:

- https://circleci.com/blog/django-deploy/

- https://circleci.com/blog/continuous-integration-for-django-projects/

- https://circleci.com/docs/2.0/env-vars/

- https://circleci.com/developer/orbs/orb/circleci/heroku

La documentation officielle de Heroku:

- https://devcenter.heroku.com/articles/heroku-cli

- https://devcenter.heroku.com/articles/heroku-cli-commands

- https://devcenter.heroku.com/articles/django-app-configuration

- https://devcenter.heroku.com/articles/django-assets


Remerciements:
---

Dernier projet de ce parcours de formation. L'aventure ne fait que commencer je l'espère.  
Un immense merci à mes trois mentors successifs Aurélien Massé, Thierry Chappuis et Sandrine Suire pour la transmission de leur savoir, leur accompagnement et leur patience.

Et un grand merci à tous les membres du Discord DA python: 
http://discord.pythonclassmates.org/
