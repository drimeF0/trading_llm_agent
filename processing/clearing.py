import re
from bs4 import BeautifulSoup

def clear(raw_text):
    """
    Эта функция очищает текст от HTML-тегов и URL-ссылок.

    :param raw_text: исходная строка с HTML и URL
    :return: очищенная строка
    """
    # 1. Удаление HTML-тегов с помощью BeautifulSoup
    soup = BeautifulSoup(raw_text, "html.parser")
    text_without_html = soup.get_text(separator=" ", strip=True) #

    # 2. Удаление URL-ссылок с помощью регулярных выражений
    # Это выражение находит строки, начинающиеся с http://, https://, /blog/, или www.
    cleaned_text = re.sub(r'https?://\S+|/blog/\S+|www\.\S+', '', text_without_html) #

    # 3. (Опционально) Удаление лишних пробелов, которые могли остаться
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()

    return cleaned_text
