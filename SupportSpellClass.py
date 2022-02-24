import config
class SupportSpell (config.it):
    def __init__ (self,itemName,itemGet,spellRestore,spellDurability):
        config.it.__init__(self, itemName, itemGet)
        self.spellRestore = spellRestore
        self.spellDurability = spellDurability