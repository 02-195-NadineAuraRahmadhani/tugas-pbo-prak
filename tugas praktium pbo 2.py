class Robot:
    def __init__(self, nama, hp, attack):
        self.nama = nama
        self.hp = hp
        self.attack = attack

    def serang(self, musuh):
        musuh.hp -= self.attack
        print(f"{self.nama} menyerang {musuh.nama} dengan {self.attack} damage!")

class Game:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2
        self.ronde = 1

    def mulai(self):
        while self.robot1.hp > 0 and self.robot2.hp > 0:
            print(f"\nRound-{self.ronde} =========================")
            print(f"{self.robot1.nama} [HP: {self.robot1.hp}] vs {self.robot2.nama} [HP: {self.robot2.hp}]")

            input(f"{self.robot1.nama}, tekan ENTER untuk menyerang...")
            self.robot1.serang(self.robot2)

            if self.robot2.hp <= 0:
                print(f"\n{self.robot1.nama} menang!")
                break

            input(f"{self.robot2.nama}, tekan ENTER untuk menyerang...")
            self.robot2.serang(self.robot1)

            if self.robot1.hp <= 0:
                print(f"\n{self.robot2.nama} menang!")
                break

            self.ronde += 1


robot1 = Robot("Drogon", 300, 50)
robot2 = Robot("Caraxes", 650, 30)


game = Game(robot1, robot2)
game.mulai()