from datetime import datetime
import sys
from collections.abc import Callable
from controler import Controler
from prettytable import PrettyTable
import json

class View(object): 
     
    def __init__(self):
        self.controler = Controler()
        
    # __________________________________________MENU___________________________________
    def menu(self,welcome=False):
    
        if  welcome :
            print("Salut fdp, tu es dans le menu qui te facilitera surement ton travail" )
        print("Tu as le choix entre : ") 
        print("1: Joueur")
        print("2: Tournois")
        print("3: Histoirque des joueurs et des maths ")
        print("4: Connaitre quand aura lieux le match de ton choix  ")
        print("5: Sauvegarde")
        choose= None
        while choose == None:
            choose = self.ask_string("Fait ton choix (met un chiffre)")
           
        if choose == "1":
        # print("ok super te voila dans le menu des joueurs. Tu pourras cree tes joeurs saisir leur nom, prenom et autres ")
            self.player_menu()
        elif choose == "2":
            self.tournament_menu()
                
        elif choose == "3":
            print("Te voila dans l'historique. Tu pourras consulter toutes les donnnes et  voir les stats des joueur  notamment les plus nuls haha ")
            ## faire le menu des 3 categories =
            #l'idee serait de pouvoir recupere les info d'un joueur precis ?

        elif choose == "4":
            pass
        elif choose =="5":
            self.controler.save()
            print("\nCa a bien ete sauvegarde \n")
            
        else:
            self.exit_back(choose,sys.exit)
            
       #_______________________________PLAYER_____________________________________     
    def player_menu(self):
        print ("\n1 : Consulter\n")
        print("\n2 : Creation \n")
        print(" \n3 : Recherche par identifiant\n")
        print("")
        choose = None
        while choose == None:
            choose = self.ask_string("Ta le choix entre consulter ou creer fdp (pas les deux en meme temps) ")
        
        if choose == "1":
            print("")
            self.consulter_player()
            
        elif choose == "2":
            print("te voila dans le menu creation fdp, ta cru on etait dans un jeux video ")
            self.player_creation() 
    
        elif choose == "3":
            self.player_data()
        else:
            #self.exit_back(choose, self.menu)
            pass
            
    def consulter_player(self):
        list_player= self.controler.get_list_players()
        for index,player in enumerate(list_player):
            print(f"{index + 1}. first name ='{player.first_name}'; name ='{player.name}; born ='{player.born}'; id = '{player.id}'")
        print(f"Il y a {len(list_player)}  joueur(s) enregistré(s) ")
        self.player_menu()
        
    
    def player_creation(self):
        name =first_name=id =born = None
        while name == None :
            name = self.ask_string("Name: ")
        while first_name == None :
            first_name = self.ask_string("first_name")
        while id == None :
            id= self.ask_string('ID: ')
        while born == None :
            born = self.ask_date("Born: ",False)
        
        
        try:
            
            
            self.controler.add_player(name, first_name, born,id)
            print(f"Ton joueur : {name} avec l'id :{id} a ete crée fdp")
        
        except Exception as error:
            print("Impossible de creer le joueur : ",error)
            
        self.player_menu()
    
    def player_data(self,):
        print("Tu souhaites connaitres toutes les info sur un joueur ?")
        id = None
        while id == None:
            id= self.ask_string("Rentre son id juste en bas ")
        try:
            
            player =self.controler.get_player_by_id(id)
            print(f"first name ='{player.first_name}'; name ='{player.name}; born ='{player.born}'; id = '{player.id}'")
        except Exception as error:
            print("Impossible d'afficher les données du joueur : ",error)
        self.player_menu()
    
    #__________________________ TOURNAMENT ____________________________________
    
    def tournament_menu(self):
        print("\nOk Super te voila dans le menu des tournois tu as le choix entre : \n")
        print("\n1 :Creer un tournois  \n")
        print("\n2: Consulter un tournois fdp \n ")
        print("\n3: Inscrire un joueur au tournois fdp \n ")
        print("\n4: Gerer les match fdp \n ")
        choose = None
        while choose == None:
            choose = self.ask_string("Indique ton choix")
        if choose == "1":
            self.debut_tournois()
        elif choose == "2":
            self.consulter_tournois()
            
        elif choose == "3":
            self.inscription()
            
        elif choose =="4":
            self.end_match()
        else:
            self.exit_back()
        
    
    def debut_tournois(self):#
        print("\nEntre les info pour la creation d'un tournois fdp \n")
        my_table= PrettyTable()
        my_table.field_names= ["Nom", "Date de debut","Date de fin","Adresse"]
        
        name, start, end, address = None, None, None, None
        while name == None:
            name = self.ask_string("Nom du tournois? svp fdp")
        while end == None or start >= end :
            if end != None:
                start, end = None, None
                print("La date de début est supérieure à la date de fin")
            
            while start == None:
                start = self.ask_date("Quelle est la date de début du tournois ? : ",True)
                now = datetime.now()
                if start != None and now > start:
                    print("Pas de date du passé  ")
                    start = None
                
            while end == None:
                end = self.ask_date("Quelle est la date de fin du tournois ? : ",True)
            #print(f"C'est bien fdp ta initialiser le tournois sous le nom de {name} qui commencera le '{start}'et se terminera le '{end}'; ".format(name,start,end))
                now = datetime.now()
                if end != None and now > end:
                    print("Pas de date du passé  ")
                    end = None
                    
        while address == None:
            address = self.ask_string("Quelle est votre adress")
        
        my_table.add_row([name,start,end,address])
        print(my_table)
      
        self.controler.create_tournament(name,start,end,address)    
        #self.controler.create_tournament(name = name ,start = start,end=end,address = address)
        
        
    def consulter_tournois(self):
        list_tournois = self.controler.get_list_tournement()
        
        if (list_tournois is not None) and len(list_tournois) != 0:
            for list in list_tournois:
                print(list)
        else:
           print("\nIl n'y a pas de tournois\n ")
        
        
        
    def inscription(self):
        print("\n Bonjour vous voici dans l'etape de l'inscription")
        try:
            name,id_player= None,None
            while name == None:
                name =self.ask_string("Rentrer le nom  du tournois  ")
            tournament =self.controler.get_tournement_by_name(name)
            while id_player == None:
                id_player = self.ask_string("Rentrer l'id  du joueur ")
            player=self.controler.get_player_by_id(id_player)
            self.controler.register_player_to_tournament(player,tournament)
            print("le joueur a bien ete inscrit ")
        except Exception as error: 
            print(f"Inscription du joueur impossible dans le tournois {name}:",error)
            self.tournament_menu()
            
        
    def end_match(self):
        selected_tournament= self.ask_tournament()
        print(selected_tournament.name)
        last_round =self.controler.get_last_round(selected_tournament)
        select_match = self.ask_match(last_round)
        
        print(select_match)
        
        tableau_score = [1,2,0]
        score = None
        while score == None :
            score =self.ask_int("\nQui a gagne ?\n 1 : Joueur 1\n 2 : Joueur 2 \n 0 : Egalité ") 
            if score != None and score not in tableau_score :
                print("Tu t'es tromper selectionne un chiffre (1,2 ou 0)")
        
    
        self.controler.end_match(select_match,selected_tournament, score)
        
        
        #end= self.ask_string("Quel match est termine ? ") 
        
        
        # Le match est termine == Oui
        #Le match n'est pas terminnne == None 
        
        
        
    #___________________________TOOLS________________________________
    def ask_string(self,question:str):
        
        name = input(question)
        if name == "":
            print("Reponse vide")
            return None
        if len(name) >= 100:
            print("Reponse trop longue fdp (limité a 99 caracteres)")
            return None
        return name
    
    def ask_date(self,question,time:bool= False):
        format = "%d/%m/%Y"
        date = input(question)
        
        if time :
            format = format + " %H:%M" 
        
        try:
            
            date = datetime.strptime(date,format)
            if not time:
                date = date.date()
            
        except ValueError:
            error ="La date doit etre au format jj/mm/aaaa "
            if time :
                error = error + "heure:minute"
            print(error)
            return None
        
        return date
    
    def ask_int(self,question:str):
        try:
            return int(input(question))
    
        except Exception as error :
            print(f"Pas un nombre : ",error)
            return None
    

    def ask_tournament(self):
        index = 1
        open_tournaments=self.controler.get_open_tournaments()
        if len(open_tournaments) ==0:
            print("Aucun tournois en cours ")
            self.tournament_menu()
            return 
        for tournement in open_tournaments:
            print(f"{index} : {tournement.name}")
        
        index_choose = None
        while index_choose == None:
            index_choose = self.ask_int("Quel est le tournois concerné ?")
            if index_choose != None and (index_choose  > len(open_tournaments) or index_choose <1):
                index_choose = None
                print("Mauvais choix fdp")
                
        return open_tournaments[index_choose -1] 
        
    def ask_match (self,last_round):
        index = 1 
        if len(last_round.matchs) == 0:
            print('Aucun match en cours')
            self.tournament_menu()
            return
        
        for matchou in last_round.matchs:
            print(f"{index}:{matchou[0][0].name} vs {matchou[1][0].name}")
            
        indexou_choose = None
        while indexou_choose == None :
            indexou_choose = self.ask_int("Quel est le match concerne")
            if indexou_choose!= None and (indexou_choose > len(last_round.matchs) or indexou_choose < 1):
                indexou_choose = None
                print("Mauvais choix de match  fdp")
                
        
        return last_round.matchs[indexou_choose-1]
   
   
    def exit_back(self,choose:str,back:Callable):
        if choose == "exit" :
            sys.exit()
        elif choose == "back":
            back()
            
        else:
            print("\nCe choix n'est pas dispo ou n'existe pas \n")
            
    

    


#30/mars:
# Pb sur la sauvegarde des tournois, l
# Probleme  de date transformer les date qui sont en string pour json
#Pb de deserialisation pour j son avec model > to_dict 
# Creer une fonction ou on pourra modif le player 
# Apres sauvegarde et chargement des tournois 
#==> tester : creeer un tournois dans lequel on aura mit un player  , apres saubvegarder , redemarrer l'appli
#==> modif le player (ex modif : nom), apres afficher la lister des player dans le tournois.
#Le comportement qu'on aura(apres avoir fait ce qui y a ete mit en amont ) la modif sur le player n'apparaitrra pas dans le tournois
# Donc resoudre se probleme
# le probleme vient de fair eun to_dict sur player ligne 41(player du torunois)+ le chargement doit se faire autrement 


    