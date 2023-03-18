import datetime
import json
    

class Tournament():
    
    def __init__(self,name,address,start,end,nb_rounds = 4 ,description = "",round_list = [],players=[],index_current_round=0): # les element necessaire pour creer un tournois (obligatoire)
        self.name = name
        self.address = address
        self.start = start
        self.end = end
        self.nb_rounds= nb_rounds
        self.description = description
        self.round_list = round_list
        self.players = players
        self.index_current_round = index_current_round
        # ceux qui a l 'interieur sont tous les attribut (variable) qu'on stockera 
        
    def to_dict(self):
        #retourner un dictionnaire et chaque attrivbut dans tournament il va le mettre dans un dictionnaire il vont aller dans round list
        print(self.players )
        print(self.round_list)
        dico= {"name": self.name,  
                    "address":self.address, 
        "start":self.start,
        "end":self.end, 
        "nb_rounds":self.nb_rounds,
        "description":self.description, 
        "round_list":[round.to_dict()for round in self.round_list], 
        "players": [ player.to_dict()for player in self.players], 
        
        #newlist = [x.upper() for x in fruits] 
        "index_current_round":self.index_current_round }
        
        return dico
    
    
    @classmethod
    def from_dict(self,dict):
        print(dict)
        #condition pour player et un round
        
        if "id" in  dict:
            return Player.from_dict(dict)
        
        if "matchs" in dict:
            return Round.from_dict(dict)
        return Tournament( dict["name"],dict["address"],dict["start"],dict["end"],dict["nb_rounds"],dict["description"],[],[],dict["index_current_round"])
    
   
            
        
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
        
            json.dump([tournament.to_dict()for tournament in self.list_tournaments],save_file)
        
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
        
            
            self.list_tournaments = json.load(save_file, object_hook= lambda dict: Tournament.from_dict(dict))
            save_file.close()
        
        except Exception as error:
            print("Error loading tournament info : ",error)
        
        pass
    
    





class Round(object):# capable de faire 
    def __init__(self,name,matchs= [],start= None,end = None):
        self.matchs = matchs
        self.start = start
        self.end = end
        self.name= name
        
        
        
        
    def add_match(self,player1, player2):
        playerA = [player1, None]
        playerB = [player2, None]
        _match =(playerA,playerB) 
        self.matchs.append(_match)
        
    def count_points(self,player_win):
        #faire une fonction qui compte les poiint 
        pass
    
    def to_dict(self):
        dico= {"name": self.name,  
                    "matchs":self.matchs, 
        "start":self.start,
        "end":self.end, 
        }

        return dico
    @classmethod    
    def from_dict(self,dict):
        return Round(dict["name"],dict["matchs"],dict["start"],dict["end"])
        
        

            
            

    
    def start(self):
        self.start= datetime.now()
        pass
        

        
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
    
    def to_dict(self):
        #retourner un dictionnaire et chaque attrivbut dans tournament il va le mettre dans un dictionnaire il vont aller dans round list

        dico= {"name": self.name,  
                    "first_name":self.first_name, 
        "id":self.id,
        "born":self.born,
        }

        return dico
    @classmethod
    def from_dict(self,dict):
        return Player(dict["name"],dict["first_name"],dict["born"],dict["id"])
        
        



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
    
        
            json.dump([player.to_dict() for player in self.list_player],save_file)
        
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
        
            
            self.list_player = json.load(save_file, object_hook= lambda dict: Player.from_dict(dict))
                                         
            save_file.close()
        
        except Exception as error:
            print("Error loading players info : ",error)
        
    #au lieu d'avoir un tableau de player avoir un tableau de dictionnaire dans la fonction save 
        
        
    

    


joueur = Player("DAVV","rAVO", "12/12/2000", "293847")
player_manager =PlayerManager()
player_manager.add_player(joueur)
player_manager.save()


tournois= Tournament("rollan","nohio","12/12/2026","12/12/2046","3","vtoenv")
tournois.register_player(joueur)
tournament_manager =TournamentManager()
tournament_manager.add_tournament(tournois)
tournament_manager.save()
