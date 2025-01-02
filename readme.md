Запуск redis
```bash
docker start my-redis
```
Запуск celery-worker
```bash
celery -A celery_app worker --loglevel=info
```
Запуск celery-beat
```bash
celery -A celery_app beat --loglevel=info
```
Запуск flower
```bash
celery -A celery_app flower
```