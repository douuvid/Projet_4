# Le controler utilise le model et les view comme bion lui semble sert de navigation
# lci c'est la view qui stock le controleur. C'est la view qui questionne le controleur 
# c'est lui qui decide qui joue avec qui(c'est le cerveau) ensuite stock lle round dans tournois

from models import Player, PlayerManager,Round
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
    
    def get_open_tournaments(self):
        return self.tournament_manager.get_open_tournaments()
        
    
    
    # result_match : 1  = joueur 1 gagner
    # result_match : 2 = joueur 2 gagne
    # result_match : 0: egalite
    
    def end_match(self,match,tournament:Tournament,result_match:int):

        
        if result_match == 1:
            match[0][1] = 2
            match[1][1] = 0
            
            
        elif result_match == 2:
            match[0][1] = 0
            match[1][1] = 2
            
            
        elif result_match == 0:
            match[0][1] = 1
            match[1][1] = 1
        
        
        
        elif len(match) > tournament.nb_rounds:
            raise Exception ("Fin du round")
        else:
            raise Exception ("Choisi 1,2 ou 0 fdp")
        
        tournament.add_score_to_player(match[0][1],match[0][0])# les scores
        tournament.add_score_to_player(match[1][1],match[1][0])
        try:
            last_round=tournament.get_last_round()
            
            for m in last_round.matchs:
                if m[0][1] == None  or m [1][1] == None:
                    break
            else:    
                last_round.end_round()
                
            
        except Exception as error :
            raise Exception (f"Impossible de recuperer le dernier round : {error}")
            
        

        
        
        
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
        tournament.register_player(player)
        
        
    def get_last_round(self,tournament:Tournament):
        if len(tournament.round_list) == 0:
            raise Exception ("No round on this tournament")
        return tournament.round_list[-1]
    
    
    def start_round(self,tournament:Tournament):
        #◊◊Le start des round est sensé créer les matchs 
        tournament.create_next_round()
        
        
        
        
        
    

    
