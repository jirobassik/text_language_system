# Многофункциональная система по автоматическому анализу текста и языка
## Возможности системы
1. Пользователь
    1. Регистрация
    2. Вход
    3. Вход через сторонние сервисы (Google, Github)
    4. Подтверждение почты
    5. Сброс пароля
    6. Восстановление пароля
    7. Изменение учетных данных
2. Работа с текстом и языком
    1. Ввод текста
       1. Через форму
       2. Загрузка файла
          1. Валидация файла
             1. Проверка расширения
             2. Проверка на тип файла
             3. Проверка размера файла
    2. Определение языка текста (short_word_method, langid, langdetect)
        1. Для short_word_method доступно добавление собственных языков через административную панель
    3. Реферирование текста (extractive_plus, pysummarizer)
    4. Определение тем текста (zero-shot-classification--facebook/bart-large-mnli)
    5. Извлечение ключевых слов текста (yake)
    6. Извлечение именованных сущностей (spacy)
    7. Определение тональности (textblob)
4. Долгая задача (только для определения тем текста)
   1. Просмотр истории долгих задач
   2. Просмотр статуса выполнения долгих задач
   3. Постановка в очередь долгих задач
5. API
   1. Создание ключа
   2. Удаление ключа
   3. Доступ к API только по ключу
   4. Документация: swagger, redoc
   5. Доступ ко всему функционалу из пункта 2, 3 удаленно
6. Дополнительно
   1. Сохранения результата в формате JSON
   2. Периодическая очистка истории и статуса
   3. Периодическая очистка просроченных ключей сессии
