class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]


class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contracts(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = self._validate_author(author)
        self.book = self._validate_book(book)
        self.date = self._validate_date(date)
        self.royalties = self._validate_royalties(royalties)
        Contract.all.append(self)

    @staticmethod
    def _validate_author(value):
        if not isinstance(value, Author):
            raise TypeError("Author must be an instance of Author class")
        return value

    @staticmethod
    def _validate_book(value):
        if not isinstance(value, Book):
            raise TypeError("Book must be an instance of Book class")
        return value

    @staticmethod
    def _validate_date(value):
        if not isinstance(value, str):
            raise TypeError("Date must be a string")
        return value

    @staticmethod
    def _validate_royalties(value):
        if not isinstance(value, int):
            raise TypeError("Royalties must be an integer")
        return value

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
