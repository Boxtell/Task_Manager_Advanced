# Task_Manager_Final

- Intégrer des fichiers static :
  (Ex beau formulaire, formulaire de connexion)

  - django-contrib-staticfiles
    - STATIC_ROOT (chemin du dossier où y'a les statics) --> os.path.join(BASE_DIR, 'static_collect')
    - STATICFILE_DIR = [os.path.join(BASE_DIR, library/static)]
    - Tag pour appeler dans les templates : {% static 'logo.png' %} avec en haut {% load static %}
    - Il faut aussi faire un ./manage.py collectstatic
    - Et mettre todolist en premier dans INSTALLED_APP
 
 Intégrer des media au projet :
    -Creer un dossier media (qui va se remplir avec les fichier upload par le user)
    - Si formualire avec fichier : Dans le tempalte mettre --> enctype= multi je sais pas quoi
    
 Deploiement:
  - WSGI (interface django serveur) --> Nombre fixe de worker, les utilisateurs font la queue pour faire leur requete sur un worker                        
    libre
  -Utiliser Gunicorn pour déployer sur serveur
  -Astuce pip freeze : pip freeze > requirements.txt
  
 Mettre des messsages sur différentes actions :
  - message.info("une tache crée") puis passer au context puis importer dans le template
    
 
