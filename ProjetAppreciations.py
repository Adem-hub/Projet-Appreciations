Liste_Appreciations={"Trimestre très moyen":[0,4],"Trimestre moyen":[4,8],"Trimestre satisfaisant":[8,12],"Bon trimestre":[12,16],"Très bon trimestre":[16,18],"Trimestre Remarquable":[18,20]}

Liste_Regularite={"un parcours trop irregulier":[-10,-1],"a été régulier tout au long":[-1,1],"une progression remarquable":[1,10]}


#Essayez avec Jules=Eleve([14,17,18,12]) par exemple


class Eleve:
    def __init__(self,ListeNotes):
        self.ListeNotes=ListeNotes
        self.Moyenne_Eleve=sum(ListeNotes)/len(ListeNotes)
        self.Appreciation_1=''
        self.Appreciation_2=''
        self.Appreciation()
        self.Regularite()
        self.Incoherence()

        self.App_Finale= self.Appreciation_1+' '+self.Appreciation_2

    def Incoherence(self):
        #Il y a peut être d'autres incoherences à ajouter, je n'en ai pas trouvé pour l'instant
        if self.Moyenne_Eleve<=10:
            if self.Appreciation_2=="a été régulier tout au long" or self.Appreciation_2=="une progression remarquable":
                self.Appreciation_2=='Vous pouvez progresser, vous en avez les capacités.'

    def Appreciation(self):
        for App in Liste_Appreciations:
            if Liste_Appreciations[App][0]<=self.Moyenne_Eleve<Liste_Appreciations[App][1]:
                self.Appreciation_1 = App

    def Regularite(self):
        L=[]
        for i in range(len(self.ListeNotes)-1):
            Taux= ((self.ListeNotes[i+1]-self.ListeNotes[i])/2)
            L.append(Taux)
        #Ici on essaye de voir si le parcours de l'eleve est en dents de scie ou pas
        Parcours_Febrile=[n for n in L if n>4]
        Parcours_Febrile2=[n for n in L if n<-4]
        print(L)
        print(Parcours_Febrile,Parcours_Febrile2)
        if len(Parcours_Febrile)>=1 and len(Parcours_Febrile2)>=1:
            self.Appreciation_2=" cependant dommage, vous avez manqué d'assiduité! Les résultats sont beacoup trop en dents de scie"
        else:
        #S'il n'est pas en dents de scie, alors on lui donne une appreciation adéquate
            somme=sum(L)
            print(somme)
            for Reg in Liste_Regularite:
                if Liste_Regularite[Reg][0]<=somme<Liste_Regularite[Reg][1]:
                    self.Appreciation_2=Reg





