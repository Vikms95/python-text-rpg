from UserClass import User as us
from ItemClass import Item as it
from WeaponClass import Weapon as wep
from CreatureClass import Creature as crt
#
from DamageSpellClass import DamageSpell as dsp
from SupportSpellClass import SupportSpell as ssp
#from CreatureSpell import CreatureSpell as csp

answerA, answerB, answerC, answerS, answerN, required, required2 = ["A","a"], ["B","b"], ["C","c"], ["S","s","Si","si","SI"],["N","n","No","no","NO"], ("Por favor escoge una de las respuestas sugeridas: "), ("Por favor escoge una de las 2 respuestas sugeridas: ") 

myAnswersLet = [answerA, answerB, answerC]
myAnswersWord = [answerS, answerN]

# Deficiones listas para chest*

chest1 = []
chest2 = []
chest3 = []

# Deficiones listas para *Bag

itemBag = ["rosa"]
weaponBag = ["espada","maza"]
spellBag = ["fira","cura"]

# Boolean variables 

ladderDown = False

#Definiciones de objetos User()

generatedUser = us()

#Definiciones de objetos Item()

ladder = it(
    itemName = "escalera",
    itemGet = 0 # 0 = No tienes el Item / 1 = Tienes el Item
)
key = it(
    itemName = "llave",
    itemGet = 0
)
mirror = it(
    itemName = "espejo",
    itemGet = 0
)
rope = it(
    itemName = "cuerda",
    itemGet = 0
)

#Deficiones de objetos Weapon()

fist = wep(
    itemName = "puños",
    itemGet = 1, 
    weaponDamage = range(2,5), # Se generara un número aleatorio dentro del rango
    weaponDurability = 999, # Número de golpes realizables con el Weapon
    weaponPrecision = range(4) # (1/weaponPrecision) de fallar el golpe con el Weapon
)
sword = wep(
    itemName = "espada",
    itemGet = 0,
    weaponDamage = range(5,10),
    weaponDurability = 15,
    weaponPrecision = range(5)
)
axe = wep(
    itemName = "hacha",
    itemGet = 0,
    weaponDamage = range(8,14),
    weaponDurability = 15,
    weaponPrecision = range(4)
)
rose = wep(
    itemName = "rosa",
    itemGet = 0,
    weaponDamage = (5,15),
    weaponDurability = 10,
    weaponPrecision = range(3)
)
mace = wep(
    itemName = "maza",
    itemGet = 0,
    weaponDamage = (10,20),
    weaponDurability = 15,
    weaponPrecision = range(3)
)
book = wep(
    itemName = "libro",
    itemGet = 0,
    weaponDamage = (10,20),
    weaponDurability = 5,
    weaponPrecision = range(3)
)
ring = wep(
    itemName = "anillo",
    itemGet = 0,
    weaponDamage = (20,30),
    weaponDurability = 1,
    weaponPrecision = 1
)

myWeapons = [axe,sword,rose,mace,book,ring]

# Deficiones de objetos DamageSpell()

fireSpell = dsp(
    itemName = "fira",
    itemGet = 0,
    spellDamage = 10,
    spellDurability = 20,
    spellElement = "fire"
)
waterSpell = dsp(
    itemName = "hidro",
    itemGet = 0,
    spellDamage = 10,
    spellDurability = 20,
    spellElement = "water"
)
lightningSpell = dsp(
    itemName = "thunda",
    itemGet = 0,
    spellDamage = 10,
    spellDurability = 20,
    spellElement = "lightning"
)
bioSpell = dsp(
    itemName = "bio",
    itemGet = 0,
    spellDamage = 10,
    spellDurability = 20,
    spellElement = None
)

#Deficiones de objetos SupportSpell()

cureSpell = ssp(
    itemName = "cura",
    itemGet = 0,
    spellRestore = 20,
    spellDurability = 10
)
cure2Spell = ssp(
    itemName = "curara",
    itemGet = 0,
    spellRestore = 40,
    spellDurability = 5
)
cure3Spell = ssp(
    itemName = "curaga",
    itemGet = 0,
    spellRestore = 70,
    spellDurability = 3
)

mySpells = [fireSpell,waterSpell,lightningSpell,bioSpell,cureSpell]

# Definiciones de objetos Creature()

goblin = crt(
    creatureName = "goblin", 
    creatureHp = 50, # Total que se le restará en combate.
    creatureTotalHp = 50, # Total fijo para compararlo con la variable ya restada.
    creaturePrecision = range(3), # (1/creaturePrecision) de golpearte.
    creaturePhyAttack = range (5,10), # Rango de puntos de daño que puede hacer la criatura.
    creatureMagAttack = 1, # Multiplicador de daño cuando la criatura utiliza un hechizo.
    escapeFrom_chance = range(4), # (1/escapeFrom) de escapar.
    creatureLoot = ["espada","maza"] # Objetos que puede dejar la criatura al morir.
)
cyclop = crt(
    creatureName = "cíclope",
    creatureHp = 60,
    creatureTotalHp = 60,
    creaturePrecision = range(10),
    creaturePhyAttack = range (8,15),
    creatureMagAttack = 1,
    escapeFrom_chance = range(3),
    creatureLoot = ["espada","maza"]
)
elf = crt(
    creatureName = "elfo",
    creatureHp = 30,
    creatureTotalHp = 30,
    creaturePrecision = range(3),
    creaturePhyAttack = range (1,5),
    creatureMagAttack = 2,
    escapeFrom_chance = range (3),
    creatureLoot = ["espada","maza"]
)
orc = crt(
    creatureName = "orco",
    creatureHp = 5, 
    creatureTotalHp = 5, 
    creaturePrecision = range(8), 
    creaturePhyAttack = range (2,7),
    creatureMagAttack = 1,
    escapeFrom_chance = range(3), 
    creatureLoot = ["espada","maza"]
)
dragon = crt(
    creatureName = "dragón",
    creatureHp = 20,
    creatureTotalHp = 20,
    creaturePrecision = range(5),
    creaturePhyAttack = range (10,15),
    creatureMagAttack = 2,
    escapeFrom_chance = range(3),
    creatureLoot = ["espada","maza","libro","rosa","hacha"]
)   
wizard = crt(
    creatureName = "mago",
    creatureHp = 50,
    creatureTotalHp = 50,
    creaturePrecision = range(4), 
    creaturePhyAttack = range (5,10),
    creatureMagAttack = 5,
    escapeFrom_chance = range(1),
    creatureLoot = ["espada","maza"]
)

myCreatures = [goblin,cyclop,elf,orc,dragon,wizard]