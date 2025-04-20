import pytest


class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.add_new_book("Что делать, если ваш кот хочет вас убить")
        assert len(collector.books_genre) == 2

    def test_init_attributes_equals_to_predefined_true(self, collector):
        assert collector.books_genre == {}
        assert collector.favorites == []
        assert collector.genre == [
            "Фантастика",
            "Ужасы",
            "Детективы",
            "Мультфильмы",
            "Комедии",
        ]
        assert collector.genre_age_rating == ["Ужасы", "Детективы"]

    @pytest.mark.parametrize("book_name", ["", "x" * 41])
    def test_add_new_book_invalid_name_false(self, collector, book_name):
        collector.add_new_book(book_name)
        assert len(collector.books_genre) == 0, "Книга с именем в 0 или 41+ символов не должна добавляться в self.books_genre"

    @pytest.mark.parametrize("book", ["Дюна", "Сияние", "Собака Баскервилей"])
    def test_add_new_book_true(self, book, collector):
        collector.add_new_book(book)
        assert book in collector.books_genre

    @pytest.mark.parametrize("book_name, book_genre", [["Дюна", "Фантастика"], ["Сияние", "Ужасы"], ["Собака Баскервилей", "Детективы"]])
    def test_add_book_ganre_true(self, book_name, book_genre, collector):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        assert collector.get_book_genre(book_name) == book_genre, f"Жанр книги не соответствует ожидаемому : {book_genre}"

    @pytest.mark.parametrize("book_name, book_genre", [["Кладбище домашних животных", "МегаУжасы"]])
    def test_add_book_invalid_ganre_false(self, book_name, book_genre, collector):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        assert collector.get_book_genre(book_name) == "", f"Несуществующий жанр - {book_genre}, не должен добавляться в коллекцию"

    @pytest.mark.parametrize("book_genre", ["Детективы", "Мультфильмы", "Комедии"])
    def test_get_books_with_spec_genre_true(self, collector, book_genre):
        collector.add_new_book("Матрица")
        collector.set_book_genre("Матрица", book_genre)
        books = collector.get_books_with_specific_genre(book_genre)
        assert "Матрица" in books

    def test_get_books_for_children_true(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        books = collector.get_books_for_children()
        assert "Гарри Поттер" in books

    def test_get_books_for_children_false(self, collector):
        collector.add_new_book("Оно")
        collector.set_book_genre("Оно", "Ужасы")
        books = collector.get_books_for_children()
        assert "Оно" not in books

    @pytest.mark.parametrize("book_name", ["Дюна", "Нейромант", "Сияние", "451 градус по Фаренгейту"])
    def test_add_book_to_favorites_true(self, collector, book_name):
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        fav_list = collector.get_list_of_favorites_books()
        assert book_name in fav_list

    @pytest.mark.parametrize("book_name", ["Цветы для Элджернона", "Марсианин", "Левиафаны открываются", "Автостопом по галактике"])
    def test_delete_book_from_favorites_true(self, collector, book_name):
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        fav_list = collector.get_list_of_favorites_books()
        assert book_name not in fav_list

    def test_get_books_genre_true(self, collector):
        collector.add_new_book("Нейромант")
        collector.set_book_genre("Нейромант", "Фантастика")
        collector.add_new_book("Винни-Пух")
        collector.set_book_genre("Винни-Пух", "Мультфильмы")
        books_genre = collector.get_books_genre()
        assert books_genre == {"Нейромант": "Фантастика", "Винни-Пух": "Мультфильмы"}

    def test_get_list_of_favorites_books_true(self, collector):
        collector.add_new_book("Нейромант")
        collector.add_book_in_favorites("Нейромант")
        collector.add_new_book("Винни-Пух")
        collector.add_book_in_favorites("Винни-Пух")
        fav_list = collector.get_list_of_favorites_books()
        assert fav_list == ["Нейромант", "Винни-Пух"]
