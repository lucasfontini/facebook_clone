from celery import shared_task

@shared_task
def minha_tarefa():
    for i in range(0-100):
        print("celery funcionando ", i )
    return f"terminou"