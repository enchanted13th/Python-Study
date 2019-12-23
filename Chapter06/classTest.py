class Person() :
    # 객체 초기화 메서드
    def __init__(self, name) :
        self.name = name

hunter = Person('Elmer Fudd')
print('The mighty hunter:', hunter.name)