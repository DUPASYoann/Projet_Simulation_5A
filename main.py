class Simulateur:

    def __init__(self, debut, fin):
        # simulateur
        self.echeancier = list()
        self.date_simulateur = 0.0
        self.date_fin = fin

        # ressource
        self.nb_bus = 0
        self.qc = 0
        self.bc = 0
        self.nb_bus_r = 0
        self.qr = 0
        self.br = 0

        # # mesure de performance
        self.attente_moyen_av_controle = 0
        self.attente_moyen_ap_controle = 0
        self.utilisation_moyen_centre_reparation = 0
        self.aire_qc = 0
        self.aire_qr = 0
        self.aire_br = 0

        # Debut
        self.echeancier.append([debut, self.date_simulateur])
        self.simulateur()

    def simulateur(self):
        while self.echeancier or self.date_simulateur < self.date_fin:
            # Récupération du dernier évènement ajouté
            couple = self.echeancier.pop()
            couple_evenement = couple[0]
            couple_date = couple[1]

            # Mise à jour des variables
            self.mise_a_jour_aires(self.date_simulateur, couple_date)
            self.date_simulateur = couple_date

            # Execution de l'évènement
            couple_evenement(self)

        print("Fin de la simulation")

    def ajout_evenement(self, evenement, date):
        index = -1
        for element in self.echeancier:
            if element[1] > date:
                break
            else:
                index += 1
        self.echeancier.insert(index, [evenement, date])

    def mise_a_jour_aires(self, date_simulation, date):
        self.aire_qc = self.aire_qc + (date - date_simulation) * self.qc
        self.aire_qr = self.aire_qr + (date - date_simulation) * self.qr
        self.aire_br = self.aire_br + (date - date_simulation) * self.br


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
    print("début de la simulation")
    simulateur.ajout_evenement(fin_simulation, 2.0)


def fin_simulation(simulateur):
    try:
        simulateur.attente_moyen_av_controle = simulateur.aire_qc / simulateur.nb_bus
        simulateur.attente_moyen_ap_controle = simulateur.aire_qr / simulateur.nb_bus_r
        simulateur.utilisation_moyen_centre_reparation = simulateur.aire_br / (2 * simulateur.date_fin)
    except ZeroDivisionError:
        pass
    print("fin de la simulation")


if __name__ == '__main__':
    Simulateur(debut_simulation, 160)
