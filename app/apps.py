from django.apps import AppConfig
from django.core.management import call_command


class AppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app"

    # def ready(self):
    #     try:
    #         print('Start migration')
    #         call_command('makemigrations', interactive=False)
    #         call_command("migrate", interactive=False)
    #         print("Migration was executed successfully.")
    #     except Exception as e:
    #         import logging
    #         logging.exception(f'Error migration: {e}')
