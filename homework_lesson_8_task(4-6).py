# homework_lesson_8_task4-6
"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
"""

"""
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу 
в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также 
других данных, можно использовать любую подходящую структуру, например словарь.
"""

"""
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, 
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных 
на уроках по ООП.
"""

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

class Warehouse:
    equipment_list = {'printers': 0, 'scaners': 0, 'xerox': 0}
    max_quantity = 1000
    stock_quantity = 0


    @classmethod
    def incoming(self, type, quantity_incom):
        try:
            if Warehouse.stock_quantity + int(quantity_incom) <= Warehouse.max_quantity:
                Warehouse.equipment_list[type] += quantity_incom
                Warehouse.stock_quantity += quantity_incom
            else:
                raise OwnError('Добавление на склад невозмжно! Проверьте доступный объем склада.')
        except ValueError:
                print('Добавление на склад невозмжно! Вы ввели не числовое значение.')
        except OwnError as err:
            print(err)

    @classmethod
    def outgoing(self, type, quantity_out):
        try:
            if Warehouse.equipment_list[type] - int(quantity_out) >= 0:
                Warehouse.equipment_list[type] -= quantity_out
                Warehouse.stock_quantity -= quantity_out
            else:
                raise OwnError('Перемещение с текущего склада невозможно! Проверьте доступный объем склада.')
        except ValueError:
                print('Добавление на склад невозмжно! Вы ввели не числовое значение.')
        except OwnError as err:
            print(err)

class OfficeEquipment:
    def __init__(self, brand, model, type, quantity):
        self.brand = brand
        self.model = model
        self.type = type
        self.quantity = quantity

class Printers(OfficeEquipment):
    def __init__(self, brand, model, quantity, print_speed, type='printers'):
        super().__init__(brand, model, type, quantity)
        self.print_speed = print_speed

    def __str__(self):
        return f'Принтер {self.__dict__}'

class Scaners(OfficeEquipment):
    def __init__(self, brand, model, quantity, scaner_speed, type='scaners'):
        super().__init__(brand, model, type, quantity)
        self.scaner_speed = scaner_speed

    def __str__(self):
        return f'Сканер {self.__dict__}'

class Xerox(OfficeEquipment):
    def __init__(self, brand, model, quantity, copy_speed, type='xerox'):
        super().__init__(brand, model, type, quantity)
        self.copy_speed = copy_speed

    def __str__(self):
        return f'Ксерокс {self.__dict__}'

# ---------------------------------------------------------------------
printer_1 =Printers('Samsung', 'PCX111222', 400, 20)
print(printer_1)
printer_2 =Printers('HP', 'Pxw333444', 700, 25)
print(printer_2)

scaner_1 =Scaners('Samsung', 'SCX111222', 600, 100)
print(scaner_1)
scaner_2 =Scaners('HP', 'Swx333444', 200, 95)
print(scaner_2)

xerox_1 =Xerox('Samsung', 'XWZ111222', 750, 230)
print(xerox_1)
xerox_2 =Xerox('HP', 'Xps333444', 350, 235)
print(xerox_2)
print()

Warehouse.incoming('scaners', 1001)
print(Warehouse.equipment_list)
Warehouse.incoming('scaners', 'sdfg')
print(Warehouse.equipment_list)
Warehouse.incoming('scaners', 7)
print(Warehouse.equipment_list)
print()

Warehouse.outgoing('scaners', 1001)
print(Warehouse.equipment_list)
Warehouse.outgoing('scaners', 'sdfg')
print(Warehouse.equipment_list)
Warehouse.outgoing('scaners', 3)
print(Warehouse.equipment_list)
