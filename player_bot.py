from game import Game
from collections import Counter


class e_player:
    # constructor, play and calcuate_score available
    def __init__(self):
        self.roll = None

    def _print(self, *args):
        print(args[0])

    def _input(self, *args):
        print(args[0], "n")
        return "n"


class bot_player:
    def __init__(self):
        self.roll = None
        self.game = None
        self.straight = False

    def _print(self, *args):

        msg = args[0]

        if msg.startswith("You rolled"):
            self.roll = [int(char) for char in msg if char.isdigit()]

        print(msg)

    def _input(self, *args):
        prompt = args[0]

        if prompt == "Wanna play? ":
            print(prompt, "y")
            return "y"

        if prompt == "Roll again? ":
            print(prompt, "n")
            return "n"

        if prompt == "Enter dice to keep: ":
            print(prompt)

            response_str = ""
            for val in self.roll:
                response_str += str(val)

            return response_str


if __name__ == "__main__":
    robot = bot_player()
    game = Game(robot._print, robot._input)
    robot.game = game

    game._play(15)
