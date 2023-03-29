from datetime import datetime
import sys
from collections.abc import Callable
from controler import Controler
from models import Tournament

# Gérer les tournois: création d'un tournoi, afficher la liste des tournois
# Gérer la sauvegarde et le rechargement des tournois, comme pour les joueurs
# Gérer l'ajout de joueurs dans un tournoi
# Faire évoluer la sauvegarde/rechargement des tournois en ajoutant la sauvegarde/rechargement des joueurs des tournois

class View(object): 
    
    def __init__(self):
        self.controler = Controler()
        
    def menu(self,welcome=False):
    
        if  welcome :
            print("Salut fdp, tu es dans le menu qui te facilitera surement ton travail" )
        print("Tu as le choix entre : ") 
        print("1: joueur")
        print("2: tournois")
        print("3: Histoirque des joueurs et des maths ")
        print("4: connaitre quand aura lieux le match de ton choix  ")
        print("5: Sauvegarde")
        choose = input("Fait ton choix (met un chiffre)")
        
        if choose == "1":
        # print("ok super te voila dans le menu des joueurs. Tu pourras cree tes joeurs saisir leur nom, prenom et autres ")
            self.player_menu()
        elif choose == "2":
            print("\nOk super te voila dans le menu des tournois tu as le choix entre : \n")
            print("\n1 :Creer un tournois  \n")
            print("\n2: Consulter un tournois fdp \n ")
            choose = input("Indique ton choix")
            if choose == "1":
                self.debut_tournois()
            elif choose == "2":
                self.consulter_tournois()
            
            
        elif choose == "3":
            
            print("Te voila dans l'historique. Tu pourras consulter toutes les donnnes et  voir les stats des joueur  notamment les plus nuls haha ")
            ## faire le menu des 3 categories =
            #l'idee serait de pouvoir recupere les info d'un joueur precis ?

        elif choose == "4":
             self.display_name_and_date()
        elif choose =="5":
            self.controler.save()
            print("\nCa a bien ete sauvegarde \n")
            
        else:
            self.exit_back(choose,sys.exit)
            
    
    def player_menu(self):
        # Consulter ou Creer joueur
        print ("\n1 : Consulter\n")
        print("\n2 : Creation \n")
        print(" \n3 : Recherche par identifiant\n")
        print("")
        choose = input("Ta le choix entre consulter ou creer fdp (pas les deux en meme temps) ")
        
        if choose == "1":
            print("")
            self.consulter_player()
            
        elif choose == "2":
            print("te voila dans le menu creation fdp, ta cru on etait dans un jeux video ")
            self.player_creation() 
    
        elif choose == "3":
            self.player_data()
        else:
            self.exit_back(choose, self.menu)
            
    def consulter_player(self):
        list_player= self.controler.get_list_players()
        for index,player in enumerate(list_player):
            print(f"{index + 1}. first name ='{player.first_name}'; name ='{player.name}; born ='{player.born}'; id = '{player.id}'")
        print(f"Il y a {len(list_player)}  joueur(s) enregistré(s) ")
        self.player_menu()
        
    
    def player_creation(self):
        name = input("Name: ")
        first_name = input("first_name")
        id= input('ID: ')
        born = input("Born: ")
        try:
            self.controler.add_player(name, first_name, born,id)
            print(f"Ton joueur : {name} avec l'id :{id} a ete crée fdp")
        
        except Exception as error:
            print("Impossible de creer le joueur : ",error)
            
        self.player_menu()
    
    def player_data(self,):
        print("Tu souhaites connaitres toutes les info sur un joueur ?")
        id= input("Rentre son id juste en bas ")
        try:
            
            player =self.controler.get_player_by_id(id)
            print(f"first name ='{player.first_name}'; name ='{player.name}; born ='{player.born}'; id = '{player.id}'")
        except Exception as error:
            print("Impossible d'afficher les données du joueur : ",error)
        self.player_menu()
    
    
    def tournament_menu(self):
        print("\n Ok te voila dans le menue tournois\n")
        
    
    def debut_tournois(self):#
        print("\nEntre les info pour la creation d'un tournois fdp \n")
        
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
        self.controler.create_tournament(name,start,end,address)    
        #self.controler.create_tournament(name = name ,start = start,end=end,address = address) 
    
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
    
    def ask_adress(self):
        address = input("Quelle est l'adress: ")
        if address == "":
            print("Veuillez indiquer un nom")
            return None
        if len(address) >= 100:
            print("Le nom est trop long (limité a 99 caracteres)")
            return None
        return address

        
    #Rajoter une categorie sauvegarder
    # def consulter_player(self):
    #     for index, player in enumerate(self.controler.list_player):
    #         print(f"first name ='{player.first_name}'; name ='{player.name}; born ='{player.born}'; id = '{player.id}'")
    #     self.back_to_menu_or_creation()
    
    def consulter_tournois(self):
        for index, Tournament in enumerate(self.controler.get_list_tournement()): #
            print(f"Le tournois '{Tournament.name}'; qui aura lieu ='{Tournament.address}; le  ='{Tournament.start}'; et finira le  = '{Tournament.end}'")
            pass
    
    def display_name_and_date(self):
    # ● nom et dates d’un tournoi donné ;
    # faire un disctionnaire
    # JE CHERCHE LE TOURNOIS rolland 
        #et je trouve tout les infio lié au tournois 
        print("Tu souhaites savoir quand est ce qu'aura lieu un tournois ?")
        print("Rentre son nom juste en bas ")
        
        name = self.ask_name(name)
        #FIXME : FINIR IMPORTANT 
        # result[name] = date#
        # print(f"le tournois {name} aura lieu le {date}")
        # print("Super ta vue ce que tu voulais ? Nice. On peut passer au chose suivante")
        pass
    
    
    

   
    
    
    
    def exit_back(self,choose:str,back:Callable):
        if choose == "exit" :
            sys.exit()
        elif choose == "back":
            back()
            
        else:
            print("\nCe choix n'est pas dispo ou n'existe pas \n")

    



    