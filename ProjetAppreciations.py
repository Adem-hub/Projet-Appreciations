Liste_Appreciations={"Trimestre très moyen":[0,4],"Trimestre moyen":[4,8],"Trimestre satisfaisant":[8,12],"Bon trimestre":[12,16],"Très bon trimestre":[16,18],"Trimestre Remarquable":[18,20]}

Liste_Regularite=["manque de sérieux à la fin de celui-ci","a été régulier tout au long du trimestre","une progression remarquable", "a su être sérieux tout au long de celui-ci."]


"""Il y a un début de code pour justement l'appréciation du début. J'essaye de faire maintenant la suite
    Avec la régularité en analysant notamment la courbe de l'élève"""

def Appreciation(ListeNotes):
    Moyenne_Eleve=sum(ListeNotes)/len(ListeNotes)
    Appreciation=''

    for App in Liste_Appreciations:
        if Liste_Appreciations[App][0]<=Moyenne_Eleve<Liste_Appreciations[App][1]:
            Appreciation = App
    return Appreciation,Moyenne_Eleve


Eleve=Appreciation([1,4,5])