# Автотесты логина на saucedemo.com

Проект с автоматизированными тестами сценариев авторизации на сайте https://www.saucedemo.com/

## Установка и запуск

### Локально

1. Установка зависимостей:

```bash
pip install -r requirements.txt
```

2. Запуск тестов:

```bash
pytest
```

### В Docker

1. Сборка образа:
```bash
docker build -t saucedemo-tests .
```
2. Запуск тестов в контейнере:
```bash
docker run --rm saucedemo-tests
```