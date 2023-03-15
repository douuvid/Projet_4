# Le controler utilise le model et les view comme bion lui semble sert de navigation
# lci c'est la view qui stock le controleur. C'est la view qui questionne le controleur 
# c'est lui qui decide qui joue avec qui(c'est le cerveau) ensuite stock lle round dans tournois



from models import Player, PlayerManager


class Controler:
    def __init__(self):
        #model
        self.player_manager = PlayerManager()
        pass
    

    def add_player(self, name, first_name, born, id):
        
        player = Player(name, first_name, born,id)
        self.player_manager.add_player(player)
        
    
    def get_list_players(self):
        return self.player_manager.list_player
        
        
    
    
