# Обрезка ссылок с помощью Битли

Cкрипт сокращает ссылки через сервис [bit.ly](https://bitly.com).

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Для работы скрипта требуется зарегистрироваться в сервисе [bit.ly](https://bitly.com),
по [ссылке](https://bitly.com/a/oauth_apps) необходимо сгенерировать токен вида `17c09e20ad155405123ac1977542fecf00231da7`.

После получения токена необходимо в папке с `main.py` создать файл `.env` с кодом
```python
BITLY_TOKEN='ВАШ_ТОКЕН'
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).