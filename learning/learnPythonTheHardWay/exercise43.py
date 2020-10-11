from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

            current_scene.enter()

class Death(Scene):

    quips = ["You died.  You kinda suck at this.","Your Mom would be proud...if she were smarter.","Such a luser.","I have a small puppy that's better at this.","You're worse than your Dad's jokes."]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips) -1)])
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""ok a whole bunch of text goes here that im not typing"""))

        action = input("> ")

        if action == "shoot!":
            print(dedent("""
            some more text"""))
            return Death

        elif action == "dodge!":
            print(dedent("""deded"""))
            return Death

        elif action == "tell a joke":
            print(dedent("""joke told"""))
            return 'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""text"""))
        
        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZZD!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print("ur in")
            return 'the_bridge'

        else:
            print("lock buzzes one last time and you hear melting sound it's over ha")
            return 'death'

    
class TheBridge(Scene):
    def enter(self):
        print("you go bridge, what do?")
        action = input("> ")
        if action == "throw the bomb":
            print("bomb thrown, death")
            return 'death'

        elif action == "slowly place the bomb":
            print("you point your blaster at the bomb")

            return 'escape_pod'
        else:
            print("does not compute!")
            return "the_bridge"


class EscapePod(Scene):
    def enter(self):
        print("rush thru ship to make it to escape pod, which pod you take?")
        good_pod = randint(1,5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(f"jump into pod {guess}, but crushed")
            return 'death'
        else:
            print(f"jump into pod {guess}")
            return 'finished'

class Finished(Scene):

    def enter(self):
        print("You won! GJ.")
        return 'finished'

class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory':LaserWeaponArmory(),
        'the_bridge':TheBridge(),
        'escape_pod':EscapePod(),
        'death':Death(),
        'finished':Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()