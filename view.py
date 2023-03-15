from datetime import datetime

import random
from controler import Controler

from models import Player, Tournament



class View(object): 
    
    def __init__(self):
        self.controler = Controler()
        
    
    def debut_tournois(self):#
        print("Entre les info pour la creation d'un tournois fdp ")
        
        name, start, end, address = None, None, None, None
        while name == None:
            name = self.ask_name()
        while end == None or start >= end :
            if end != None:
                start, end = None, None
                print("La date de début est supérieure à la date de fin")
            while start == None:
                start = self.date_event("Quelle est la date de début du tournois ? : ")
            while end == None:
                end = self.date_event("Quelle est la date de fin du tournois ? : ")
            print(f"C'est bien fdp ta initialiser le tournois sous le nom de {name} qui commencera le '{start}'et se terminera le '{end}'; ".format(name,start,end))
            while address == None:
                address = self.ask_adress()
        #self.controler.create_tournament(name,start,end,address)    
        self.controler.create_tournament(name = name ,start = start,end=end,address = address) 
    
    def ask_name(self):
        name = input("Nom : ")
        if name == "":
            print("Veuillez indiquer un nom")
            return None
        if len(name) >= 100:
            print("Le nom est trop long (limité a 99 caracteres)")
            return None
        # tester nom disponible
        return name
    
    
    def date_event(self,question):
        format = "%d/%m/%Y %H:%M"
        event = input(question)
        try:
            event = datetime.strptime(event,format)
        except ValueError:
            print("La date doit etre au format jj/mm/aaaa heure:min")
            return None
        now = datetime.now()
        if now > event:
            print("Pas de date du passé  ")
            return None
        return event
    
    def menu(self,welcome):
    
        if  welcome :
            print("Salut fdp, tu es dans lme menue qui te facilitera surement ton travail" )
        print("Tu as le choix entre : ") 
        print("1 : joueur")
        print("2: tournois")
        print("3: Histoirque des joueurs et des maths ")
        print("4: connaitre quand aura lieux le match de ton choix  ")
        choose = input("Fait ton choix (met un chiffre)")
        
        if choose == "1":
        # print("ok super te voila dans le menue des joueurs. Tu pourras cree tes joeurs saisir leur nom, prenom et autres ")
            self.player_menue()
        elif choose == "2":
            print("ok super te voila dans le menue des tournois . Tu pourras cree tes tournois  en indiquant son nom et les tours ou consulter fdp ")
                    
        elif choose == "3":
            print("Te voila dans l'historique. Tu pourras consulter toutes les donnnes et  voir les stats des joueur  notamment les plus nuls haha ")
            ## faire le menue des 3 categories 
            
        # elif choose == "4":
        #     display_name_and_date()
        else:
            print("Ce choix n'est pas dispo")
            
            
        #Rajoter une categorie sauvegarder


    def player_menue(self):
        # Consulter ou Creer joueur
        print ("1 : Consulter ")
        print("2 : Creation  ")
        print("")
        choose = input("Ta le choix entre consulter ou creer fdp (pas les deux en meme temps) ")
        
        if choose == "1":
            print("")
            
            print("Ok tu as fait le choix de consulter ")
            self.consulter_player()
            
            
            
        
        if choose == "2":
            print("te voila dans le menue creation fdp, ta cru on etait dans un jeux video ")
            self.player_creation()



    def player_creation(self):
        name = input("Name")
        first_name = input("first_name")
        id= input('ID')
        born = input("Born")
        self.controler.add_player(name, first_name, born,id)
        
        
        print("Ton joueur a ete crer fdp")
        

        self.player_menue()
        
        
        
    def ask_adress(self):
        adress = input("Quelle est l'adress : ")
        if adress == "":
            print("Veuillez indiquer un nom")
            return None
        if len(adress) >= 100:
            print("Le nom est trop long (limité a 99 caracteres)")
            return None
        # tester nom disponible
        return adress

    # def menu(self,welcome):
    
    #     if  welcome :
    #         print("Salut fdp, tu es dans lme menue qui te facilitera surement ton travail" )
    #     print("Tu as le choix entre : ") 
    #     print("1 : joueur")
    #     print("2: tournois")
    #     print("3: Histoirque des joueurs et des maths ")
    #     choose = input("Fait ton choix (met un chiffre)")
    
    #     if choose == "1":
    #     # print("ok super te voila dans le menue des joueurs. Tu pourras cree tes joeurs saisir leur nom, prenom et autres ")
    #         player_menue()
    #     elif choose == "2":
    #         print("ok super te voila dans le menue des tournois . Tu pourras cree tes tournois  en indiquant son nom et les tours ou consulter fdp ")
                    
    #     elif choose == "3":
    #         print("Te voila dans l'historique. Tu pourras consulter toutes les donnnes et  voir les stats des joueur  notamment les plus nuls haha ")
    #         ## faire le menue des 3 categories 
    #     else:
    #         print("Ce choix n'est pas dispo")
            
        
    #Rajoter une categorie sauvegarder
    # def consulter_player(self):
    #     for index, player in enumerate(list_player):
    #         print(f"first name ='{player.first_name}'; name ='{player.name}; born ='{player.born}'; id = '{player.id}'")
    #     self.back_to_menue_or_creation()
    
    def creer_tournament(self):
        name = self.ask_name()
        quand = self.date_event("Ca commence quand fdp ?")
        Tournament(name,quand)
        
    def back_to_menue_or_creation(self):
        print("")
        reponse = input("Souhaite tu consulter d'autre joueurs: yes ou no ?")
        
        if reponse == "yes":
            self.consulter_player()

        elif reponse =="no":
            self.player_menue()
            
    def creer_tournament(self):
        name = self.ask_name()
        quand = self.date_event("Ca commence quand fdp ?")
    
        Tournament(name,quand)
        
    def afficher_tournois(self):
        for index, Tournament in enumerate(list_tournois):
            print(f"Le tournois '{Tournament.name}'; qui aura lieu ='{Tournament.address}; le  ='{Tournament.start}'; et finira le  = '{Tournament.end}'")

    
    def consulter_player(self):
        for index, player in enumerate(self.controler.get_list_players()):
            print(f"first name ='{player.first_name}'; name ='{player.name}; born ='{player.born}'; id = '{player.id}'")
        self.player_menue()
    #name_liste_des_joueur_creer =liste_joueur_creer[0]
    
   #liste_des_joueurs = ["Hector","David", "Brian"]  #rajouter nom et/ou ID ; il faut stocker 
    #liste_des_joueurs.append(name_liste_des_joueur_creer)
    #print(*liste_des_joueurs)
    
    
    #choose = input("selectionne un joueur ")
    # if choose == 'Hector':
    #     hector = Player(name ="Roulias", first_name ="Hector", born= "11/11/2011",id="AB23333")
    #     print("Nom :"+hector.name, "Prenom " +hector.first_name, "ID :"+hector.id, "Né le : "+ hector.born)
    #     back_to_menue_or_creation()
        
    # elif choose == "David":
    #     david = Player(name="ROLLAS ",first_name="David ",born="22/22/2012",id="AB2333")
    #     print("Prenom " +david.first_name,"Nom :"+david.name,"Né le : "+david.born, "ID :"+david.id)
    #     print("")
    #     back_to_menue_or_creation()
        
    # elif choose == "Brian":
    #     brian = Player("Kollos","Brian", "12/02/1999","AB23333")
    #     print("Nom :"+brian.name, "Prenom " +brian.first_name,"Né le : "+brian.born,"ID :"+brian.id)
    #     back_to_menue_or_creation()
    
    
    
        
    # Une fois qu'il a consulter il retourne en arriere pl
  
    def display_name_and_date(self):
    # ● nom et dates d’un tournoi donné ;
    # faire un disctionnaire
    # JE CHERCHE LE TOURNOIS rolland 
        #et je trouve tout les infio lié au tournois 
        print("Tu souhaites savoir quand est ce qu'aura lieu un tournois ?")
        print("Rentre son nom juste en bas ")
        tournoi = input("Nom du tournois  ")
        
        result = {}
    
        name = self.ask_name(name)
        date = self.date_event()
    #
        result[name] = date
        print(f"le tournois {name} aura lieu le {date}")
        print("Super ta vue ce que tu voulais ? Nice. On peut passer au chose suivante")
        
    
    
    
# fire une classe vue ou je met toute mes method de dans
#==> mettre dans le init de ma view il y a ura la creation de l'instance du controler => self.controler= controler





list_tournois = [
    
    Tournament(name = "", address= "", start= "", end= "", )

]

    
    



    