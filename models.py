import json

class Player():
        
    def __init__(self,name,first_name,born,id):
            self.name = name
            self.first_name = first_name
            self.id = id
            self.born = born

            
     
    

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





class PlayerManager():
    
    def __init__(self):
        self.list_player= [
            Player(name ="Roulias", first_name ="Hector", born= "11/11/2011",id="AB23333"),
            Player(name="Rollas ",first_name="David ",born="22/22/2012",id="AB2333"),  
            Player("Kollos","Brian", "12/02/1999","AB23333")
            ]
        
    def save(self):
    
        try:
            
            save_file = open ("Ficher de sauvegarde","w")
        
            json.dump(self.list_player,save_file)
        
            save_file.close()
        
        except Exception as error:
            print(error)
        
    # penser a ferme le fichier
    
    def add_player(self, player):
    
        self.list_player.append(player)
    
