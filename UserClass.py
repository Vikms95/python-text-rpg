import config
import time
import functions

class User():

    # Estadísticas base héroe

    userHp = 50
    userTotalHp = 100
    userAttack = 1
    userDefense = 1
    userMagic = 1
    userMDefense = 1
    userName = ""
    userVocation = "Caballero"
    userWeapon = "puños"

    def __init___(self):
        pass
    
    # Modifica estadísticas base de User() dependiendo de la vocación asignada

    def set_vocation(self,vocation): 
        
        if vocation == 1:
            self.userVocation = "Caballero"
            self.userHp += 100
            self.userTotalHp += 200 
            self.userAttack += 0.50
            self.userDefense += 0.50
            self.userMagic += 0.05
            self.userMDefense += 0
            self.stringVocation = " tu habilidad en combates cuerpo y el uso de armas de corto alcance."
        elif vocation == 2:
            self.userVocation = "Paladín"
            self.userHp += 75
            self.userTotalHp += 150
            self.userAttack += 0.60
            self.userDefense += 0.20
            self.userMagic += 0.20
            self.userMDefense += 0.20
            self.stringVocation = " tu habilidad con las armas a distancia y agilidad en combate."
        elif vocation == 3:
            self.userVocation = "Mago"
            self.userHp += 50
            self.userTotalHp += 120
            self.userAttack += 0.20
            self.userDefense += 0.20
            self.userMagic += 0.80
            self.userMDefense += 0.40
            self.stringVocation = " tu conocimiento en las artes mágicas oscuras y por asestar grandes cantidades de daño con tus hechizos."
        elif vocation == 4:
            self.userVocation = "Druida"
            self.userHp += 75
            self.userTotalHp += 150 
            self.userAttack += 0.30
            self.userDefense += 0.30
            self.userMagic += 0.60
            self.userMDefense += 1
            self.stringVocation = " tu conocimiento en las artes mágicas naturales y tu capacidad de sanar hasta la herida mas profunda."
    
    # Función de User() para usar hechizos de cura

    def use_heal (self,SupportSpell):
        outputHeal = (SupportSpell.spellRestore * config.generatedUser.userMagic)
        SupportSpell.spellDurability -= 1
        functions.ind_print(" Has usado " + "'" +  SupportSpell.itemName.capitalize() + "'" + "!")
        if SupportSpell.spellDurability == 0:
            time.sleep(3)
            functions.ind_print("Te has quedado sin cargas de este hechizo")
            SupportSpell.item_remove()
        else:
            pass
        return outputHeal

    #Funcion de User() para usar hechizos de daño

    def use_spell (self,DamageSpell):
        outputDamage = DamageSpell.spellDamage*config.generatedUser.userMagic
        DamageSpell.spellDurability -= 1
        functions.ind_print(" Has usado " + "'" +  DamageSpell.itemName.capitalize() + "'" + "!")
        if DamageSpell.spellDurability == 0:
            time.sleep(3)
            functions.ind_print("Te has quedado sin cargas de este hechizo.")
            DamageSpell.item_remove()
        else:
            pass
        return outputDamage