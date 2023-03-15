import datetime
import json
    

class Tournament():
    
    def __init__(self,name,address,start,end,nb_rounds = 4 ,description = ""): # les element necessaire pour creer un tournois (obligatoire)
        self.name = name
        self.address = address
        self.start = start
        self.end = end
        self.nb_rounds= nb_rounds
        self.description = description
        self.round_list = []
        self.players = []
        self.index_current_round = 0
        # ceux qui a l 'interieur sont tous les attribut (variable) qu'on stockera 
        
        #P
        
    def register_player(self,player):
        for pl in self.players:
            if pl.id == player.id: ## 
                print("le joueur avec l'id "+ player.id +" est deja inscrit ")
                return 
        self.players.append(player)
    ######è
    
    def __str__(self):
        return f"{self.name},{self.start},{self.end}{self.address}{self.description}"
    
   
    
class TournamentManager():
    def __init__(self,save_file_name= "tournaments.json"):
    
        self.save_file_name = save_file_name
        self.list_tournaments= [
        
        ]
        self.load()
        
        
    def save(self):
    
        try:
            save_file = open (self.save_file_name ,"w+")
        

            new_list= []
            
            for element in self.list_tournaments:
                
                new_list.append(element.__dict__)
        
            json.dump(new_list,save_file)
        
            save_file.close()
        
        except Exception as error:
            print("Error saving tournament info : ",error)
        
    # penser a ferme le fichier
    
    def add_tournament(self, tournament):
    
        self.list_tournaments.append(tournament)
    
    def trier(self): 
        self.list_tournaments.sort(key=lambda tournament:tournament.start)
        
        
        
    def load(self):
        try:
            
            save_file = open (self.save_file_name,"r")
        
            
            self.list_tournaments = json.load(save_file, object_hook= lambda dict:(dict["name"],dict["first_name"],dict["born"],dict["id"]))
            save_file.close()
        
        except Exception as error:
            print("Error loading tournament info : ",error)
        
        pass





class Round(object):# capable de faire 
    def __init__(self,round=1):
        self.matchs = []
        self.start = None
        self.end = None
        self.name= "Round " + str(round)
        
        
        
    def add_match(self,player1, player2):
        playerA = [player1, None]
        playerB = [player2, None]
        _match =(playerA,playerB) 
        self.matchs.append(_match)
        
        
    def start(self):
        self.start= datetime.now()
        

        
    def end(self):
        self.end = datetime.now()
        
    def add_new_round(self,players):
        return
        
        
        
    
    #rajouter une methode news round 
    # comptabilite les point 
    






class Player():
        
    def __init__(self,name,first_name,born,id):
            self.name = name
            self.first_name = first_name
            self.id = id
            self.born = born
            
    def __str__(self):
        return f"{self.name},{self.first_name},{self.id}{self.born}"
    
    def __repr__(self):
        return f"< Player name:{self.name} first_name:{self.first_name} id:{self.id} born:{self.born} >"



class PlayerManager():
    
    def __init__(self,save_file_name= "players.json"):
        
        self.save_file_name = save_file_name
        self.list_player= [
            # Player(name ="Roulias", first_name ="Hector", born= "11/11/2011",id="AB23333"),
            # Player(name="Rollas ",first_name="David ",born="22/22/2012",id="AB2333"),  
            # Player("Kollos","Brian", "12/02/1999","AB233")
            ]
        self.load()
        
        
    def save(self):
    
        try:
            save_file = open (self.save_file_name ,"w+")
        

            new_list= []
            
            for element in self.list_player:
                
                new_list.append(element.__dict__)
        
            json.dump(new_list,save_file)
        
            save_file.close()
        
        except Exception as error:
            print("Error saving players info : ",error)
        
    # penser a ferme le fichier
    
    def add_player(self, player):
    
        self.list_player.append(player)
    
    def trier(self): 
        self.list_player.sort(key=lambda player:player.id)
        
        
        
    def load(self):
        try:
            
            save_file = open (self.save_file_name,"r")
        
            
            self.list_player = json.load(save_file, object_hook= lambda dict:Player(dict["name"],dict["first_name"],dict["born"],dict["id"]))
            save_file.close()
        
        except Exception as error:
            print("Error loading players info : ",error)
        
    #au lieu d'avoir un tableau de player avoir un tableau de dictionnaire dans la fonction save 
        

    



