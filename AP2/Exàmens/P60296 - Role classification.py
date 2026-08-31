import yogi
from typing import TypeAlias


class Player:

    def __init__(self) -> None:
        self.elo = 1200
        self.connected = True
    
    def get_elo(self) -> int:
        return self.elo
    
    def is_connected(self) -> bool:
        return self.connected
    
    def connect(self) -> None:
        self.connected = True
    
    def disconnect(self) -> None:
        self.connected = False

    def change_elo(self, n: int) -> None:
        self.elo = max(self.elo + n, 1200)

Database: TypeAlias = dict[str, Player] #ID player, [elo, connected]

class Dataserver:

    def __init__(self) -> None:
        self.database: Database = {}
    
    def login(self, player: str) -> None:
        if player in self.database:
            self.database[player].connect()
        else:
            self.database[player] = Player()
    
    def logout(self, player: str) -> None:
        if player in self.database:
            self.database[player].disconnect()
    
    def play(self, player1: str, player2: str) -> bool:
        if (player1 in self.database) and self.database[player1].is_connected() and (player2 in self.database) and self.database[player2].is_connected():
            self.database[player1].change_elo(10)
            self.database[player2].change_elo(-10)
            return True
        else: 
            return False
    
    def get_elo(self, player: str) -> int:
        if player in self.database: 
            return self.database[player].get_elo() 
        else: 
            return 0
    
    def ranking(self) -> list[tuple[str, int]]:
        return sorted(((player, stats.get_elo()) for player, stats in self.database.items()), key=lambda x: (-x[1], x[0]))

def main() -> None:
    dataserver = Dataserver()

    for op in yogi.tokens(str):
        if op == "LOGIN":
            p1 = yogi.read(str)
            dataserver.login(p1)

        elif op == "LOGOUT":
            p1 = yogi.read(str)
            dataserver.logout(p1)

        elif op == "PLAY":
            p1 = yogi.read(str)
            p2 = yogi.read(str)
            if not dataserver.play(p1, p2):
                print(f'player(s) not connected')

        elif op == "GET_ELO":
            p1 = yogi.read(str)
            elo = dataserver.get_elo(p1)
            if elo:
                print(f'{p1} {elo}')
    
    print('\nRANKING')
    leaderboard = dataserver.ranking()
    for persona in leaderboard:
        print(persona[0], persona[1])

if __name__ == "__main__":
    main()