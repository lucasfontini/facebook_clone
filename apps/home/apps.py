from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'

    # precisa indicar o caminho tbm 
    name = 'apps.home'
