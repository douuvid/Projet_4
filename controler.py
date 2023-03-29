# Le controler utilise le model et les view comme bion lui semble sert de navigation
# lci c'est la view qui stock le controleur. C'est la view qui questionne le controleur 
# c'est lui qui decide qui joue avec qui(c'est le cerveau) ensuite stock lle round dans tournois



from models import Player, PlayerManager
from models import TournamentManager


class Controler:
    def __init__(self):
        #model
        self.player_manager = PlayerManager()
        self.tournament_manager = TournamentManager()
        
        pass
    

    def add_player(self, name, first_name, born, id):
        
        player = Player(name, first_name, born,id)
        self.player_manager.add_player(player)
        
    
    def get_list_players(self):
        
        return self.player_manager.list_player
        
        
    def save(self):
        self.player_manager.save()
        
    def create_tournament(self,name, start ,end,address):
        print(name,start,end,address)
        
    def get_player_by_id(self,id):
        list_player=self.player_manager.list_player
        for player in list_player:
            if player.id == id:
                return player
            
        raise Exception(f"Le joueur avec l'id : {id}, n'existe pas")
    
    def get_list_tournement(self):
        return self.tournament_manager.list_tournaments
        
    
