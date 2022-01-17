class Person:
 def greet(self, name: str = 'Red Hatter') -> None:
 print('Hello {}!'.format(name))
pablo = Person()
pablo.greet('Jaime')
pablo.greet('Guy')
