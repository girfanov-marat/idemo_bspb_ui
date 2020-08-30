[![Build Status](https://travis-ci.org/girfanov-marat/idemo_bspb_ui.svg?branch=master)](https://travis-ci.org/girfanov-marat/idemo_bspb_ui)
# idemo_bspb_ui
Тестируемый ресурс https://idemo.bspb.ru/
# Итоговый проект
##### Используемый стэк: 
python + selenum + pytest + allure + travis ci

В качестве основоного шаблона проектирования был взят PageObject pattern
#### Написаны тесты на следующие разделы: 
- Счета
- Кредиты
- Вклады

Тест кейсы описаны в докстрингах тестовых методов.
### Установка

Необходимо установить все зависимости из requirements.txt

```sh
pip install -r requirements.txt
```

 ### Запуск

Необходимо установить все зависимости из requirements.txt
Перед запуском создайте виртуальное окружение

```sh
pip install virtualenv
virtualenv <env_name>
pytest
```
 ### Pre-commit-hooks
 Перед началом работы, необходимо выполнить команду
  ```sh
pre-commit install
```
для того, чтобы pre-commit запускался перед каждым коммитом

Принудительный запуск pre-commit:
 ```sh
pre-commit run --all-files
```
Запуск конкретного hook:
 ```sh
pre-commit run <hook_id>
```
 ### Allure
 #### Установка allure
 ##### Windows:
 Для генерации отчетов необходимо установить Scoop через PowerShell
 https://scoop.sh/
 
 После чего нужно выполнить команду 
  ```sh
 scoop install allure
 ```
 в окне PowerShell
 
 #### Генерация отчетов
 После прохождения тестов сформируется папка allure_result в корневой директории проекта
  
 Для генерации отчета необходимо ввести команду в окне PowerShell
 ```sh
 allure serve ${path}\tests\allure
 ```

