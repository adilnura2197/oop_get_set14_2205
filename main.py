class Kurs:
    def __init__(self, nom, davomiylik):
        self.nom = nom
        self.__davomiylik = davomiylik

    def get_davomiylik(self):
        return self.__davomiylik

    def set_davomiylik(self, oy):
        if oy > 0:
            self.__davomiylik = oy
            print("Davomiylik yangilandi")
        else:
            print("Xato qiymat")


k1 = Kurs("Python", 6)
print(k1.get_davomiylik())
