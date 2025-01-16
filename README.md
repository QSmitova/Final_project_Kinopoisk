# Final_project_Kinopoisk

## Диплом по автоматизированнуиу тестированию сервиса Кинопоиск

### Шаги
1. Склонировать проект 'git clone https://github.com/QSmitova/Final_project_Kinopoisk.git'
2. Установить зависимости
3. Запустить тесты 'pytest'
4. Сгенерировать отчет 'allure generate allure-files -o allure-report'
5. Открыть отчет 'allure open allure-report'

### Стек:
- pytest
- selenium
- requests
- allure
- configparser
- json
- quote
- os
- pathlib

### Струткура:
- ./test - тесты
- ./test_data - вводные данные (токен, логин, пароль)
- ./ui_pages - описание страниц
- ./api - хелперы для работы с API

### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore/)

### Библиотеки (!)
- pyp install pytest
- pip install selenium
- pip install webdriver-manager
- pip install allure-pytest