class Enigma():
    def __init__(self, reflector, rotor1, rotor2, rotor3, position1, position2, position3, plugboard):
        if reflector is None:
            pass
        else:
            self.reflector = reflector
            self.rotor1 = rotor1
            self.rotor2 = rotor2
            self.rotor3 = rotor3
            self.position1 = position1 % 26
            self.position2 = position2 % 26
            self.position3 = position3 % 26
            self.plugboard = plugboard
            self.ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def runThroughPlugboard(self, letter):
        for x in range(10):
            if self.plugboard[x][0] == letter:
                return self.plugboard[x][1]
            if self.plugboard[x][1] == letter:
                return self.plugboard[x][0]
        return letter

    def runThroughReflector(self, letter):
        for x in range(0, len(self.reflector)):
            if letter == self.reflector[x]:
                letter = self.ALPHABET[x]
                return letter

    def runThroughRotorFront(self, letter, num):
        for x in range(26):
            if letter == self.ALPHABET[x]:
                if num == 1:
                    letter = self.rotor1[(x - self.position1) % 26]
                    return letter
                if num == 2:
                    letter = self.rotor2[(x - self.position2) % 26]
                    return letter
                if num == 3:
                    letter = self.rotor3[(x - self.position3) % 26]
                    return letter

    def runThroughRotorBack(self, letter, num):
        if num == 1:
            for x in range(26):
                if letter == self.rotor1[x]:
                    letter = self.ALPHABET[(x - self.position1) % 26]
                    return letter
        if num == 2:
            for x in range(26):
                if letter == self.rotor2[x]:
                    letter = self.ALPHABET[(x - self.position2) % 26]
                    return letter
        if num == 3:
            for x in range(26):
                if letter == self.rotor3[x]:
                    letter = self.ALPHABET[(x - self.position3) % 26]
                    return letter

    def fixPositioning(self):
        self.position1 += 1
        if self.position1 >= 26:
            self.position1 = self.position1 % 26
            self.position2 += 1
            if self.position2 >= 26:
                self.position2 = self.position2 % 26
                self.position3 += 1
                self.position3 = self.position3 % 26