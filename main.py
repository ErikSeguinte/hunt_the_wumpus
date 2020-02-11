from typing import List, Tuple

class BaseGameException(BaseException): pass
class GameOver(BaseGameException): pass


class Main:

    def __init__(self):
        self.cave = None
        self.player = None

    def run_game_loop(self):
        raise NotImplementedError

    def get_input(self, valid_responses: List[str]) -> str:
        while True:
            choice = input('What do you do?\n')
            try:
                self.validate_input(valid_responses, choice)
            except ValueError:
                print("I don't know what that means. Try again.")
                continue
            else:
                print('choice accepted')
                break
        return choice

    @staticmethod
    def validate_input(valid_responses: List[str], choice:str):
        if choice not in valid_responses:
            raise ValueError

    def game_start(self):
        self.run_game_loop()

class Room:

    def __init__(self, label:int):
        self.label = label
        self.adjacent_rooms = None
        self.visited = False
        self.description = self.assign_description()
        self.contents = None

    @staticmethod
    def assign_description() -> str:
        return "Room Description"

    def enter(self):
        raise NotImplementedError


class Player:

    def __init__(self, num_arrows:int):
        self.num_arrows = num_arrows
        self.current_room = None
        self.adjacent_rooms = None

    def move(self, room:Room):
        raise NotImplementedError

    def shoot(self, room:Room):
        raise NotImplementedError

    def game_over(self):
        raise NotImplementedError


class Cave:

    def __init__(self):
        self.rooms = None

    def populate_rooms(self, map = None):
        self.rooms = [Room(i) for i in range(20)]
        print(self.rooms)

class Hazard:

    def __init__(self, nearby:str = ""):
        self.nearby = nearby

    def act():
        raise NotImplementedError

class Mobile(Hazard):

    def __init__(self):
        super().__init__()

    def move() -> str:
        raise NotImplementedError




if __name__ == "__main__":
    main = Main()
    choice = main.get_input({'hello', 'world'})
    print(f'Your choice was: {choice}')

    cave = Cave()
    cave.populate_rooms()


