from datetime import datetime
import json

import random
from pickle import *
from models import Player, Tournament

from view import View

"""
Ici on a creer la class joueur pour pouvoir la reutiliser plus tard quand on voudra creeer des joueur 

""" 
# class Player():
        
#     def __init__(self,name,first_name,born,id):
#             self.name = name
#             self.first_name = first_name
#             self.id = id
#             self.born = born

            
     
    

# class Tournament():
    
#     kind = ' echec'
#     def __init__(self,name,address,start,end,nb_rounds = 4 ,description = ""): # les element necessaire pour creer un tournois (obligatoire)
#         self.name = name
#         self.address = address
#         self.start = start
#         self.end = end
#         self.nb_rounds= nb_rounds
#         self.description = description
#         self.round_list = []
#         self.players = []
#         self.index_current_round = 0
#         # ceux qui a l 'interieur sont tous les attribut (variable) qu'on stockera 
        
#         #P
        
#     def register_player(self,player):
#         for pl in self.players:
#             if pl.id == player.id: ## 
#                 print("le joueur avec l'id "+ player.id +" est deja inscrit ")
#                 return 
#         self.players.append(player)
#     ######è
    
#     def __str__(self):
#         return f"{self.name},{self.start},{self.end}{self.address}{self.description}"
        
   

# class View(object):
    
#     def ask_adress(self):
#         adress = input("Quelle est l'adress : ")
#         if adress == "":
#             print("Veuillez indiquer un nom")
#             return None
#         if len(adress) >= 100:
#             print("Le nom est trop long (limité a 99 caracteres)")
#             return None
#         # tester nom disponible
#         return adress
    
    
    
    
#     def debut_tournois(self):#
#         print("Entre les info pour la creation d'un tournois fdp ")
        
#         name, start, end, address = None, None, None, None
#         while name == None:
#             name = self.ask_name()
#         while end == None or start >= end :
#             if end != None:
#                 start, end = None, None
#                 print("La date de début est supérieure à la date de fin")
#             while start == None:
#                 start = date_event("Quelle est la date de début du tournois ? : ")
#             while end == None:
#                 end = date_event("Quelle est la date de fin du tournois ? : ")
#             print(f"C'est bien fdp ta initialiser le tournois sous le nom de {name} qui commencera le '{start}'et se terminera le '{end}'; ".format(name,start,end))
#             while address == None:
#                 address = ask_adress()
#         #self.controler.create_tournament(name,start,end,address)    
#         self.controler.create_tournament(name = name ,start = start,end=end,address = address) 
    
#     def ask_name(self):
#         name = input("Nom : ")
#         if name == "":
#             print("Veuillez indiquer un nom")
#             return None
#         if len(name) >= 100:
#             print("Le nom est trop long (limité a 99 caracteres)")
#             return None
#         # tester nom disponible
#         return name
    
    
#     def date_event(question):
#         format = "%d/%m/%Y %H:%M"
#         event = input(question)
#         try:
#             event = datetime.strptime(event,format)
#         except ValueError:
#             print("La date doit etre au format jj/mm/aaaa heure:min")
#             return None
#         now = datetime.now()
#         if now > event:
#             print("Pas de date du passé  ")
#             return None
#         return event
    
    
# def ask_name(self):
#     name = input("Nom : ")
#     if name == "":
#         print("Veuillez indiquer un nom")
#         return None
#     if len(name) >= 100:
#         print("Le nom est trop long (limité a 99 caracteres)")
#         return None
#         # tester nom disponible
#     return name

# def display_name_and_date(self):
#     # ● nom et dates d’un tournoi donné ;
#     # faire un disctionnaire
#     # JE CHERCHE LE TOURNOIS rolland 
#         #et je trouve tout les infio lié au tournois 
#         print("Tu souhaites savoir quand est ce qu'aura lieu un tournois ?")
#         print("Rentre son nom juste en bas ")
#         tournoi = input("Nom du tournois  ")
        
#         result = {}
    
#         name = ask_name(name)
#         date = date_event()
#     #
#         result[name] = date
#         print(f"le tournois {name} aura lieu le {date}")
#         print("Super ta vue ce que tu voulais ? Nice. On peut passer au chose suivante")


    
    

# class Controler:
#     def create_tournament(name,start,end,address):
#         tournament = Tournament(name,start,end,address)
        
    
    


# class Round(object):# capable de faire 
#     def __init__(self):
#         self.matchs = []
#         self.start = None
#         self.end = None
        
        
        
#     def add_match(self,player1, player2):
#         pass
        
        
#     def start(self):
#         self.start= datetime.now
        
#     def end(self):
#         self.end = datetime.now
        
#     def add_new_round(self,players):
#         return
        
        
        
    
#     #rajouter une methode news round 
#     # comptabilite les point 
    
    
    
# fire une classe vue ou je met toute mes method de dans
#==> mettre dans le init de ma view il y a ura la creation de l'instance du controler => self.controler= controler










# date de debut et fin du tournoir
# def debut_tournois(self):#
#     print("Entre les info pour la creation d'un tournois fdp ")
    
#     name, start, end, address = None, None, None, None
#     while name == None:
#         name = ask_name(name)
#     while end == None or start >= end :
#         if end != None:
#             start, end = None, None
#             print("La date de début est supérieure à la date de fin")
#         while start == None:
#             start = date_event("Quelle est la date de début du tournois ? : ")
#         while end == None:
#             end = date_event("Quelle est la date de fin du tournois ? : ")
#         print(f"C'est bien fdp ta initialiser le tournois sous le nom de {name} qui commencera le '{start}'et se terminera le '{end}'; ".format(name,start,end))
#         while address == None:
#             address = ask_adress()
#     #self.controler.create_tournament(name,start,end,address)    
#     self.controler.create_tournament(name = name ,start = start,end=end,address = address) 
   
    
        
                        
        
# def ask_adress():
#     adress = input("Quelle est l'adress : ")
#     if adress == "":
#         print("Veuillez indiquer un nom")
#         return None
#     if len(adress) >= 100:
#         print("Le nom est trop long (limité a 99 caracteres)")
#         return None
#     # tester nom disponible
#     return adress



# def date_event(question):
#     format = "%d/%m/%Y %H:%M"
#     event = input(question)
#     try:
#         event = datetime.strptime(event,format)
#     except ValueError:
#         print("La date doit etre au format jj/mm/aaaa heure:min")
#         return None
#     now = datetime.now()
#     if now > event:
#         print("Pas de date du passé  ")
#         return None
#     return event




# def menu(welcome):
    
#     if  welcome :
#         print("Salut fdp, tu es dans lme menue qui te facilitera surement ton travail" )
#     print("Tu as le choix entre : ") 
#     print("1 : joueur")
#     print("2: tournois")
#     print("3: Histoirque des joueurs et des maths ")
#     choose = input("Fait ton choix (met un chiffre)")
    
#     if choose == "1":
#        # print("ok super te voila dans le menue des joueurs. Tu pourras cree tes joeurs saisir leur nom, prenom et autres ")
#         player_menue()
#     elif choose == "2":
#         print("ok super te voila dans le menue des tournois . Tu pourras cree tes tournois  en indiquant son nom et les tours ou consulter fdp ")
                   
#     elif choose == "3":
#         print("Te voila dans l'historique. Tu pourras consulter toutes les donnnes et  voir les stats des joueur  notamment les plus nuls haha ")
#         ## faire le menue des 3 categories 
#     else:
#         print("Ce choix n'est pas dispo")
        
        
#     #Rajoter une categorie sauvegarder


# def player_menue():
#     # Consulter ou Creer joueur
#     print ("1 : Consulter ")
#     print("2 : Creation  ")
#     print("")
#     choose = input("Ta le choix entre consulter ou creer fdp (pas les deux en meme temps) ")
    
#     if choose == "1":
#         print("")
        
#         print("Ok tu as fait le choix de consulter ")
#         consulter_player()
        
        
        
    
#     if choose == "2":
#         print("te voila dans le menue creation fdp, ta cru on etait dans un jeux video ")
#         player_creation()



# def player_creation():
#     name = input("Name")
#     first_name = input("first_name")
#     id= input('ID')
#     born = input("Born")
#     player = Player(name, first_name, born,id)
#     list_player.append(player)
    
#     print("Ton joueur a ete crer fdp")
    

#     player_menue()
    
#     return player.name,player.first_name,player.born,player.id
    
    
    
    

# def consulter_player():
#     for index, player in enumerate(list_player):
#         print(f"first name ='{player.first_name}'; name ='{player.name}; born ='{player.born}'; id = '{player.id}'")
#     back_to_menue_or_creation()
    
    
    
    
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
    
    
    
        
#     # Une fois qu'il a consulter il retourne en arriere pl
# def back_to_menue_or_creation():
#     print("")
#     reponse = input("Souhaite tu consulter d'autre joueurs: yes ou no ?")
        
#     if reponse == "yes":
#         consulter_player()

#     elif reponse =="no":
#         player_menue()

    


# ● liste de tous les joueurs par ordre alphabétique ;
# def trier(): 
#     for index, player in enumerate(list_player): 
#         list_player_uno.append(player.name)
#         list_player_uno = sorted(list_player_uno)
        
#     print (list_player_uno)
    
    
#    Nous aimerions pouvoir afficher les rapports suivants dans le programme :


    
    

    
# ● liste de tous les tournois
# def afficher_tournois():
#     for index, Tournament in enumerate(list_tournois):
#         print(f"Le tournois '{Tournament.name}'; qui aura lieu ='{Tournament.address}; le  ='{Tournament.start}'; et finira le  = '{Tournament.end}'")
#     return None
        


        

        
        
        
        
# def creer_tournament():
#     name = ask_name()
#     quand = date_event("Ca commence quand fdp ?")
    
#     Tournament(name,quand)
    
    






# ● liste des joueurs du tournoi par ordre alphabétique ;
# ● liste de tous les tours du tournoi et de tous les matchs du tour.
    
# def save():
    
#     try:
        
#         save_file = open("data/tournaments","w")
    
#         json.dump(list_player,save_file)
    
#         save_file.close()
    
#     except Exception as error:
#         print(error)
    


# def go_tournois():
#     Un tournoi a un nombre de tours défini.
# ● Chaque tour est une liste de matchs.
# ○ Chaque match consiste en une paire de joueurs.
# ● À la fin du match, les joueurs reçoivent des points selon leurs résultats.
# ○ Le gagnant reçoit 1 point.
# ○ Le perdant reçoit 0 point.
# Centre échecs
# ○ Chaque joueur reçoit 0,5 point si le match se termine par un match nul


#Il faudrait juste indique qui a gagner ?
# On indique qui a joue donc joueur 1 vs joueur 2
# on indique le gzgnznt 
# et le 
 


if __name__ == "__main__":

    view = View()
    while True:
        view.menu(True)

