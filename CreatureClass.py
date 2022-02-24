from WeaponClass import Weapon as wep

class Creature (wep):
    def __init__(self, creatureName, creatureHp,creatureTotalHp,creaturePhyAttack,creatureMagAttack,creaturePrecision, escapeFrom_chance,creatureLoot):
        self.creatureName = creatureName
        self.creatureHp = creatureHp
        self.creatureTotalHp = creatureTotalHp
        self.creaturePrecision = creaturePrecision
        self.creaturePhyAttack = creaturePhyAttack
        self.creatureMagAttack = creatureMagAttack
        self.escapeFrom_chance = escapeFrom_chance
        self.creatureLoot = creatureLoot