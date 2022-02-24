import config

class Weapon (config.it):
    
    def __init__ (self,itemName, itemGet, weaponDamage,weaponDurability,weaponPrecision):
        config.it.__init__(self, itemName, itemGet)
        self.weaponDamage = weaponDamage
        self.weaponDurability = weaponDurability
        self.weaponPrecision = weaponPrecision
    
    def weapon_break(self):
        if self.weaponDurability == 0:
            self.item_remove()
            return 0
        else:
            pass
