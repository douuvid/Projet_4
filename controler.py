# Le controler utilise le model et les view comme bion lui semble sert de navigation
# lci c'est la view qui stock le controleur. C'est la view qui questionne le controleur 
# c'est lui qui decide qui joue avec qui(c'est le cerveau) ensuite stock lle round dans tournois



from models import Player, PlayerManager
from models import TournamentManager,Tournament
from datetime import datetime


class Controler:
    def __init__(self):
        #model
        self.player_manager = PlayerManager()
        self.tournament_manager = TournamentManager()
        
    

    def add_player(self, name, first_name, born, id):
        if name == None or first_name ==None or born ==None or id == None:
            raise Exception("Impossible de creer le joeur ")
        player = Player(name, first_name, born,id)
        
        self.player_manager.add_player(player)
        
    
    def get_list_players(self):
        return self.player_manager.list_player
        
        
    def save(self):
        self.player_manager.save()
        self.tournament_manager.save()
        
    def create_tournament(self,name, start ,end,address):
        tournament = Tournament(name,address,start,end)
        self.tournament_manager.add_tournament(tournament)
        
        
    def get_player_by_id(self,id):
        list_player=self.player_manager.list_player
        for player in list_player:
            if player.id == id:
                return player
            
        raise Exception(f"Le joueur avec l'id : {id}, n'existe pas")
    
    def get_list_tournement(self):
        list_tournement =self.tournament_manager.list_tournaments
        return list_tournement
        
            
    
    def sav_tournament(self):
        self.tournament_manager.save()
        
    def get_tournement_by_name(self,name):
        tournaments=self.tournament_manager.list_tournaments
        for tournament in tournaments:
            if tournament.name == name:
                return tournament
            
        raise Exception(f"Le  tournois avec le nom: {name}, n'existe pas")
    
    
    def register_player_to_tournament(self,player:Player,tournament:Tournament):
        now = datetime.now()
        start=tournament.start
        if start < now:
            raise Exception ("Trop tard pour s'inscrire ")
        for pl in tournament.players:
            if pl.id == player.id:
                raise Exception(f"Le joueur avec l'id : {pl.id}, est deja inscrit")
            
        tournament.players.append(player)
        
        
        

        
    
