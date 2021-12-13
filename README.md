# Куда пойти - Москва глазами Артёма

Этоn проект написан на Django для учебного приложения "Куда пойти".  


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
## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).