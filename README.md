# 21.2-Basics-of-layout(Основы верстки)
# Установлены все зависимости
"""
python -m venv venv  # Создание окружения
.\venv\Scripts\Activate  # Активация окружения
echo "venv/" >> .gitignore
echo "__pycache__/" >> .gitignore
echo ".env" >> .gitignore
pip install -r requirements.txt
poetry install
poetry init
git config --global core.autocrlf false
Это предотвратит автоматическую замену LF → CRLF

"""
# Собраны все страницы макета
"""
Страница «Главная» собрана по макету.
Страница «Каталог» собрана по макету.
Страница «Категория» собрана по макету.
Страница «Контакты» собрана по макету.
На страницах используются стили Bootstrap.
"""
# Задание 2
"""
На основе получившейся верстки веб-приложение,
будет на любой GET-запрос возвращать страницу «Контакты».
"""