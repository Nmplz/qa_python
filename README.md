# Sprint_4

## Установка зависимостей
pip install -r requirements.txt

## Запуск тестов
pytest

## 📚 Тестовое покрытие `BooksCollector`

Ниже перечислены тесты, покрывающие ключевые методы класса `BooksCollector`. Используется библиотека `pytest` с параметризацией.

---

### `test_add_new_book_add_two_books`

Проверяет метод `add_new_book`. Убеждается, что можно корректно добавить **две книги** в коллекцию.

---

### `test_init_attributes_equals_to_predefined_true`

Проверяет, что при инициализации коллектора все атрибуты:

- `books_genre`
- `favorites`
- `genre`
- `genre_age_rating`

имеют **значения по умолчанию**.

---

### `test_add_new_book_invalid_name_false`

Проверяет, что книги с **некорректным названием**:

- пустая строка
- длина больше 40 символов

**не добавляются** в `books_genre`.

---

### `test_add_new_book_true`

Проверяет, что книга с валидным названием корректно добавляется в `books_genre`.

---

### `test_add_book_ganre_true`

Проверяет, что метод `set_book_genre` устанавливает жанр корректно, и `get_book_genre` возвращает **ожидаемый жанр**.

---

### `test_add_book_invalid_ganre_false`

Убеждается, что **неподдерживаемый жанр** не присваивается книге, и `get_book_genre` возвращает пустую строку.

---

### `test_get_books_with_spec_genre_true`

Проверяет, что метод `get_books_with_specific_genre` возвращает **корректный список книг**, соответствующих заданному жанру.

---

### `test_get_books_for_children_true`

Проверяет, что книга с **безопасным жанром** (не входящим в `genre_age_rating`) попадает в список книг, подходящих для детей — `get_books_for_children`.

---

### `test_get_books_for_children_false`

Проверяет, что книга с **возрастным жанром** (например, "Ужасы") **не включается** в список детских книг.

---

### `test_add_book_to_favorites_true`

Проверяет, что метод `add_book_in_favorites` добавляет книгу в избранное, и она появляется в `get_list_of_favorites_books`.

---

### `test_delete_book_from_favorites_true`

Проверяет, что метод `delete_book_from_favorites` корректно **удаляет книгу из списка избранного**, если она была туда добавлена.

---
