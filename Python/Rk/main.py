from operator import itemgetter


class Chapter:
    def __init__(self, id, name, pages, book_id):
        self.id = id
        self.name = name
        self.pages = pages
        self.book_id = book_id


class Book:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class ChapBook:
    def __init__(self, book_id, chapter_id):
        self.book_id = book_id
        self.chapter_id = chapter_id


books = [
    Book(1, 'Книга кадров'),
    Book(2, 'Книга жизни'),
    Book(3, 'джунги'),


    Book(11, 'Жизнь'),
    Book(22, 'Мир и мир'),
    Book(33, 'Какая-то ещё'),
]

chapters = [
    Chapter(1, 'Глава 1', 25000, 1),
    Chapter(2, 'Глава 2', 35000, 2),
    Chapter(3, 'КГлава 3', 45000, 3),
    Chapter(4, 'КГлава 4', 35000, 1),
    Chapter(5, 'КГлава 5', 25000, 2),
    Chapter(6, 'КГлава 6', 15324, 1),
    Chapter(7, 'Глава 7', 76585, 2),
    Chapter(8, 'Глава 8', 1734, 3)
]


chapters_books = [
    ChapBook(1,1),
    ChapBook(2,2),
    ChapBook(3,3),
    ChapBook(3,4),
    ChapBook(3,5),


    ChapBook(11,1),
    ChapBook(22,2),
    ChapBook(33,3),
    ChapBook(33,4),
    ChapBook(33,5),
    ChapBook(33,6),
]


def main():
    """Основная функция"""

    one_to_many = [(c.name, c.pages, b.name) 
        for b in books 
        for c in chapters 
        if b.id==c.book_id]
    
    many_to_many_temp = [(b.name, cb.book_id, cb.chapter_id) 
        for b in books 
        for cb in chapters_books 
        if b.id==cb.book_id]
    
    many_to_many = [(c.name, c.pages, book_name) 
        for book_name, book_id, chapter_id in many_to_many_temp
        for c in chapters if c.id==chapter_id]

    print('Задание E1')
    res_11 = [res 
        for res in one_to_many
        if "книга" in res[2].lower() 
        ]
    print(res_11)
    
    print('\nЗадание E2')
    res_12_unsorted = []
    for b in books:
        b_chapters = list(filter(lambda i: i[2]==b.name, one_to_many))
        if len(b_chapters) > 0:
            b_pages = [page for _,page,_ in b_chapters]
            b_page_mid = round(sum(b_pages)/len(b_pages),2)
            res_12_unsorted.append((b.name, b_page_mid))

    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    print('\nЗадание E3')
    res_13 = {}
    for c in chapters:
        if 'К' in c.name:
            b_chapters = list(filter(lambda i: i[0]==c.name, many_to_many))
            b_chapters_st = [x for _,_,x in b_chapters]
            res_13[c.name] = b_chapters_st


    print(res_13)


if __name__ == '__main__':
    main()


