from sys import exit
import random

# a lot of names a taken from Class Map
class Scene(object):

    def enter(self):
        print "Scene not available!"
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('happy_end')
        # prevents last scenes to go in an infinite loop
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        # prints out the next_scene
        current_scene.enter()

class Death(Scene):

    insult = [
        "Well, that was embarising....",
        "Failing is part of learning...i hope this aplies to you too.",
        "At least no one watched you play.",
        "Don't tell your mother that you died in such an embarisng way.",
        "You could do better, unless that was your best."
        ]
    def enter(self):
        print Death.insult[random.randint(0,len(self.insult) - 1)]
        exit(1)

class Home(Scene):

    def enter(self):
        print "You are a bounty hunter."
        print "Currently you are home having 3 wanted posters next to your bed."
        print "You decide your plan of action, and draw a line of how you will"
        print "of how you will go an take down your targets."
        print "You decided that first target will be"
        print 'James the "Terror of the Shadows"'
        return 'desert'

class Desert(Scene):

    def enter(self):
        print "Walking toward the desert took about 2 weeks."
        print "Finding James took about 1 week."
        print "You are now inside the base."
        print "You know James is at the end of the base."
        print "But in order to get to him you need to be"
        print "silent. If the the guards see you they alert"
        print "everyone and James will escape and they will kill you."

        stealth = ["left","right"]
        i = random.choice(stealth)
        print i
        decide = raw_input("> ")

        if decide == i:
            print "You dive %s" % i
            print "Sneaking past the guards. And climp up the leader"
            print "Know where you will go?"
            i = random.choice(stealth)
            print i
            decide = raw_input("> ")
        else:
            return 'death'
        if decide == i:
            print "You jump %s" % i
            print "Grab the bar in front of you and pull yourself up."
            print "No one was able to see you. You are about half way"
            print "toward your desired goal."
            print "What will you do now?"
            i = random.choice(stealth)
            print i
            decide = raw_input("> ")
        else:
            return 'death'
        if decide == i:
            print "You starter running in the %s direction" % i
            print "You take take your zipshooter."
            print "Shoot into the ceiling and masterfully on top"
            print "of James place."
            print "You were wrong. It wasn't half way there."
            print "Not if you know a shorcut."
            print "The boss turns towards you. Takes a knife"
            print "and starts to attack you."
        else:
            return 'death'

        hero = 100
        villain = 100

        while True:
            print "What do you do now?"
            print "Hero health:", hero
            print "Villain health:", villain

            if hero < 0:
                return 'death'
            elif villain < 0:
                return 'woods'

            choice = raw_input("> ")

            if choice == "shoot him":
                print "You shot the villain."
                print "It hits his chest."
                print "But he is to fast, he hits you with his knife."
                hero -= 50
                villain -= 50
            elif choice == "block":
                print "You block his attack and hit him in the head."
                print "He stumbles backward."
                villain -= 30
            elif choice == "cut him":
                print "You get your knife and attack James."
                print "You clash blade but James proves to be"
                print "A stronger swordsman. You cut his"
                print "arm and he stabs you in the sholder"
                hero -= 40
                villain -= 20
            else:
                print "Try again."

class Woods(Scene):

    def enter(self):
        print "After you killed James 3 weeks past, you are now in the woods."
        print "Waiting for you're next target Josh the \"Unpredictable\""
        print "You heard of his destination and know that he is comming here"
        print "You wait silently. After a while he apears with 3 henchmen."
        print "They started to make a camp."
        print "You have 5 seconds to take down his henchmen before something."
        print "is amiss for them"

        i = 5
        henchmen = 3

        while True:
            print "What will you do know?"
            print "Seconds remaining: ", i
            print "Henchmen remaining", henchmen

            if i == 0:
                return 'death'
            elif henchmen == 0:
                break
            i -= 1
            choice = raw_input("> ")
            if choice == "use zip":
                print "You snach one henchmen and killed him instantly."
                henchmen -= 1
            elif choice == "use blade":
                print "You take your blade and cut down one of the henchmen."
                henchmen -= 1
            elif choice == "use pistol":
                print "You shot down one henchmen with a silencer."
                henchmen -= 1
            else:
                print "Try again."

        print "After you delt with all the henchmen Josh jumps from behind."
        print "He start fighting with you."
        print "It's a fist fight."

        hero = 100
        villain = 100

        while True:
            print "With which fist you want to him him?"
            print "Hero health:", hero
            print "Villain health:", villain

            if hero < 0:
                return 'death'
            elif villain < 0:
                return 'mountains'

            decide = raw_input("> ")
            if decide == "right":
                print "You attack with your right fist."
                print "He attacks with his left fist."
                hero -= random.randint(20,40)
                villain -= random.randint(40,60)
            elif decide == "left":
                print "You attack with your left fist."
                print "He attacks with his right fist."
                hero -= random.randint(40,60)
                villain -= random.randint(20,40)
            else:
                print "Try again."

class Mountains(Scene):

    def enter(self):
        print "After you defeated Josh. You headed towards the mountains."
        print "There you're final target sits."
        print "Jim the \"Knigh\""
        print "He has 2 hostages. Holly and Molly, you have 5 seconds to save them."
        print "They are bought straped to a bomb, each one in different location"
        print "Each bomb has a 3 digit code."

        holly = True
        molly = True

        for i in range(1,6):
            print "Who will you save?"
            print "Time remaining:", i

            if not holly and not molly:
                print "You saved both of them!"
                break

            decide = raw_input("> ")

            if decide == "Holly" and holly:
                print "You decided to save Holly."
                print "Whats the code?"
                code = random.randint(100,1000)
                print code
                decide = int(raw_input("> "))
                if decide != code:
                    return 'death'
                print "You saved Holly!"
                holly = False
            elif decide == "Molly" and molly:
                print "You decided to save Molly."
                print "Whats the code?"
                code = random.randint(100,1000)
                print code
                decide = int(raw_input("> "))
                if decide != code:
                    return 'death'
                print "You saved Molly!"
                molly = False
            else:
                print "Try again!"

        if holly:
            return ('death')
        elif molly:
            return ('death')

        print "After you saved both, Jim comes in angry!"
        print "He takes his shotgun! And startes firing!"
        print "You take cover, and start to think where to shoot!"
        print "You only have 4 bullets! Make it count!"

        hero = 100
        villain = 100
        bullets = 4
        direction = ["up", "down", "left", "right"]

        while True:
            print "In which direction do you shoot?"
            print "Hero health:",hero
            print "Villain health:",villain
            print "Bullets left:", bullets

            if hero < 0:
                return 'death'
            elif villain < 0:
                return 'happy_end'
            elif bullets == 0:
                return 'death'

            bullets -= 1
            shoot = random.choice(direction)
            print shoot

            choice = raw_input("> ")

            if choice == shoot:
                print "You shoot %s, hitting Jim but he also hits you." % shoot
                hero -= random.randint(10,20)
                villain -= random.randint(30,50)
            elif choice != shoot:
                print "You shoot %s, but you missed. Jim didn't miss." % shoot
                hero -= random.randint(10,20)
            else:
                print "Try again."

class HappyEnd(Scene):

    def enter(self):
        print "You won 100000000000000 euros!"
        return 'happy_end'

# class changer
class Map(Scene):

    scenes = {
        'home': Home(),
        'desert': Desert(),
        'woods': Woods(),
        'mountains': Mountains(),
        'death': Death(),
        'happy_end': HappyEnd()
        }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

# starting point
a_map = Map('mountains')
# Engine takes the map
a_game = Engine(a_map)
a_game.play()
