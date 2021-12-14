# Куда пойти - Москва глазами Артёма

Этот проект написан на Django для учебного приложения "Куда пойти".  
Готовый к использованию сайт можно посмотреть [здесь](https://coffeinik.pythonanywhere.com).

## Как запустить

* Скачайте код
* Выполните команды:
```sh
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ cp dev.env .env
$ python manage.py runserver
```
* Откройте `http://127.0.0.1:8000`.

Переменные окружения, необходимые для запуска в production-mode
* SECRET_KEY
* ALLOWED_HOSTS
* DATABASE_URL  

## Структура проекта и админка

На главной странице сайта выкачивается список интересных мест и рендерится в JSON:

```json
{
    "type": "FeatureCollection",
    "features": [
        {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [37.62, 55.793676]
        },
        "properties": {
            "title": "Легенды Москвы",
            "placeId": "1",
            "detailsUrl": "/places/1/"
        }
        },
        // ...
    ]
}
```

При выборе одного из мест выкачивается подробная информация об объекте.

```http
GET http://localhost:8000/places/1/
```

Ответ:
```json
{

    "title": "Заголовок",
    "imgs": [
        "/media/7a7631bab8af3e340993a6fb1ded3e73_AAsbIJX.jpg",
    ],
    "description_short": "Короткое описание",
    "description_long": "Длинное описание",
    "coordinates": {
        "lat": "55.77754550000010",
        "lng": "37.64912239999980"
    }

}
```

По адресу `http://localhost:8000/admin` можно перейти в панель администрирования Django.
Во вкладке Places есть возможность добавлять, изменять и удалять интересные места и прикладывать к ним фотографии.

Чтобы создать пользователя с правами администратора, необходимо исполнить команду
```sh
python manage.py createsuperuser
```

Для импорта данных из JSON с готовыми данными, необходимо воспользоваться командой load_place

```sh
./manage.py load_place "http://example.com/place.json'
```
 
По адресу http://example.com/place.json должны находиться тестовые данные в формате:
```json

{
    "title": "Заголовок",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1f09226ae0edf23d20708b4fcc498ffd.jpg",       
    ],
    "description_short": "Короткое описание",
    "description_long": "Длинное описание",
    "coordinates": {
        "lng": "37.50169",
        "lat": "55.816591"
    }
}

```
## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).