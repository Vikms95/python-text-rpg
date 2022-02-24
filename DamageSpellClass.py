import config
class DamageSpell (config.it):
    def __init__ (self,itemName,itemGet,spellDamage,spellDurability,spellElement):
        config.it.__init__(self, itemName, itemGet)
        self.spellDamage = spellDamage
        self.spellDurability = spellDurability
        self.spellElement = spellElement