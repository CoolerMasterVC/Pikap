# используется для сортировки
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


# Отделы
books = [
    Book(1, 'Книга кадров'),
    Book(2, 'Книга жизни'),
    Book(3, 'джунги'),


    Book(11, 'Жизнь'),
    Book(22, 'Мир и мир'),
    Book(33, 'Какая-то ещё'),
]


# Сотрудники
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
]


def main():
    """Основная функция"""


    # Соединение данных один-ко-многим 
    one_to_many = [(c.name, c.pages, b.name) 
        for b in books 
        for c in chapters 
        if b.id==c.book_id]
    
    # Соединение данных многие-ко-многим
    many_to_many_temp = [(b.name, cb.book_id, cb.chapter_id) 
        for b in books 
        for cb in chapters_books 
        if b.id==cb.book_id]
    
    many_to_many = [(c.name, c.pages, book_name) 
        for book_name, book_id, chapter_id in many_to_many_temp
        for c in chapters if c.id==chapter_id]

    #print(many_to_many_temp)
    #print(many_to_many)

    print('Задание E1')
    res_11 = [res 
        for res in one_to_many
        if "книга" in res[2].lower() 
        ]
    print(res_11)
    
    print('\nЗадание E2')
    res_12_unsorted = []
    # Перебираем все отделы
    for b in books:
        # Список сотрудников отдела
        b_chapters = list(filter(lambda i: i[2]==b.name, one_to_many))
        #print(b_chapters, 1375198327501751)
        # Если отдел не пустой        
        if len(b_chapters) > 0:
            # Зарплаты сотрудников отдела
            b_pages = [page for _,page,_ in b_chapters]
            # Суммарная зарплата сотрудников отдела
            b_page_mid = round(sum(b_pages)/len(b_pages),2)
            res_12_unsorted.append((b.name, b_page_mid))


    # Сортировка по суммарной зарплате
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)


    print('\nЗадание E3')
    res_13 = {}
    # Перебираем все отделы
    for c in chapters:
        if 'К' in c.name:
            # Список сотрудников отдела
            b_chapters = list(filter(lambda i: i[0]==c.name, many_to_many))
            # Только ФИО сотрудников
            b_chapters_st = [x for _,_,x in b_chapters]
            # Добавляем результат в словарь
            # ключ - отдел, значение - список фамилий
            res_13[c.name] = b_chapters_st


    print(res_13)


if __name__ == '__main__':
    main()


# class Department:
#     def __init__(self, id_department, name):
#         self.id_department = id_department
#         self.name = name

# class Employee:
#     def __init__(self, id_employee, last_name, salary, id_department):
#         self.id_employee = id_employee
#         self.last_name = last_name
#         self.salary = salary
#         self.id_department = id_department

# class EmployeeDepartment:
#     def __init__(self, id_employee, id_department):
#         self.id_employee = id_employee
#         self.id_department = id_department

# departments = [
#     Department(1, "Отдел продаж"),
#     Department(2, "Отдел разработки"),
#     Department(3, "Отдел маркетинга"),
#     Department(4, "Финансовый отдел"),
# ]

# employees = [
#     Employee(1, "Алексеев", 50000, 1),
#     Employee(2, "Борисов", 60000, 1),
#     Employee(3, "Сидоров", 70000, 2),
#     Employee(4, "Андреев", 80000, 2),
#     Employee(5, "Петров", 90000, 3),
# ]

# # Связь многие-ко-многим (пример)
# employee_departments = [
#     EmployeeDepartment(1, 1),
#     EmployeeDepartment(2, 1),
#     EmployeeDepartment(3, 2),
#     EmployeeDepartment(4, 2),
#     EmployeeDepartment(5, 3),
# ]

# def departments_with_employees(departments, employees):
#     result = {}
#     for department in departments:
#         if 'отдел' in department.name.lower():
#             result[department.name] = [emp.last_name for emp in employees if emp.id_department == department.id_department]
#     return result

# print(departments_with_employees(departments, employees))

# def average_salary_by_department(departments, employees):
#     department_salary = {}
    
#     for emp in employees:
#         if emp.id_department not in department_salary:
#             department_salary[emp.id_department] = []
#         department_salary[emp.id_department].append(emp.salary)
    
#     average_salaries = []
    
#     for dept in departments:
#         if dept.id_department in department_salary:
#             avg_salary = round(sum(department_salary[dept.id_department]) / len(department_salary[dept.id_department]), 2)
#             average_salaries.append((dept.name, avg_salary))
    
#     return sorted(average_salaries, key=lambda x: x[1])

# print(average_salary_by_department(departments, employees))
# def employees_with_last_name_a(employees, departments):
#     result = []
#     for emp in employees:
#         if emp.last_name.startswith('А'):
#             dept_name = next((dept.name for dept in departments if dept.id_department == emp.id_department), None)
#             result.append((emp.last_name, dept_name))
#     return result

# print(employees_with_last_name_a(employees, departments), 1232414)
