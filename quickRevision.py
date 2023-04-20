import pandas as pd
import random as rd

print("Chargement de data.csv")
dataframe = pd.read_csv('data.csv', header=None)

liste = dataframe.values.tolist()

while True:

    print("nb restant ", len(liste))

    if len(liste) == 0:
        print("fini tu connais TOUT")
        break

    i = rd.randint(0, len(liste) - 1)
    question = liste[i][1]
    rep = liste[i][0]
    print(question)
    a = input("")

    if a != rep:
        print("la rep était")
        print(rep)
        k = 0
        input()
    else:
        liste.pop(i)
    
    print()
