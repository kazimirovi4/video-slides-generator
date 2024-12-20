# Video Slides Generator

Приложение для автоматического создания слайдов из видеофайлов. Генерирует объединённое изображение с ключевыми кадрами видео, где количество слайдов определяется длительностью видео.

## Возможности

- Автоматический выбор ключевых кадров в зависимости от продолжительности видео.
- Генерация одного изображения с объединёнными кадрами.
- Удобный графический интерфейс, позволяющий выбрать видео и папку для сохранения.

## Как это работает

Количество слайдов определяется следующим образом:
- Более 10 минут: 5 слайдов.
- От 5 до 10 минут: 4 слайда.
- От 2 до 5 минут: 3 слайда.
- 1 минута и менее: 2 слайда.

Кадры выбираются из видео равномерно, чтобы охватить весь временной промежуток.

## Установка

### 1. Клонирование репозитория
Склонируйте проект с помощью Git:

    git clone https://github.com/kazimirovi4/video-slides-generator.git

    cd video-slides-generator

### 2. Установите зависимости:
Убедитесь, что у вас установлен Python версии 3.8 или выше. Установите зависимости:

    pip install -r requirements.txt

## Использование

### 1. Запустите приложение:

для Windows:

    python main.py

для Linux и MacOS:

    python3 main.py    

### 3. Выберите видеофайл, нажав кнопку "Выбрать видео".

### 4. Укажите папку для сохранения результата, нажав кнопку "Выбрать папку".

### 5. Нажмите кнопку "Сгенерировать файл". После завершения программа сообщит о сохранении файла.

