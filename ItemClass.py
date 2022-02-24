import config

class Item:
    def __init__ (self,itemName, itemGet):
        self.itemName = itemName
        self.itemGet = itemGet

    def item_get(self):
        self.itemGet = 1
        if isinstance(self,config.wep) is True:
            config.weaponBag.append(self.itemName)
        elif isinstance(self,config.dsp) is True or isinstance(self,config.ssp) is True:
            config.spellBag.append(self.itemName)    
        elif isinstance(self,Item) is True:
            config.itemBag.append(self.itemName)
        else:
            pass

    def item_remove(self):
        self.itemGet = 0
        if isinstance(self,config.wep) is True:
            config.weaponBag.remove(self.itemName)
        elif isinstance(self,config.dsp) is True or isinstance(self,config.ssp) is True:
            config.spellBag.remove(self.itemName)    
        elif isinstance(self,Item) is True:
            config.itemBag.remove(self.itemName)
        else:
            pass

