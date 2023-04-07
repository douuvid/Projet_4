from datetime import datetime,date
import json
from types import NoneType
import random
    

class Tournament():
    
    def __init__(self,name,address,start:datetime,end:datetime,nb_rounds = 4 ,description = "",round_list = [],players=[],index_current_round=0,is_open = True,): # les element necessaire pour creer un tournois (obligatoire)
        self.name = name
        self.address = address
        self.start = start
        self.end = end
        self.nb_rounds= nb_rounds
        self.description = description
        self.round_list = round_list
        self.players = players
        self.index_current_round = index_current_round
        self.is_open = is_open
        
        # ceux qui a l 'interieur sont tous les attribut (variable) qu'on stockera 
        
        
        
    def to_dict(self):
        
        
        dico= {"name": self.name,  
                    "address":self.address, 
        "start":self.start.isoformat(),
        "end":self.end.isoformat(), 
        "nb_rounds":self.nb_rounds,
        "description":self.description, 
        "round_list":[round.to_dict()for round in self.round_list], 
        "players": [ (player[0].to_dict(),player[1])for player in self.players], 
        
        #newlist = [x.upper() for x in fruits] 
        "index_current_round":self.index_current_round,
        "is_open": self.is_open
        }
        return dico
    
    
    @classmethod
    def from_dict(self,dict):
        
        #condition pour player et un round
        
        if "id" in  dict:
            return Player.from_dict(dict)
        
        if "matchs" in dict:
            return Round.from_dict(dict)
        return Tournament( dict["name"],dict["address"],datetime.fromisoformat(dict["start"]),datetime.fromisoformat(dict["end"]),dict["nb_rounds"],dict["description"],[],[],dict["index_current_round"],dict["is_open"])
    
   
            
        
    def register_player(self,player):
        for pl in self.players:
            if pl[0].id == player.id: ## 
                raise Exception("le joueur avec l'id "+ player.id +" est deja inscrit ")
        self.players.append((player,0))
    ######è
    
    def __str__(self):
        return f"{self.name},{self.start},{self.end}{self.address}{self.description}"
    
    def close_tournament(self):
      self.is_open= False
      
    def add_score_to_player(self,score:int,player:Player):
        for pl in self.players:
            if pl[0].id == player.id:
                pl[1] += score
                break
        else:
            raise Exception ("Impossible d'ajouter  le score au joueur , joueur inexistant ")
        
    
   
    
class TournamentManager():
    def __init__(self,save_file_name= "tournaments.json"):
    
        self.save_file_name = save_file_name
        self.list_tournaments= []
        self.load()
    
    def add_tournament(self, tournament:Tournament):
        self.list_tournaments.append(tournament)
    
    
    def close_tournament(self,name:str):
        for tournament in self.list_tournaments:
            if tournament.name == name:
                tournament.close_tournament()
                break
            
        else:
            raise Exception(f"Le tournois : {name} est inconnu")
            
      
     
      
    def save(self):
        try:
            save_file = open (self.save_file_name ,"w+")
        
            json.dump([tournament.to_dict()for tournament in self.list_tournaments],save_file)
        
            save_file.close()
        
        except Exception as error:
            raise Exception ("Error saving tournament info : ",error)
        
    # penser a ferme le fichier
    
    
    
    def trier(self): 
        self.list_tournaments.sort(key=lambda tournament:tournament.start)
        
        
        
    def load(self):
        try:
            
            save_file = open (self.save_file_name,"r")
        
            
            self.list_tournaments = json.load(save_file, object_hook= lambda dict: Tournament.from_dict(dict))
            save_file.close()
        
        except Exception as error:
            print("Error loading tournament info : ",error)
        
    
    def get_open_tournaments(self):
        open_tournaments = []
        
        for tournament in self.list_tournaments:
            if tournament.is_open:
                open_tournaments.append(tournament)
        return open_tournaments
                
        
        
    
    
class Player():
        
    def __init__(self,name,first_name,born:date,id):
            self.name = name
            self.first_name = first_name
            self.id = id
            self.born = born
            
            
    def __str__(self):
        return f"{self.name},{self.first_name},{self.id}{self.born}"
    
    def __repr__(self):
        return f"< Player name:{self.name} first_name:{self.first_name} id:{self.id} born:{self.born} >"
    
    def to_dict(self):
        #retourner un dictionnaire et chaque attrivbut dans tournament il va le mettre dans un dictionnaire

        dico= {"name": self.name,  
                    "first_name":self.first_name, 
        "id":self.id,
        "born":self.born.isoformat()
        }

        return dico
    @classmethod
    def from_dict(self,dict):
        return Player(dict["name"],dict["first_name"],date.fromisoformat(dict["born"]),dict["id"])
        
        



class PlayerManager():
    
    def __init__(self,save_file_name= "players.json"):
        
        self.save_file_name = save_file_name
        self.list_player= []
        self.load()
        
        
    def save(self):
    
        try:
            save_file = open (self.save_file_name ,"w+")
            json.dump([player.to_dict() for player in self.list_player],save_file)
            save_file.close()
        
        except Exception as error:
            print("Error saving players info : ",error)
        
    # penser a ferme le fichier
    
    def add_player(self, player:Player):
        for pl in self.list_player:
            if pl.id == player.id:
                raise Exception (f"Le joueur avec {pl.id} existe deja ")
                
        self.list_player.append(player)
    
    def trier(self): 
        self.list_player.sort(key=lambda player:player.id)
        
        
        
    def load(self):
        try:
            save_file = open (self.save_file_name,"r")
            self.list_player = json.load(save_file, object_hook= lambda dict: Player.from_dict(dict))                            
            save_file.close()
        
        except Exception as error:
            print("Error loading players info : ",error)
        
    #au lieu d'avoir un tableau de player avoir un tableau de dictionnaire dans la fonction save 
        
        


class Round(object):# capable de faire 
    def __init__(self,name,matchs= [],start:datetime | NoneType = None,end: datetime | NoneType = None):
        self.matchs = matchs
        self.start = start
        self.end = end
        self.name= name
    
    
    def start(self):
        self.start= datetime.now()
       
    def end(self):
        self.end = datetime.now()
        
        
        
    def add_match(self,player1, player2):
        playerA = [player1, None]
        playerB = [player2, None]
        _match =(playerA,playerB) 
        self.matchs.append(_match)
        
    def count_points(self,player_win):
        #faire une fonction qui compte les poiint 
        #l'idee serait de se dire qu'a chaque fois un joueur gagne un point lui ai attribue 
        total_de_point = 0
        
        pass
    
    def to_dict(self):
        dico= {"name": self.name,  
                    "matchs":self.matchs, 
        "start":self.start,
        "end":self.end, 
        }
        if self.start is not None:
            dico ["start"]=self.start.isoformat()

        if self.end is not None:
            dico ["end"]=self.end.isoformat()

        return dico
    @classmethod    
    def from_dict(self,dict):
        
        if dict["start"] is not None:
            dict["start"]=datetime.fromisoformat(dict["start"])
            
        if dict["end"] is not None:
            dict["end"]=datetime.fromisoformat(dict["end"])
            
            
        return Round(dict["name"],dict["matchs"],dict["start"],dict["end"])
    
    def mixe_player (self,):
        
        list_player = []
        
        
        
        
    def mixe_player_after_match (self):
        pass
        
        
        
    def add_new_round(self,players):
        return
        
        
    #rajouter une methode news round 
    # comptabilite les point 

    


# joueur = Player("DAVV","rAVO", "12/12/2000", "293847")
# player_manager =PlayerManager()
# player_manager.add_player(joueur)
# player_manager.save()


# tournois= Tournament("rollan","nohio","12/12/2026","12/12/2046","3","vtoenv")
# tournois.register_player(joueur)
# tournament_manager =TournamentManager()
# tournament_manager.add_tournament(tournois)
# tournament_manager.save()
