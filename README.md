# Task_Manager_Final

- Intégrer des fichiers static :
  (Ex beau formulaire, formulaire de connexion)

  - django-contrib-staticfiles
    - STATIC_ROOT (chemin du dossier où y'a les statics) --> os.path.join(BASE_DIR, 'static_collect')
    - STATICFILE_DIR = [os.path.join(BASE_DIR, library/static)]
    - Tag pour appeler dans les templates : {% static 'logo.png' %} avec en haut {% load static %}
    - il faut aussi faire un ./manage.py collectstatic
