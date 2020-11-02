import numpy as np
import pandas as pd

fileName = "DonneesControle.txt"

if __name__ == "__main__":

   data = pd.read_csv(fileName, sep=" ", header=None)
   # data.columns = ["loiUne", "loiDeux", "rien"]
   print(data.shape)

   inter_arrivee = []
   duree_controle = []

   for i in range(0, 74):
      res = data[0][i+1] - data[0][i]
      inter_arrivee.append(res)
      duree_controle.append(data[1][i])

   duree_controle.append(data[1][74])

   print(len(inter_arrivee))
   print(type(inter_arrivee))
   print(type(duree_controle))
   inter_arrivee.sort()
   duree_controle.sort()
   print(inter_arrivee)
   print(duree_controle)
   
  for i in range(0,7):
      print(inter_arrivee[i*10])
   print()
   for i in range(0,7):
      print(duree_controle[i*10])
