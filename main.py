import numpy.random as npr
import numpy as np
import matplotlib.pyplot as plt


class Simulateur:

    def __init__(self, debut, fin):
        # simulateur
        self.echeancier = list()
        self.date_simulateur = 0.0
        self.date_fin = fin
        self.historique = list()
        self.nu_bus_traite_control = 0

        # matplotlib
        self.x_time = list()
        self.y_bc = list()
        self.y_br = list()
        self.y_qc = list()
        self.y_qr = list()
        self.y_aire_qc = list()
        self.y_nb_bus = list()
        self.x_time_sd = list()
        self.y_qc_sd = list()

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
        self.taille_moyenne_file_c = 0
        self.taille_moyenne_file_r = 0

        # paramètre
        self.param_reparation = 0.3

        # # paramètre en minute
        self.param_arrivee_bus = 120
        self.param_controle_low = 15
        self.param_controle_high = 65
        self.param_reparation_low = 126
        self.param_reparation_high = 270

        # Debut
        self.echeancier.append([debut, self.date_simulateur])
        self.simulateur()

    def simulateur(self):
        while self.echeancier and self.date_simulateur < self.date_fin:
            # Récupération du dernier évènement ajouté
            couple = self.echeancier.pop(0)
            couple_evenement = couple[0]
            couple_date = couple[1]

            # Mise à jour des variables
            self.mise_a_jour_aires(self.date_simulateur, couple_date)
            self.date_simulateur = couple_date

            # Execution de l'évènement
            couple_evenement(self)
            self.historique.append(
                (couple_evenement.__str__().split(" ")[1], couple_date, self.nu_bus_traite_control, self.bc, self.br))

        print("Fin du simulateur")

    def ajout_evenement(self, evenement, date):
        index = 0
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

        # Graphic
        self.x_time.append(date_simulation)
        self.y_bc.append(self.bc)
        self.y_br.append(self.br)
        self.y_qc.append(self.qc)
        self.y_qr.append(self.qr)
        self.y_aire_qc.append(self.aire_qc / (self.nb_bus + 0.00001))
        self.y_nb_bus.append(self.nb_bus)

        if len(self.x_time_sd) > 0 and self.x_time_sd[-1] == date_simulation:
            self.x_time_sd.pop()
            self.y_qc_sd.pop()

        self.x_time_sd.append(date_simulation)
        self.y_qc_sd.append(self.qc)


def arrivee_bus(simulateur):
    simulateur.ajout_evenement(arrivee_bus, simulateur.date_simulateur + npr.exponential(simulateur.param_arrivee_bus))
    simulateur.nb_bus += 1
    simulateur.ajout_evenement(arrivee_file_c, simulateur.date_simulateur)


def arrivee_file_c(simulateur):
    simulateur.qc += 1
    if simulateur.bc == 0:
        simulateur.ajout_evenement(acces_controle, simulateur.date_simulateur)


def acces_controle(simulateur):
    simulateur.qc -= 1
    simulateur.bc = 1
    simulateur.ajout_evenement(depart_controle, simulateur.date_simulateur +
                               npr.uniform(simulateur.param_controle_low, simulateur.param_controle_high))

    # Modification
    simulateur.nu_bus_traite_control += 1


def depart_controle(simulateur):
    simulateur.bc = 0
    if simulateur.qc > 0:
        simulateur.ajout_evenement(acces_controle, simulateur.date_simulateur)
    if npr.rand() < 0.3:
        simulateur.ajout_evenement(arrivee_file_r, simulateur.date_simulateur)


def arrivee_file_r(simulateur):
    simulateur.qr += 1
    simulateur.nb_bus_r += 1
    if simulateur.br < 2:
        simulateur.ajout_evenement(acces_reparation, simulateur.date_simulateur)


def acces_reparation(simulateur):
    simulateur.qr -= 1
    simulateur.br += 1
    simulateur.ajout_evenement(depart_reparation, simulateur.date_simulateur +
                               npr.uniform(simulateur.param_reparation_low, simulateur.param_reparation_high))


def depart_reparation(simulateur):
    simulateur.br -= 1
    if simulateur.qr > 0:
        simulateur.ajout_evenement(acces_reparation, simulateur.date_simulateur)


def debut_simulation(simulateur):
    simulateur.attente_moyen_av_controle = 0
    simulateur.attente_moyen_ap_controle = 0
    simulateur.utilisation_moyen_centre_reparation = 0
    simulateur.aire_qc = 0
    simulateur.aire_qr = 0
    simulateur.aire_br = 0
    simulateur.ajout_evenement(arrivee_bus, simulateur.date_simulateur + npr.exponential(simulateur.param_arrivee_bus))
    simulateur.ajout_evenement(fin_simulation, simulateur.date_fin)


def fin_simulation(simulateur):
    try:
        simulateur.attente_moyen_av_controle = simulateur.aire_qc / simulateur.nb_bus
        simulateur.attente_moyen_ap_controle = simulateur.aire_qr / simulateur.nb_bus_r
        simulateur.utilisation_moyen_centre_reparation = simulateur.aire_br / (2 * simulateur.date_fin)
        simulateur.taille_moyenne_file_c = simulateur.aire_qc / simulateur.date_fin
        simulateur.taille_moyenne_file_r = simulateur.aire_qr / simulateur.date_fin
    except ZeroDivisionError:
        pass
    print("evenement fin de la simulation")


if __name__ == '__main__':
    moyenne_tps_att_moy_avt_ctrl = 0
    moyenne_tps_att_moy_avt_rep = 0
    moyenne_taille_moy_file_c = 0
    moyenne_taille_moy_file_r = 0
    moyenne_taux_utilisation_centre_rep = 0
    list_moyenne = list()

    for i in range(500):
        simu = Simulateur(debut_simulation, 240*60)
        moyenne_tps_att_moy_avt_ctrl += simu.attente_moyen_av_controle
        moyenne_tps_att_moy_avt_rep += simu.attente_moyen_ap_controle
        moyenne_taille_moy_file_c += simu.taille_moyenne_file_c
        moyenne_taille_moy_file_r += simu.taille_moyenne_file_r
        moyenne_taux_utilisation_centre_rep += simu.utilisation_moyen_centre_reparation
        list_moyenne.append(simu.attente_moyen_av_controle/500)

    print("list moyenne")
    print(np.std(list_moyenne))
    moyenne_tps_att_moy_avt_ctrl /= 500
    moyenne_tps_att_moy_avt_rep /= 500
    moyenne_taille_moy_file_c /= 500
    moyenne_taille_moy_file_r /= 500
    moyenne_taux_utilisation_centre_rep /= 500

    print("moyenne_tps_att_moy_avt_ctrl")
    print(moyenne_tps_att_moy_avt_ctrl/60)
    print("moyenne_tps_att_moy_avt_rep")
    print(moyenne_tps_att_moy_avt_rep/60)
    print("moyenne_taille_moy_file_c")
    print(moyenne_taille_moy_file_c)
    print("moyenne_taille_moy_file_r")
    print(moyenne_taille_moy_file_r)
    print("moyenne_taux_utilisation_centre_rep")
    print(moyenne_taux_utilisation_centre_rep)

    # simu = Simulateur(debut_simulation, 240 * 60)
    # plt.plot(simu.x_time_sd, simu.y_qc_sd)
    # plt.show()
    # plt.plot(simu.x_time, simu.y_aire_qc)
    # plt.show()
    # print(simu.nb_bus)
    # print(simu.nb_bus_r)
    # print(simu.x_time_sd)
    # print(simu.y_qc_sd)
