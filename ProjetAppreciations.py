Liste_Appreciations={"Trimestre très moyen":[0,4],"Trimestre moyen":[4,8],"Trimestre satisfaisant":[8,12],"Bon trimestre":[12,16],"Très bon trimestre":[16,18],"Trimestre Remarquable":[18,20]}

Liste_Regularite={"un parcours trop irregulier":[-10,-1],"a été régulier tout au long":[-1,1],"une progression remarquable":[1,10]}


"""Il y a un début de code pour justement l'appréciation du début. J'essaye de faire maintenant la suite
    Avec la régularité en analysant notamment la courbe de l'élève"""


class Eleve:
    def __init__(self,ListeNotes):
        self.ListeNotes=ListeNotes
        self.Moyenne_Eleve=sum(ListeNotes)/len(ListeNotes)
        self.Appreciation=''
        self.Regularite=''
        self.Appreciation_()
        self.Regularite_()
        self.Incoherence()

        self.Tot= self.Appreciation+' '+self.Regularite

    def Incoherence(self):
        #Il y a peut être d'autres incoherences à ajouter, je n'en ai pas trouvé pour l'instant
        if self.Moyenne_Eleve<10:
            if self.Regularite=="a été régulier tout au long" or self.Regularite=="une progression remarquable":
                self.Regularite=='Vous pouvez progresser, vous en avez les capacités.'

    def Appreciation_(self):
        for App in Liste_Appreciations:
            if Liste_Appreciations[App][0]<=self.Moyenne_Eleve<Liste_Appreciations[App][1]:
                self.Appreciation = App

    def Regularite_(self):
        L=[]
        for i in range(len(self.ListeNotes)-1):
            Taux= ((self.ListeNotes[i+1]-self.ListeNotes[i])/2)
            L.append(Taux)
        #Ici on essaye de voir si le parcours de l'eleve est en dents de scie ou pas
        Parcours_Febrile=[n for n in L if n>4]
        Parcours_Febrile2=[n for n in L if n<-4]
        print(Parcours_Febrile,Parcours_Febrile2)
        print(L)
        if len(Parcours_Febrile)>=2 and len(Parcours_Febrile2)>=2:
            self.Regularite=" cependant dommage, vous avez manqué d'assiduité! Les résultats sont beacoup trop en dents de scie"
        else:
        #S'il n'est pas en dents de scie, alors on lui donne une appreciation adéquate
            somme=sum(L)
            for Reg in Liste_Regularite:
                if Liste_Regularite[Reg][0]<=somme<Liste_Regularite[Reg][1]:
                    self.Regularite=Reg





