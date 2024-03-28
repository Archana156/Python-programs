class Library:
    def __init__(self, book):
        book_details = book.split(", ")
        self.name = book_details[0]
        self.__author = book_details[1]
        self.__edition = book_details[2]
        self._rate = int(book_details[3])  

    def publish(self):
        print(f"Book: {self.name}, Author: {self.__author}, Edition: {self.__edition}, Rate: {self._rate}")
        return self._rate

lib = Library("Harry Potter, Rowling, House, 250")

lib.publish()



