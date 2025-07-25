class Player:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def introduce(self):
        return f"Player Name: {self.name}, Type: {self.type}"
    

class Wizard(Player):
    def __init__(self, name, magic_type):
        super().__init__(name, "Wizard")
        self.magic_type = magic_type

    def play(self):
        return f"{self.name} casts a spell of type {self.magic_type}!"
    

wizard1 = Wizard("Gandalf", "Fire")
print(wizard1.introduce())
print(wizard1.play())
wizard2 = Wizard("Merlin", "Ice")
print(wizard2.introduce())
print(wizard2.play())
wizard3 = Wizard("Saruman", "Lightning")
print(wizard3.introduce())
print(wizard3.play())