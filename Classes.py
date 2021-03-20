class Rotor:
    def __init__(self, rotor, position):
        self.rotor = [char for char in rotor]
        self.position = position % 26
        self.ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def runThroughFront(self, letter):
        for x in range(26):
            if letter == self.ALPHABET[x]:
                letter = self.rotor[(x - self.position) % 26]
                return letter

    def runThroughBack(self, letter):
        for x in range(26):
            if letter == self.rotor[x]:
                letter = self.ALPHABET[(x-self.position) % 26]
                return letter


class Reflector:
    def __init__(self, reflector):
        self.reflector = [char for char in reflector]
        self.ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def runThrough(self, letter):
        for x in range(0, len(self.reflector)):
            if letter == self.reflector[x]:
                letter = self.ALPHABET[x]
                return letter


class Plugboard:
    def __init__(self, plugboard):
        self.plugboard = plugboard

    def runThrough(self, letter):
        for x in range(10):
            if self.plugboard[x][0] == letter:
                return self.plugboard[x][1]
            if self.plugboard[x][1] == letter:
                return self.plugboard[x][0]
        return letter


class Enigma:
    def __init__(self, reflector, rotor1, rotor2, rotor3, position1, position2, position3, plugboard):
        if reflector or rotor1 or position1 is None:
            pass
        else:
            self.reflector = Reflector(reflector)
            self.rotor1 = Rotor(rotor1, position1)
            self.rotor2 = Rotor(rotor2, position2)
            self.rotor3 = Rotor(rotor3, position3)
            self.plugboard = Plugboard(plugboard)
            print("great sakses.")