class Vaca:
    def __init__(self, sonido_base):
        self.sonido_base = sonido_base

    # Sobrecarga de metodo
    def hablar(self, palabra=None):
        if palabra is None:
            print(self.sonido_base)
        else:
            print(f'La vaca dice: {palabra}')

"""
Equivalente de sobrecarga de metodo en c++
class Vaca():

    def __init__(self, hablar):
        self.hablar = hablar

    def hablado(self):
        print(self.hablar)

    def hablado(self, palabra):
        print(f'la vaca dice {palabra}')
"""
# Polimorfismo porque el metodo se llama igual en las distintas clases pero hacen cosas distintas

class Chivo:
    def hablar(self):
        return "chiva"

class Oveja:
    def hablar(self):
        return "Beee"
    
chivo1 = Chivo()
oveja1 = Oveja()

juan_vaca = Vaca('muu')
juan_vaca.hablar()
juan_vaca.hablar('muje')
print(chivo1.hablar())
print(oveja1.hablar())
