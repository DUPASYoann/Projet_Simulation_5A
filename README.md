# Projet_Simulation_5A

**Avant propos :** Cet énoncé est certainement incomplet ou imprécis. Si à un moment vous pensez qu'il
vous manque une information : posez une hypothèse supplémentaire, en n'oubliant pas de la préciser
dans votre compte rendu.

**Restitution :** Vous fournirez un compte-rendu synthétique, comportant l'analyse du système, des
données, les algorithmes et les conclusions argumentées.
Vous fournirez également le code de votre simulateur ainsi que tous les codes périphériques que vous
auriez pu être amené à développer.

Vous présenterez les grandes lignes de votre travail lors d'une restitution d'une quinzaine de minutes
devant machine.
Travail demandé :
1. Reprendre l'exercice 4 de la feuille de TD et implémenter le simulateur correspondant. Les temps
d'attente moyens et taux d'occupation étant calculés à partir des aires sous les courbes des
effectifs des Files et d'occupation des postes. (Attention, on demande de réaliser une simulation
par événements, pas par processus !)
2. Faire des simulations sur 40, 80, 160 et 240 heures. Analyser les sorties.
3. Indicateurs statistiques
- recalculer les indicateurs de temps d'attente précédents en excluant les bus encore en train
d'attendre. Les résultats sont-ils significativement différents ?
- Y a t'il un intérêt à faire de même pour calculer le taux d'occupation des postes de réparation ?
- Calculer le temps d'attente maximum avant contrôle et avant réparation
4. Analyse des données d'entrée. Dans le fichier DonneesControle.txt, on dispose des dates d'arrivées
des bus ainsi que des durées de contrôle sur 160 heures.
- Ces données permettent-elles de retrouver la loi d'inter-arrivée ?
- Ces données permettent-elles de retrouver la loi de durée de contrôle ?
5. Etude d'un éventuel régime permanent. On ne s'intéresse dans cette partie qu'au temps d'attente
avant contrôle.
- Modifier le simulateur pouq que la simulation s'arrête quand le mième bus entre dans le poste
de contrôle (m étant une donnée d'entrée)
- On s'intéresse au processus (Di)i>=1 des temps d'attente avant contrôle des bus successifs et
plus particulièrement aux espérances E(Di) de ces VAR. Peut-on mettre en évidence un régime
permanent ? Quel est alors le temps d'attente espéré avant contrôle dans ce régime permanent ?
