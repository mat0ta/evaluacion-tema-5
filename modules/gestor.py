import pickle

class Personaje:
    def __init__(self, nombre, atack, defense, range, life):
        self.nombre = nombre
        self.ataque = atack
        self.defensa = defense
        self.alcance = range
        self.vida = life

    def __str__(self):
        return "{}\nDatos: {} ataque, {} defensa, {} alcance, {} vida.".format(self.nombre, self.vida, self.ataque, self.defensa, self.alcance)

class Gestor:
    personajes = []

    def __init__(self):
        self.load_data()

    def load_data(self):
        data = open("./personajes.pkl", "ab+")
        data.seek(0)
        try:
            self.personajes = pickle.load(data)
        except:
            print("No hay ningun dato")
            pass
        finally:
            data.close()
            print("Se han cargado " + str(len(self.personajes)) + " personajes.")

    def add(self, p):
        for personaje_temporal in self.personajes:
            if personaje_temporal.nombre == p.nombre:
                return
        self.personajes.append(p)
        self.save()

    def delete(self, nombre):
        for personaje_temporal in self.personajes:
            if personaje_temporal.nombre == nombre:
                self.personajes.remove(personaje_temporal)
                self.save()
                print("\n{} ha sido eliminado".format(nombre))
                return

    def show(self):
        if len(self.personajes) == 0:
            print("Gestor sin dator")
            return
        for p in self.personajes:
            print(p)

    def save(self):
        fichero = open("./personajes.pkl", "wb")
        pickle.dump(self.personajes, fichero)
        fichero.close()


def main():
    gestor = Gestor()
    gestor.add(Personaje("Caballero", 4, 2, 4, 2))
    gestor.add(Personaje("Guerrero", 2, 4, 2, 4))
    gestor.add(Personaje("Arquero", 2, 4, 1, 8))
    gestor.show()
    gestor.delete("Arquero")
    gestor.show()

if __name__ == "__main__":
    main()