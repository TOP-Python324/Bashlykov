def deck() -> 'generator':
    """Функция возвращает объект генератор, которй возвращает кортеж из двух элементов в упорядоченной колоде карт"""
    
    card_suit = ['черви', 'бубны', 'пики', 'трефы']
    
    for suit in card_suit:
        for n in range (2, 15):        
            yield (n, suit)
            
# >>> list(deck())[:31:5]
# [(2, 'черви'), (7, 'черви'), (12, 'черви'), (4, 'бубны'), (9, 'бубны'), (14, 'бубны'), (6, 'пики')]# >>> list(deck())[::13]
# [(2, 'черви'), (2, 'бубны'), (2, 'пики'), (2, 'трефы')]
# >>> list(deck())[::10]
# [(2, 'черви'), (12, 'черви'), (9, 'бубны'), (6, 'пики'), (3, 'трефы'), (13, 'трефы')]
# >>> list(deck())[:31:5]
# [(2, 'черви'), (7, 'черви'), (12, 'черви'), (4, 'бубны'), (9, 'бубны'), (14, 'бубны'), (6, 'пики')]