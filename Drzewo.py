class Wezel():
    def __init__(self,wartosc=None):
        self.wartosc = wartosc
        self.lewy = None
        self.prawy = None

    def is_leaf(self):
        if self.lewy == None and self.prawy == None:
            return True
        else:
            return False

    def add_lewy(self, wartosc):
        dziecko = Wezel(wartosc)
        if self.lewy == None:
            self.lewy = dziecko
        else:
            dziecko.lewy = self.lewy
            self.lewy = dziecko


    def add_prawy(self, wartosc):
        dziecko = Wezel(wartosc)
        if self.prawy == None:
            self.prawy = dziecko
        else:
            dziecko.prawy = self.prawy
            self.prawy = dziecko

    def deepfirst(self, visit):
        wierzcholek = Wezel()
        if wierzcholek == None:
            return None
        else:
            visit(wierzcholek)
            deepfirst(wierzcholek.lewy, visit)







    def __str__(self):
        return "[{}; {}; {}]".format(self.wartosc, self.lewy, self.prawy)


wezel = Wezel(1)
wezel.add_lewy(2)
wezel.add_prawy(3)
print(wezel)




class Drzewo():
    def __init__(self):
        self.korzen = Wezel()




