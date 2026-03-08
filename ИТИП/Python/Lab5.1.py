class Book():
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_info(self):
        return f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}"
    
luti_kniga = Book('Книга', 'Автор', '2024')
bad_kniga = Book('Плохая книга', 'Плохой автор', '990')

print(luti_kniga.get_info())
print(bad_kniga.get_info())