# du_10.02.26_pasta cooking app

class Pasta:
    def __init__(self, typ_cestovina=None, omacka=None, obloha=None, dresing=None):
        self.typ_cestovina = typ_cestovina
        self.omacka = omacka
        self.obloha = obloha
        self.dresing = dresing

class PastaBuilder:
    def __init__(self):
        self.typ_cestovina = None
        self.omacka = None
        self.obloha = None
        self.dresing = None

    def add_typ_cestovina(self, typ_cestovina):
        self.typ_cestovina = typ_cestovina

    def add_omacka(self, omacka):
        self.omacka = omacka

    def add_obloha(self, obloha):
        self.obloha = obloha

    def add_dresing(self, dresing):
        self.dresing = dresing

    def build(self):
        return Pasta(
            self.typ_cestovina,
            self.omacka,
            self.obloha,
            self.dresing
        )

def vypis_pastu(pasta):
    print(
        pasta.typ_cestovina,
        pasta.omacka,
        pasta.obloha,
        pasta.dresing,
        sep=" / "
    )

builder1 = PastaBuilder()
builder1.add_typ_cestovina("Špagety")
builder1.add_omacka("Bolonská omáčka")
builder1.add_obloha("Parmezán")
spagety = builder1.build()

builder2 = PastaBuilder()
builder2.add_typ_cestovina("Ravioli")
builder2.add_dresing("Olivový olej")
ravioli = builder2.build()

builder3 = PastaBuilder()
builder3.add_typ_cestovina("Penne")
builder3.add_omacka("Rajčinová omáčka")
builder3.add_dresing("Olivový olej")
builder3.add_obloha("Syr")
penne = builder3.build()

vypis_pastu(spagety)
vypis_pastu(ravioli)
vypis_pastu(penne)