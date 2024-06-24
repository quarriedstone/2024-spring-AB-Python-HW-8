## ДЗ 8. Документация о проделанной работе
### Запуск приложения 
Настроим БД:
```bash
# Подтянем postgres контейнер
docker run --name seminar-postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres

# Создадим схему homework
docker exec -it seminar-postgres psql -U postgres
CREATE SCHEMA homework;

# Создадим таблицы
alembic -c homework/app/infrastructure/alembic.ini upgrade head
```
Для запуска приложения выполним следующую команду:
```bash
poetry run python3.10 -m homework.manage
```
### Запуск тестов
Для запуска тестов выполним следующую команду:
```bash
poetry run pytest
```
### Генерация автоклиента
Для удобства сгенерированный автоклиент лежит в репозитории. Как проходила генерация описано ниже.

Для начала возьмём документацию к написанному api с http://localhost:8000/openapi.json и положим ее в файл `swagger.json`.

Скачаем `openapi-generator-cli`:
```bash
wget https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/6.2.0/openapi-generator-cli-6.2.0.jar -O openapi-generator-cli.jar
```
Из директории со скачанным `openapi-generator-cli.jar` выполним команду для генерации автоклиента `gen`:
```bash
java -jar openapi-generator-cli.jar generate -g python -i /path/to/swagger.json -o /path/to/gen
```
Будем работать из-под виртуального окружения:
```bash
poetry shell
```
Установим сгенерированный клиент как библиотеку. Из директории `gen`:
```bash
pip install -e .
```
Теперь его можно использовать, просто написав `import openapi_client`!
