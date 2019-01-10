from .celery import *

broker_url = 'amqp://guest:guest@localhost:5672//'
result_backend = 'redis://localhost:6379/0'
if os.getenv('RABBIT_PORT') is not None and os.getenv('REDIS_PORT') is not None:
    broker_url = 'amqp://guest:guest@rabbit:5672'
    result_backend = 'redis://redis:6379/0'
    CELERY_ENABLED = True
    EVENTS_PUSH_BACKEND = "taiga.events.backends.rabbitmq.EventsPushBackend"
    EVENTS_PUSH_BACKEND_OPTIONS = {"url": "amqp://guest:guest@rabbit:5672//"}
