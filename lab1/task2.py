# TODO Найдите количество книг, которое можно разместить на дискете
info_V = 1.44 #объём дискеты в Мб
lists = 100 #число страниц
str_on_list = 50 #число строк на странице
symbols_in_str = 25 #число символов в строке
Memory = 4 #память одного символа в байтах

symbols_in_book = lists * str_on_list * symbols_in_str #число символов в книге
Memory_book = symbols_in_book * Memory # объём 1 книги в байтах
Memory_book /= 1024 ** 2 #перевод в Мб

Chislo_books = info_V // Memory_book
print("Количество книг, помещающихся на дискету:", round(Chislo_books))
