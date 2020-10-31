class Simulateur:

    def __init__(self, debut):
        self.echeancier = list()
        self.date_simulateur = 0.0
        self.echeancier.append([debut, self.date_simulateur])
        self.simulateur()

    def simulateur(self):
        while self.echeancier:
            # Récupération du dernier évènement ajouté
            couple = self.echeancier.pop()
            couple_evenement = couple[0]
            couple_date = couple[1]

            # Mise à jour des variables
            self.mise_a_jour_aires(couple_date)
            self.date_simulateur = couple_date

            # Execution de l'évènement
            couple_evenement(self)

        print("Fin de la simulation")

    def ajout_evenement(self, evenement, date):
        self.echeancier.append([evenement, date])

    def mise_a_jour_aires(self, date):
        pass


def arrivee_bus(simulateur):
    pass


def arrivee_file_c(simulateur):
    pass


def acces_controle(simulateur):
    pass


def depart_controle(simulateur):
    pass


def arrivee_file_r(simulateur):
    pass


def acces_reparation(simulateur):
    pass


def depart_reparation(simulateur):
    pass


def debut_simulation(simulateur):
    print("youpi")
    simulateur.ajout_evenement(fin_simulation, 2.0)


def fin_simulation(simulateur):
    print("c'est la fin :'(")


if __name__ == '__main__':
    Simulateur(debut_simulation)
