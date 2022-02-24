import random
import sys
import time

#
import config as c

#Definiciones de funciones 

def ind_print(str,delay = 0):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.025 + float(delay))
    print ("\n")

def random_number(numberRange):
    randomNumber = random.choice(numberRange)
    return randomNumber

def ask_for_weapon():
    if len(c.weaponBag) == 0:
        ind_print("No tienes más armas, deberás pelear con tus puños.")
        time.sleep(3)
        c.generatedUser.userWeapon = c.fist
        return   
    elif len(c.weaponBag) == 1:
        ind_print("Solamente te queda un arma en la bolsa.")
        time.sleep(3)
        ind_print("Quieres usarla?")
        ind_print("Si/No")
        choice = input_check(c.myAnswersWord)
        if choice in c.answerS:
            for weapon in c.myWeapons:
                for onlyWeapon in c.weaponBag:
                    while weapon.itemName != onlyWeapon:
                        break
                    else:
                        time.sleep(3)
                        c.generatedUser.userWeapon ==  weapon
                        ind_print("Coges: " + weapon.itemName.capitalize() + ".")
                        return
        else:
            ("Pelearás con los puños.")
            c.generatedUser.userWeapon = c.fist
            return
    else:
        time.sleep(3)
        ind_print("Quieres usar alguna de tus armas en la bolsa?")
        ind_print("Si/No")
        choice = input_check(c.myAnswersWord)
        if choice in c.answerS:
            time.sleep(3)
            ind_print("En tu bolsa tienes las siguientes armas: " + (", ".join(c.weaponBag).title()) + ". Cual quieres coger?")
            choice = input(">")
            if choice in c.weaponBag:
                for weapon in c.myWeapons:
                    while weapon.itemName != choice:
                        break
                    else:
                        time.sleep(3)
                        choice = c.generatedUser.userWeapon
                        ind_print("Coges: " + weapon.itemName.capitalize() + ".")
                        return
            else:
                ind_print("No encontrado. Quieres usar los puños?")
                ind_print("Si/No")
                choice = input_check(c.myAnswersLet)
                if choice in c.answerN:
                    ask_for_weapon()
                else:
                    c.generatedUser.userWeapon = c.fist
                    ind_print("Pelearás con los puños.")
                    return
        else:
            ind_print("Mantienes el mismo arma que antes.")
            pass

def combat(creature,weapon):
    ind_print("Empieza el combate!")
    #Empiezas la primera fase
    while c.generatedUser.userHp > 0 and creature.creatureHp > 0:    
        time.sleep(3)
        ind_print("Escoge una opción.")
        time.sleep(3)
        ind_print("A. Atacar con arma de mano\nB. Usar hechizo")
        choice = input_check(c.myAnswersLet[:2])
        if creature.creatureHp > (creature.creatureTotalHp / 3):
            if choice in c.answerA:   
                if random_number(weapon.weaponPrecision) != 1:
                    damage = (random_number(weapon.weaponDamage)*c.generatedUser.userAttack)
                    creature.creatureHp -= damage
                    ind_print("Golpeas con tu " + weapon.itemName + " contra el "+ creature.creatureName + "!" )
                    time.sleep(2)
                    ind_print("Le has hecho " + str(int(damage)) + " puntos de daño al "+ creature.creatureName +"!")
                    time.sleep(3)
                    weapon.weaponDurability -= 1
                    time.sleep(3)
                    ind_print("El " + creature.creatureName +  " recibe el golpe pero sigue en pie sin un rasguño.")
                    time.sleep(3)
                else:
                    ind_print("El " + creature.creatureName + " esquiva tu ataque!")
                    pass
                if weapon.weapon_break() == 0:
                    ind_print("Tu " + weapon.itemName + " se ha roto y no se puede utilizar")
                    time.sleep(3)
                    c.us.userWeapon = c.fist
                else:
                    pass
            elif choice in c.answerB:
                if len(c.spellBag) > 0:
                    ind_print("Que hechizo quieres usar? " + (", ".join(c.spellBag).title() + "."))
                    choice = input(">")
                    if choice in c.spellBag:
                        for spell in c.mySpells:
                            while spell.itemName != choice:
                                break
                            else:
                                if isinstance(spell,c.ssp) is True:
                                    cure = (c.generatedUser.use_heal(spell))
                                    c.generatedUser.userHp += cure
                                    ind_print("Te has curado " + str(int(cure)) + " puntos de daño. Ahora tienes " + str(int(c.generatedUser.userHp)) + " puntos de vida restantes!" )
                                    time.sleep(3)
                                elif isinstance(spell,c.dsp) is True:
                                    damage = c.generatedUser.use_spell(spell)
                                    creature.creatureHp -= damage
                                    ind_print("El " + creature.creatureName + " ha recibido " + str(int(damage)) + " puntos de daño de tu hechizo. ")
                                    time.sleep(3)
                                    ind_print("El " + creature.creatureName +  " recibe el golpe pero sigue en pie sin un rasguño.")
                                    time.sleep(3)
                    else:
                        ind_print("Este hechizo no está disponible.")
                        continue
                else:
                    ind_print("No tienes ningun hechizo disponible.")
                    continue
        # Turno de la criatura                        
            time.sleep(3)
            ind_print("El " + creature.creatureName + " empieza a prepararse para intentarte alcanzar.")
            time.sleep(3)
            ind_print("Bashhh..!!!")
            time.sleep(3)
            # La criatura te alcanza en la primera fase
            if random_number(creature.creaturePrecision) == 1:
                ind_print("Krr! El " + creature.creatureName + " te alcanza!")
                time.sleep(3)
                damage = (random_number(creature.creaturePhyAttack)/c.generatedUser.userDefense)
                c.generatedUser.userHp -= damage
                ind_print("El " + creature.creatureName + " te ha hecho " + str(int(damage))+" puntos de daño! Ahora tienes " + str(int(c.generatedUser.userHp)) + " puntos de vida restantes!")
                if c.generatedUser.userHp <= 0:
                    game_over("Caes inconsciente")
                elif c.generatedUser.userHp > 0:
                    ind_print("Seguir combatiendo (Si) / Intentar escapar (No)?")
                    choice = input_check(c.myAnswersWord)
                    if choice in c.answerN:
                        ind_print("Quieres salir corriendo y escapar? ")
                        time.sleep(3)
                        ind_print("Si/No")
                        choice = input_check(c.myAnswersWord)
                        if choice in c.answerS:
                            ind_print("El " + creature.creatureName + " ve que le giras la espalda y se prepara para atacarte")
                            time.sleep(3)
                                    #El dragón te alcanza mientras escapas en la primera fase
                            if creature.escapeFrom_chance == 1:
                                ind_print("BAAAASH!")
                                time.sleep(3)
                                game_over("El " + creature.creatureName + " alcanza al héroe y este perece.")
                            else:
                                time.sleep(3)
                                ind_print("Escapas exitosamente.")
                                time.sleep(3)
                                break
                    elif choice in c.answerS:
                        if c.generatedUser.userHp < (c.generatedUser.userTotalHp / 4):
                            ind_print("Estas gravemente herido, tienes múltiples heridas y empiezas a marearte.")
                            ind_print("Te preparas para el siguiente ataque.")
                            time.sleep(3)
                            continue
                        else:
                            ind_print("Te preparas para el siguiente ataque.")
                            time.sleep(3)
                            continue
        #Esquivas el golpe en la primera fase
            else: 
                ind_print("Esquivas el golpe con éxito!")
                time.sleep(4)
                ind_print("Seguir combatiendo (Si) / Intentar escapar (No)?")
                choice = input_check(c.myAnswersWord)
                if choice in c.answerN:
                    ind_print("Quieres salir corriendo y escapar? ")
                    time.sleep(3)
                    ind_print("Si/No")
                    choice = input_check(c.myAnswersWord)
                    if choice in c.answerS:
                        ind_print("El " + creature.creatureName + " ve que le giras la espalda y se prepara para atacarte")
                        time.sleep(3)
                    #El dragón te alcanza mientras escapas en la primera fase
                        if creature.escapeFrom_chance == 1:
                            ind_print("BAAAASH!")
                            time.sleep(3)
                            game_over("El " + creature.creatureName + " alcanza al héroe y este perece.")
                #Escapas exitosamente
                        else:
                            time.sleep(3)
                            ind_print("Escapas exitosamente.")
                            time.sleep(3)
                            break
                    if choice in c.answerN:
                        ind_print("Te preparas para el siguiente ataque.")
                        time.sleep(3)
                        continue
                elif choice in c.answerS:
                    ind_print("Te preparas para el siguiente ataque.")
                    time.sleep(3)
                    continue  
    #Empiezas la segunda fase             
        elif creature.creatureHp <= (creature.creatureTotalHp / 3):
            if choice in c.answerA:
                if random_number(weapon.weaponPrecision) != 1:
                    damage = (random_number(weapon.weaponDamage)*c.generatedUser.userAttack)
                    creature.creatureHp -= damage
                    ind_print("Golpeas con tu " + weapon.itemName + " contra el "+ creature.creatureName + "!" )
                    time.sleep(2)
                    ind_print("Le has hecho " + str(int(damage)) + " puntos de daño al "+ creature.creatureName +"!")
                    time.sleep(3)
                    weapon.weaponDurability -= 1
                    time.sleep(3)
                    ind_print("La criatura empieza a dolerse, debe estar a punto de caer.")
                    time.sleep(3)
                else:
                    ind_print("El " + creature.creatureName + " esquiva tu ataque!")
                    pass
                if weapon.weapon_break()== 0:
                    ind_print("Tu " + weapon.itemName + " se ha roto y no se puede utilizar")
                    time.sleep(3)
                    weapon.item_remove()
                    weapon = c.fist
                else:
                    pass
                time.sleep(3)
            elif choice in c.answerB:
                if len(c.spellBag) > 0:
                    ind_print("Que hechizo quieres usar? " + (", ".join(c.spellBag).title()) + ".")
                    choice = input(">")
                    if choice in c.spellBag:
                        for spell in c.mySpells:
                            while spell.itemName != choice:
                                break
                            else:
                                if isinstance (spell,c.ssp) is True:
                                    cure = c.generatedUser.use_heal(spell)
                                    c.generatedUser.userHp += cure
                                    ind_print("Te has curado " + str(int(cure)) + " puntos de daño. Ahora tienes " + str(int(c.generatedUser.userHp)) + " puntos de vida restantes!")
                                    time.sleep(3)
                                elif isinstance (spell,c.dsp) is True:
                                    damage = c.generatedUser.use_spell(spell)
                                    creature.creatureHp -= damage
                                    ind_print("El " + creature.creatureName + " ha recibido " + str(int(damage)) + " puntos de daño de tu hechizo.")
                                    time.sleep(3)
                                    ind_print("La criatura empieza a dolerse, debe estar a punto de caer.")  
                                    time.sleep(3)
                    else:
                        ind_print("Este hechizo no está disponible.")  
                else:
                    ind_print("No tienes ningún hechizo disponible.")  
            ind_print("El " + creature.creatureName + " se prepara para un ataque poderoso. Parece que está a punto de envestirte.")
            time.sleep(3)
            ind_print("Te preparas para el ataque.")
            time.sleep(3)
            ind_print("El "  +creature.creatureName + " se avalanza sobre ti!!!")
            time.sleep(3)
            ind_print("Bashhh..!!!")
            time.sleep(3)
            if random_number(creature.creaturePrecision) == 1:
                ind_print("Krr! El " + creature.creatureName + " te alcanza!")
                time.sleep(3)
                damage = (random_number(creature.creaturePhyAttack*1.25)/c.generatedUser.userDefense)
                c.generatedUser.userHp -= damage
                ind_print("El " + creature.creatureName + " te ha hecho " + str(int(damage))+" puntos de daño! Ahora tienes " + str(int(c.generatedUser.userHp)) + " puntos de vida restantes!")
                if c.generatedUser.userHp <= 0:
                    game_over("Caes inconsciente")
                elif c.generatedUser.userHp > 0:
                    ind_print("Seguir combatiendo (Si) / Intentar escapar (No)?")
                    choice = input_check(c.myAnswersWord)
                    if choice in c.answerN:
                        ind_print("Quieres salir corriendo y escapar? ")
                        time.sleep(3)
                        ind_print("Si/No")
                        choice = input_check(c.myAnswersWord)
                        if choice in c.answerS:
                            ind_print("El " + creature.creatureName + " ve que le giras la espalda y se prepara para atacarte")
                            time.sleep(3)
                                #El dragón te alcanza mientras escapas en la primera fase
                            if creature.escapeFrom_chance == 1:
                                ind_print("BAAAASH!")
                                time.sleep(3)
                                game_over("El " + creature.creatureName + " alcanza al héroe y este perece.")
                            else:
                                time.sleep(3)
                                ind_print("Escapas exitosamente.")
                                time.sleep(3)
                                break
                        elif choice in c.answerN:
                            if c.generatedUser.userHp < (c.generatedUser.userTotalHp / 4):
                                ind_print("Estas gravemente herido, tienes múltiples heridas y empiezas a marearte.")
                            else:
                                pass
                            ind_print("Te preparas para el siguiente ataque")
                            time.sleep(3)
                            continue
                    elif choice in c.answerS:
                        if c.generatedUser.userHp < (c.generatedUser.userTotalHp / 4):
                            ind_print("Estas gravemente herido, tienes múltiples heridas y empiezas a marearte.")
                            ind_print("Te preparas para el siguiente ataque.")
                            time.sleep(3)
                            continue
                        else:
                            ind_print("Te preparas para el siguiente ataque.")
                            time.sleep(3)
                            continue
            else:
                ind_print("Fuuush..!!!")
                time.sleep(2)
                ind_print("...")
                time.sleep(3)
                ind_print("Esquivas el torrente de envestidas del adversario!.")
                time.sleep(4)
                ind_print("Seguir combatiendo (Si) / Intentar escapar (No)?")
                choice = input_check(c.myAnswersWord)
                if choice in c.answerN:
                    ind_print("Intentas escapar.")
                    time.sleep(3)
                    if random_number(creature.escapeFrom_chance) == 1:
                        ind_print("El "+ creature.creatureName + " se da cuenta que quieres escapar y se prepara para atacarte.")
                        time.sleep(3)
                        ind_print("Sin pensarselo dos veces, te enviste con toda su fuerza,") 
                        time.sleep(3)
                        ind_print("Baaaash...")
                        time.sleep(3)
                        game_over("La envestida te alcanza y caes desplomado en el suelo")
                    else:
                        time.sleep(3)
                        ind_print("Sales corriendo sin ningún problema")
                        break
                else:
                    if c.generatedUser.userHp < (c.generatedUser.userTotalHp / 4):
                            ind_print("Estas gravemente herido, tienes múltiples heridas y empiezas a marearte.")
                            ind_print("Te preparas para el siguiente ataque.")
                            time.sleep(3)
                            continue
                    else:
                        ind_print("Te preparas para el siguiente ataque.")
                        time.sleep(3)
                        continue

def loot_chest(chest): # chest = lista
    ind_print("Veamos que hay en este cofre...")
    time.sleep(3)
    ind_print("En este cofre hay " + str(len(chest)) + " objetos: " )
    for item in chest:
        ind_print("Encuentras el siguiente objeto: " + item.itemName.capitalize() + "")
        time.sleep(3)
        ind_print("Quieres cogerlo?")
        time.sleep(3)
        ind_print("Si/No")
        choice = input_check(c.myAnswersWord)
        if choice in c.answerS:
            item.item_get()
            time.sleep(3)
            ind_print("Colocas el objeto en tu bolsa.")
            time.sleep(3)
        else:
            ind_print("Mejor lo dejo, no parece de utilidad.")
            time.sleep(3)
            pass

def loot_creature(creature):
    ind_print("Quieres coger el botín?")
    ind_print("Si/No")
    choice = input_check(c.myAnswersWord)
    time.sleep(3)
    generatedLoot = []
    generatedLoot = random.sample(creature.creatureLoot,random_number(range(5)))
    ind_print("A ver que me ha dado esta criatura...")
    while choice in c.answerS and len(generatedLoot) > 0:
        time.sleep(3)
        ind_print("El botín es: " + (", ".join(generatedLoot).title()) + ". Que quieres coger?:")
        lootChoice = input(">")
        if lootChoice in generatedLoot:
            for item in c.myWeapons:
                while lootChoice != item.itemName:
                    break
                else:
                    item.item_get()
                    ind_print("Coges " + item.itemName + " y lo colocas en tu bolsa.")
                    generatedLoot.remove(item.itemName)
                    if len(generatedLoot) > 0:
                        time.sleep(3)
                        ind_print("Quieres coger algo más del botín?: ")
                        ind_print("Si/No")
                        choice = input_check(c.myAnswersWord)
                        if choice in c.answerS:
                            break
                        else:
                            return
                    else:
                        time.sleep(3)
                        ind_print("Ya no hay más botín que recoger.") 
                    return                                        
    if choice in c.answerN:
        ind_print("Decides no coger nada de botín.")
        return
    else:
        ind_print("La criatura no ha dejado nada de botín.")
    return

def game_over(string):
    ind_print(string)
    time.sleep(3)
    ind_print("Fin de la aventura.")
    time.sleep(2)
    ind_print("Quieres volver a intentarlo?")
    time.sleep(2)
    ind_print("Si/No")
    choice = input_check(c.myAnswersWord)
    if choice in c.answerS:
        option_orc()
    else:
        quit()

def input_check(answerList):
    choice = input(">")
    while choice not in [item for sublist in answerList for item in sublist]:
        choice = input("Por favor escoge una de las respuestas sugeridas.\n>")
    else:
        return choice
    
def timed_input(timeout):
    import threading
    from threading import Timer
    t = threading.Timer(timeout, game_over, ["Parece que has tardado demasiado en responder...."])
    t.start()
    answer = input_check(c.myAnswersLet)
    t.cancel()
    return answer

def reset_function():
    from inspect import currentframe, getframeinfo
    caller = currentframe().f_back
    func_name = getframeinfo(caller)[2]
    caller = caller.f_back
    from pprint import pprint
    func = caller.f_locals.get(
            func_name, caller.f_globals.get(
                func_name
            )
    )
    return func

#Definiciones de funciones storyline

def intro():
    ind_print("Bienvenid@ a mi juego. Antes de empezar, respóndeme un par de preguntas sobre ti.")
    time.sleep(3)
    ind_print("Por favor, responde con la opción mas cercana a lo que harías en cada situación propuesta.")
    #1
    ind_print("Pregunta 1:")
    time.sleep(3)
    ind_print("Paseas por un callejón oscuro y aparece un hombre por detrás con una navaja en la mano. ¿Que haces?")
    time.sleep(3)
    ind_print("A. Me giro sin miedo y uso la fuerza bruta para inmovilizar al hombre.")
    time.sleep(1)
    ind_print("B. Salgo corriendo.")
    time.sleep(1)
    ind_print("C. Me giro con calma e intento engañar al posible ladrón mediante la palabra. ")
    
    choice1 = input_check(c.myAnswersLet)
    
    time.sleep(3)
    
    #2
    ind_print("Pregunta 2:")
    time.sleep(3)
    ind_print("Estan pegándole una paliza a un chico joven en un callejón, tienes amplios conocimientos en primeros auxilios por lo que crees que podrías ser de ayuda. Los agresores salen corriendo al verte ¿Que haces?")
    time.sleep(5)
    ind_print("A. Les persigo mientras gritas que no escapen, estos no se pueden escapar por las buenas.")
    time.sleep(2)
    ind_print("B. Coges una piedra que hay en el suelo para ver si puedes darle a uno de los agresores, luego irás a ver como está el agredido.")
    time.sleep(2)
    ind_print("C. Que escapen, lo primero es ayudar al agredido con lo que necesite, puede estar gravemente herido.")

    choice2 = input_check(c.myAnswersLet)
    
    #Algoritmo para determinar tu vocación basado en los 2 inputs
    # 1 = caballero / 2 = paladin / 3 = mago / 4 = druida 

    if choice1 in c.answerA:
        if choice2 in c.answerA:
            c.generatedUser.set_vocation(1)
        elif choice2 in c.answerB or c.answerC:
            c.generatedUser.set_vocation(2)
    elif choice1 in c.answerB:
        if choice2 in c.answerA:
            c.generatedUser.set_vocation(3)
        elif choice2 in c.answerB:
            c.generatedUser.set_vocation(2)
        elif choice2 in c.answerC:
            c.generatedUser.set_vocation(4)
    elif choice1 in c.answerC:
        if choice2 in c.answerA:
            c.generatedUser.set_vocation(3)
        elif choice2 in c.answerB:
            c.generatedUser.set_vocation(2)
        elif choice2 in c.answerC:
            c.generatedUser.set_vocation(4)

    ind_print("Por último, escoge el nombre del héroe / de la heroína.")
    
    c.generatedUser.userName = input(">")
    
    time.sleep(3)
    ind_print("Oyes una voz lejana, casi rugiendo.")
    time.sleep(3)
    ind_print("...Grrrr....")  
    time.sleep(3)
    ind_print("Sientes algo haciendote cosquillas en tu oreja izquierda.") 
    time.sleep(3) 
    ind_print("Estás estirado en el suelo, abres los ojos y te incorporas confuso. Parece que estas en un bosque.")
    time.sleep(3) 
    ind_print("Empiezas a acordarte de lo que has venido a hacer aquí.") 
    time.sleep(5)  
    ind_print("Corren tiempos medievales, época en la que se conoce de un lugar sagrado. ")
    time.sleep(5)
    ind_print("En este lugar corrían historias de un anillo, color plata y brillante como la Luna de nieve.") 
    time.sleep(5)
    ind_print("El anillo fue forjado por el herrero más talentoso del reino, que debido al poder mágico que emanaba su creación,fue consumido por el mismo.")
    time.sleep(7)
    ind_print("Tu nombre es " + c.generatedUser.userName + " y has sido encomendad@ con esta misión por" + c.generatedUser.stringVocation + " Tu misión es destruir este anillo. ")
    time.sleep(10)

    option_orc()

#Encuentro con el orco. Este será el punto de retorno en caso de que acabes en Game Over.

def option_orc(): 
    ind_print("La puerta trasera del templo donde las leyendas dicen que el anillo reside está cerrada.")
    time.sleep(3)
    ind_print("Decides dar una vuelta para encontrar alguna entrada.")
    time.sleep(3)
    ind_print("El rugido que escuchaste desde el bosque parece que se ha desvanecido...") 
    time.sleep(3)
    ind_print("Cruzando la parte frontal del templo, localizas lo que seguramente sea la armería del lugar.")
    time.sleep(3)
    ind_print("....GRRRRRR.....")
    time.sleep(2)
    ind_print("Un orco, de piel marrón como el barro y de siete pies de altura te avasalla.")
    time.sleep(2)
    ind_print("Te tira contra el suelo junto a una espada que debió quedar descuidada al último que la usó.")
    time.sleep(2)
    ind_print("Debes tomar una decisión rápido! Que decides hacer?:")
    time.sleep(2)
    ind_print("A. Intentar coger la espada.")
    time.sleep(2)
    ind_print("B. Quedarme en el suelo y rendirme a las garras del orco, quizás se compadezca de mi.")
    time.sleep(2)
    ind_print("C. Resistirme con mis propias manos. ") 
   
    choice = input_check(c.myAnswersLet)


    #Ejecutará el escenario donde se recoge la espada para matar al orco

    if choice in c.answerA:
        option_sword()
    
    #No te resistes, mueres y el juego se acaba, dándote la opción de reiniciar la escena del orco

    elif choice in c.answerB:
        game_over("Te quedas mirando al cielo mientras sientes como tu cuerpo se desgarra lentamente.")
    
    #Ejecutará el escenario donde te resistes con los puños.

    elif choice in c.answerC:
        option_fist()

#Decides recoger la espada en el encuentro con el orco.

def option_sword():

    c.sword.item_get()
    c.generatedUser.userWeapon = c.sword

    ind_print("Recoges la espada y la empalas en el torso del orco. Parece que lo has matado.")
    time.sleep(3)
    ind_print("Detrás del orco divisas la entrada de una cueva.")
    time.sleep(2)
    ind_print("Quieres entrar?")
    time.sleep(2)
    ind_print("Si/No")
    
    choice = input_check(c.myAnswersWord)

    #Ejecutas el escenario en que puedes entrar en la cueva detrás del orco, ya que no es requerido escapar, puedes acceder a ella.

    if choice in c.answerS:
        option_cave()

    #Ejecutas el escenario donde decides ignorar la cueva y entrar en el templo.
    
    elif choice in c.answerN:
        option_door()
    
#Decides resistirte con tus propias manos en el encuentro con el orco.

def option_fist():
    ind_print("Tirado en el suelo, golpeas al orco en la mandíbula. El orco se queda aturdido, pero debes escapar rápido.")
    time.sleep(5)
    ind_print("Divisas una puerta detrás tuyo, pero antes te gustaría recoger la espada a pesar de que aun tienes el orco persiguiendote?")
    time.sleep(2)
    ind_print("Si/No")
    
    choice = input_check(c.myAnswersWord)
   
    if choice in c.answerS:
        c.sword.item_get()
        c.generatedUser.userWeapon = c.sword
        option_door()
    elif choice in c.answerN:
        option_door()

#Decides explorar la cueva al matar el orco con la espada. Solo posible si matas al orco con la espada.

def option_cave():
    ind_print("""El olor a moho invade tus fosas nasales, está muy oscuro y prefieres no entrar muy profundo""") 
    time.sleep(5) 
    ind_print("""pero nada más entrar en la cueva divisas un libro escondido detrás de una piedra, con el cuerpo de un esqueleto abrázandolo. Esta cueva parece interesante....""")
    time.sleep(6)
    ind_print("""Qué quieres hacer?:""")
    time.sleep(3)
    ind_print("A. Adentrarme en la cueva, tiene más sentido que el anillo esté custodiado en este lugar insólito, y este libro parece peligroso.")
    time.sleep(3)
    ind_print("B. Prefiero salir de aquí antes de que un dragón me salga de cualquier lado.") 
    time.sleep(3)
    ind_print("C. El libro podría ser de utilidad, lo cojo y me voy.")  
    
    choice = input_check(c.myAnswersLet)
    
    #Decides adentrarte en la cueva
    if choice in c.answerA:
        ind_print("Te apoyas en la pared de piedra para adentrarte con sigilo.")
        time.sleep(5)
        ind_print("...")
        time.sleep(3)
        ind_print("Grrrrr.....")
        time.sleep(3)
        ind_print("""Un dragón morado amatista aparece de la penumbra buscando el libro que el anterior héroe le había usurpado.""")
        time.sleep(3)
        ind_print("El dragón te atraviesa con sus ojos verdes...")
        time.sleep(3)
        ind_print("...")
        time.sleep(2)
        ind_print("A. Escapar sin coger el libro.")
        time.sleep(3)
        ind_print("B. Escapar y coger el libro antes de salir.")
        time.sleep(3)
        ind_print("C. Desenvainar tu espada y enfrentarte al dragón.")
        
        choice = input_check(c.myAnswersLet)
        
        #Fin de la partida
        
        if choice in c.answerA:
            ind_print("""El dragón se da cuenta que quieres escapar y divisa su preciado libro justo a la salida de la cueva.""")
            time.sleep(3)
            ind_print("Sin pensarselo dos veces, concentra todo su aire en la garganta apuntando a la figura empotrada contra la luz proveniente de la salida de la cueva""") 
            time.sleep(3)
            ind_print("Bsssssssssssh.....")
            time.sleep(3)
            ind_print()
            game_over("El dimensionado lagarto exhala un torbellino de ascuas que te incinera hasta dejarte de rodillas en el suelo")
        
        #Fin de la partida
        
        elif choice in c.answerB:
            ind_print("""El dragón se da cuenta que quieres escapar y divisa su preciado libro justo a la salida de la cueva.""")
            time.sleep(3)
            ind_print("Sin pensarselo dos veces, concentra todo su aire en la garganta apuntando a la figura empotrada contra la luz proveniente de la salida de la cueva""") 
            time.sleep(3)
            ind_print("Bsssssssssssh.....")
            time.sleep(3)
            game_over("El dimensionado lagarto exhala un torbellino de ascuas que te incinera hasta dejarte de rodillas en el suelo""")
        
        #Detona el combate contra el dragón
        
        elif choice in c.answerC:
            ind_print("Con toda la fuerza que puedes, hostigas al dragón con el acero en mano.")
            
            combat(c.dragon,c.generatedUser.userWeapon)
            
            time.sleep(3)
            ind_print("El dragón cae desplomado.")
            time.sleep(3)
            ind_print("Parece que lo he derrotado...")
            time.sleep(3)
            ind_print("Qué es esto? Del lomo del dragón ha surgido una rosa?")
            time.sleep(3)
            ind_print("La cojo?")
            time.sleep(3)
            ind_print("Si/No")
            choice = input_check(c.myAnswersWord)
            if choice in c.answerS:
                c.rose.item_get()
                ind_print("Coges la rosa y la colocas en tu bolsa. Hay que ir con cuidado de no cortarse..")
                time.sleep(3)
                ind_print("Cuidadosamente caminas en dirección de la salida. El libro sigue ahí,quieres cogerlo o prefieres dejarlo ahí?")
                time.sleep(3)
                ind_print("Cogerlo (Si) / Dejarlo (No)")
                choice = input_check(c.myAnswersWord)
                if choice in c.answerS:
                    c.book.item_get()
                    time.sleep(3)
                    ind_print("Coges el libro y sales a la luz del día para dirigirte al templo.")
                    time.sleep(3)
                    option_door()
                elif choice in c.answerN:
                    time.sleep(3)
                    ind_print("Sigue sin hacerme gracia este libro, no quiere acabar como este cadáver.")
                    time.sleep(3)
                    ind_print("Sales a la luz del día para dirigirte al templo.")
                    time.sleep(3)
                    option_door() 
            else:
                time.sleep(3)
                ind_print("No puede ser de fiar viniendo de este bicho, mejor la dejo donde está.")
                time.sleep(3)
                ind_print("Cuidadosamente caminas en dirección de la salida. El libro sigue ahí, quieres cogerlo o prefieres dejarlo ahí?")
                time.sleep(3)
                ind_print("Cogerlo (Si) / Dejarlo (No)")
                choice = input_check(c.myAnswersWord)
                if choice in c.answerS:
                    c.book.item_get()
                    time.sleep(3)
                    ind_print("Coges el libro y sales a la luz del día para dirigirte al templo.")
                    time.sleep(3)
                    option_door()
                elif choice in c.answerN:
                    time.sleep(3)
                    ind_print("Sigue sin hacerme gracia este libro, no quiere acabar como este cadáver.")
                    time.sleep(3)
                    ind_print("Sales a la luz del día para dirigirte al templo.")
                    time.sleep(3)
                    option_door()       
        else:
            ind_print("""El dragón se da cuenta de que tienes tanto miedo de que no puedes ni formular tus pensamientos.""")
            time.sleep(3)
            ind_print("Sin pensarselo dos veces, concentra todo su aire en la garganta apuntando a la figura empotrada contra la luz proveniente de la salida de la cueva""") 
            time.sleep(3)
            ind_print("Bsssssssssssh.....")
            time.sleep(3)
            game_over("El dimensionado lagarto exhala un torbellino de ascuas que te incinera hasta dejarte de rodillas en el suelo""")
    #Decides no hacer nada en la cueva y volver a la puerta del templo
    elif choice in c.answerB:
        ind_print("Decides volver a la luz del día")
        time.sleep(3)
        ind_print("""El orco parece que no da señales de vida, por lo que con paso ligero y envainando la espada que recogiste,""")
        time.sleep(3) 
        ind_print("""decides replantear la opción de explorar el templo a través de la puerta.""")
        time.sleep(3) 
        option_door()
    #Coges el libro de sospechosa pesantez y sales de la cueva
    elif choice in c.answerC:
        c.book.item_get()
        ind_print("""Recoges el libro por el lomo. Sospechosamente el libro pesa más de lo que su volumen te sugiere. De momento voy a salir de la cueva e investigaré el libro más adelante. """)
        time.sleep(7)
        ind_print("""El orco parece que no da señales de vida, por lo que con paso ligero y envainando la espada que recogiste,""")
        time.sleep(3) 
        ind_print("""decides replantear la opción de explorar el templo a través de la puerta.""")
        time.sleep(3) 
        option_door()

#Entras por la puerta directamente o viniendo de la cueva.

def option_door():
    ind_print("""Detrás de la armería localizas una puerta de visagras y pomo dorados.""")
    time.sleep(3)
    ind_print("""En la puerta parece que hay una cerradura que previamente parece haber sido forzada.""")
    time.sleep(3)
    ind_print("""Entre la armería y la puerta, hay una escalera de mano apoyada debajo de una ventana que parece entreabierta.""")
    time.sleep(3)
    ind_print("Qué decides hacer?:")
    
    #Opciones disponibles si tienes la espada pero no el libro.
    if c.sword.itemGet == 1 and c.book.itemGet == 0:
        ind_print("""A. Subo por la escalera y entro por la ventana.""")
        time.sleep(2)
        ind_print("""B. Intentar romper la cerradura con la espada.""")
        time.sleep(2)
        ind_print("""C. Intentar abrir la puerta, parece que la cerradura está forzada.""" )
        time.sleep(2)
        choice = input_check(c.myAnswersLet)
        #Inicialmente decides A, respuesta errónea y te ofrece B/C.
        if choice in c.answerA:
            ind_print("""Lamentablemente, la ventana está bloqueada por un mueble interior a pesar de estar entreabierta, no puedes entrar por ahí""")
            time.sleep(2)
            ind_print("Que decides hacer?:")
            time.sleep(2)
            ind_print("""B. Intentar romper la cerradura con la espada.""")
            time.sleep(2)
            ind_print("""C. Intentar abrir la puerta, parece que la cerradura está forzada.""" )
            time.sleep(2)
            choice = input_check(c.myAnswersLet)
            #Escoges la B, la cual es también errónea y directamente te lleva a la C
            if choice in c.answerB:
                ind_print("""Desenvainas la espada y atraviesas la cerradura con el filo.""")
                time.sleep(3)
                ind_print("""La cerradura hace un estridente ruido. Pruebas a abrir la puerta, pero no tienes suerte.""")
                time.sleep(2)
                ind_print("""Parece que voy a tener que buscar otra entrada.""")
                option_window()
        #Inicialmente decides B, respuesta errónea y te ofrece A/C.
        elif choice in c.answerB:
            ind_print("""Desenvainas la espada y atraviesas la cerradura con el filo.""")
            time.sleep(3)
            ind_print("""La cerradura hace un estridente ruido. Pruebas a abrir la puerta, pero no tienes suerte.""")
            time.sleep(2)
            ind_print("Que decides hacer?:")
            time.sleep(2)
            ind_print("""A. Subo por la escalera y entro por la ventana.""")
            time.sleep(2)
            ind_print("""C. Intentar abrir la puerta, parece que la cerradura está forzada.""" )
            time.sleep(2)
            choice = input_check(c.myAnswersLet)
            #Escoges la A, la cual es también errónea y directamente te lleva a la C
            if choice in c.answerA:
                ind_print("""Lamentablemente, la ventana está bloqueada por un mueble interior a pesar de estar entreabierta, no puedes entrar por ahí""")
                time.sleep(2)
                ind_print("""Parece que voy a tener que buscar otra entrada.""")
                option_window()    
        #Desde un inicio escoges la opción C,la única opción viable si no llegaste a coger el libro en la cueva
        elif choice in c.answerC:
            ind_print("""La puerta no abre. Parece que voy a tener que buscar otra entrada.""") 
            option_window()

    #Opciones disponibles si tienes el libro
    elif c.book.itemGet == 1 :
        time.sleep(2)
        ind_print("Bshzzzz")
        time.sleep(3)
        ind_print("Un momento! Parece que el libro que has recogido en la cueva está vibrando. Ya decía yo que parecía peligroso! Debo tomar una decisión rápido.")
        time.sleep(3)
        ind_print("""A. Subo por la escalera y entro por la ventana.""")
        time.sleep(2)
        ind_print("""B. Intentar romper la cerradura con la espada.""")
        time.sleep(2)
        ind_print("""C. Abrir el libro para ver que es lo que pesaba tanto.""")
        time.sleep(2)
        choice = timed_input(10.0)
        
        #Escoges opción A, la cual es incorrecta y en este escenario supone el fin del juego.
        if choice in c.answerA:
            ind_print("""Lamentablemente, la ventana está bloqueada por un mueble interior a pesar de estar entreabierta, no puedes entrar por ahí""")
            time.sleep(2)
            game_over("Decides bajar la escalera. Una luz verde brota del libro y desintegra tu cuerpo")
        #Escoges opción B, la cual es incorrecta y en este escenario supone el fin del juego.
        elif choice in c.answerB:
            ind_print("""Desenvainas la espada y atraviesas la cerradura con el filo.""")
            time.sleep(3)
            ind_print("""La cerradura hace un estridente ruido. Pruebas a abrir la puerta, pero no tienes suerte.""")
            time.sleep(2)
            game_over("Nada mas soltat el pomo de la puerta, una luz verde brota del libro atravesando tu pecho.")

        #Escoges opción C, la cual es la única forma de progresar si llevas el libro contigo.
        elif choice in c.answerC:
            ind_print("Decides coger el libro y abrirlo por aproximadamente la mitad")
            time.sleep(3)
            ind_print("...")
            time.sleep(3)
            ind_print("Pero...")
            time.sleep(3)
            ind_print("Qué es esto? Hay una llave dentro del libro? Debería cogerla? No se si fiarme...")
            time.sleep(2)
            ind_print("Si/No")
            choice = input_check(c.myAnswersWord)
            #Decides no tomar la llave, opción que termina el juego.
            if choice in c.answerN:
                game_over("Una luz verde brota del libro y desintegra tu cuerpo")

            #Decides tomar la llave, única forma de progresar si llevas el libro contigo.
            elif choice in c.answerS:
                c.key.item_get()
                ind_print("Coges cuidadosamente con el dedo índice y pulgar, y la colocas en la cerradura aparantemente rota....")
                time.sleep(3)
                ind_print("...")
                time.sleep(3)
                ind_print("Click!")
                time.sleep(2)
                ind_print("Voilá! La puerta cede y rápidamente la empujas con tu hombro izquierdo")
                time.sleep(3)
                ind_print("El libro parece que ha dejado de vibrar, pero después de lo sucedido no se si es de fiar... ")
                time.sleep(3)
                ind_print("Lo quieres soltar y dejarlo en el suelo?")
                time.sleep(3)
                ind_print("Si/No")
                choice = input_check(c.myAnswersWord)
                #Entras en el templo con el libro
                if choice in c.answerN:
                    ind_print("Me adentro en el templo con el libro.")
                    option_hall()
                #Entras en el templo sin el libro
                elif choice in c.answerS:
                    c.book.item_get()
                    ind_print("Me adentro en el templo sin el libro.")
                    option_hall()
            #Das una respuesta incorrecta, lo cual en esta situación frenética termina el juego.
            else:
                game_over("Una luz verde brota del libro y desintegra tu cuerpo")
        elif choice is None:
                game_over("Una luz verde brota del libro y desintegra tu cuerpo")
    #Opciones disponibles si no tienes ni espada ni libro
    else:
        ind_print("""A. Subo por la escalera y entro por la ventana.""")
        time.sleep(2)
        ind_print("""B. Intentar abrir la puerta, parece que la cerradura está forzada.""" )
        time.sleep(2)
        choice = input_check(c.myAnswersLet)
        if choice in c.answerA:
            ind_print("""Lamentablemente, la ventana está bloqueada por un mueble interior a pesar de estar entreabierta, no puedes entrar por ahí""")
            time.sleep(2)
            ind_print("""Parece que voy a tener que buscar otra entrada.""")
            option_window()
        elif choice in c.answerB:
            ind_print("""La puerta no abre. Parece que voy a tener que buscar otra entrada.""") 
            option_window()

#Sobrevives entrando por la puerta.

def option_hall():
    time.sleep(3)
    ind_print("Un enorme vestíbulo con escaleras de marfil maquilladas en la penumbra del techo con candelabros ")
    time.sleep(3)
    ind_print("Escuchas un ruido parecido al de unas cadenas en el fondo del vestibulo..")
    time.sleep(3)
    ind_print("Hay un cofre justo al lado de la entrada.. Quieres ver que hay dentro?")
    time.sleep(3)
    ind_print("Si/No")
    choice = input_check(c.myAnswersWord)
    if choice in c.answerN:
        time.sleep(3)
        pass
    else:
        loot_chest(c.chest1)
        time.sleep(3)
    ind_print("CLANK!")
    time.sleep(3)
    ind_print("Parece que hay algo que esta intentando escapar de esas cadenas..")
    time.sleep(3)
    ind_print("Debería acercarme a la habitación de donde proceden los ruidos?")
    time.sleep(3)
    ind_print("Si/No")
    choice = input_check(c.myAnswersWord)
    if choice in c.answerN:
        time.sleep(3)
        pass
    
    #Detona el combate contra el cíclope
    else:
        ind_print("Voy a ver que hay en esa habitación...")
        time.sleep(3)
        ind_print("...")
        time.sleep(3)
        ind_print("*Una enorme mano atraviesa la puerta y te coge por la cintura, dejandote inmovilizado..")
        time.sleep(3)
        ind_print("Levantas la cabeza y percibes a un gigante de un solo ojo... encadenado hasta la cintura e inmovilizado.. en esa habitación había un cíclope?")
        time.sleep(3)
        ind_print("El cíclope empieza a apretarte dentro de su mano...")
        time.sleep(3)
        ind_print("No tienes otra opción que pelear!")
        time.sleep(3)

        combat(c.cyclop,c.generatedUser.userWeapon)
        
        time.sleep(3)
        ind_print("El cíclope cae desplomado delante de la puerta de entrada con el ojo entreabierto, pero aparentemente inconsciente.")
        time.sleep(3)
        loot_creature(c.cyclop)
        time.sleep(3)
        ind_print("El cíclope estaba ligado encima de una trampilla metálica. En la superficie de la trampilla hay lo que parece un grabado de una flor de lirio. ")
        time.sleep(3)
        ind_print("No tengo otra opción que bajar por la trampilla, el acceso por la puerta está bloqueado por el cíclope.")
        time.sleep(3)
        ind_print("Abres la trampilla, bajas las escaleras descendiendo sin ver a donde llevan debido a la falta de luz.")
        option_hatch()

#No tienes la llave por lo que entras por la ventana

def option_window():
    time.sleep(3)
    ind_print("Parece que la escalera de mano que hay apoyada de la ventana bloqueada podría ser útil, quieres llevarla contigo?")
    time.sleep(3)
    ind_print("Si/No")
    choice = input_check(c.myAnswersWord)
    if choice in c.answerS:
        time.sleep(3)
        ind_print("Coges la escalera de mano.")
        c.ladder.item_get()
    elif choice in c.answerN:
        time.sleep(3)
        ind_print("*No creo que necesite esta escalera, sigamos.*")

    ind_print("Parece que hay una ventana al otro lado de la capilla. La ventana se abre y se cierra debido a la corriente de aire haciendo un ruido muy estridente. Espero que no atraiga ninguna criatura cercana...")
    time.sleep(3)
    if c.ladder.itemGet == 1: 
        time.sleep(3)
        ind_print("Parece que puedo usar la escalera para acercarme a esa ventana, debería usarla?")
        time.sleep(3)
        ind_print("Si/No")
        choice = input_check(c.myAnswersWord)
        if choice in c.answerN:
            time.sleep(3)
            ind_print("Mejor busco otra entrada.")
            time.sleep(3)
            ind_print("Corriendo hacia ti se acerca una criatura con orejas puntiagudas y ojos amarillos.")
            time.sleep(3)
            ind_print("Parece agresiva")
            
            combat(c.goblin,c.generatedUser.userWeapon)

            ind_print("El goblin pierde el conocimiento. El goblin tenía una cuerda colgando de su cinturón. La coges y la colocas en tu bolsa.")

            c.rope.item_get()
            
            time.sleep(3)
            ind_print("Debería subir por la escalera ya que no parece haber otra entrada.")
            time.sleep(3)
            ind_print("Entras por la ventana. Dentro hay una criatura enorme tirada en el suelo y atada en cadenas.")
            time.sleep(3)
            ind_print("Parece que esta criatura es un cíclope. Decides saltar y golpear al cíclope en el ojo con tu cuchillo.")
            ind_print("Le haces 60 puntos de daño al cíclope!.")
            time.sleep(3)
            ind_print("El cíclope se levanta del dolor y vuelve al suelo desplomado delante de la puerta de entrada a la sala con su ojo cubierto de sangre.")
            time.sleep(3)
            ind_print("Parece que estaba ligado encima de una trampilla metálica. En la superficie de la trampilla hay lo que parece un grabado de una flor de lirio. ")
            time.sleep(3)
            ind_print("No tengo otra opción que bajar por la trampilla, el acceso por la puerta está bloqueado por el cíclope.")
            time.sleep(3)
            ind_print("Abres la trampilla, bajas las escaleras descendiendo sin ver a donde llevan debido a la falta de luz.")
            option_hatch()
        elif choice in c.answerS:
            time.sleep(3)
            ind_print("Subes por la escalera y te apoyas en la ventana. Quieres tirar la escalera al suelo de una patada?")
            time.sleep(3)
            ind_print("Si/No")
            choice = input_check(c.myAnswersWord)
            if choice in c.answerS:
                c.ladderDown = True
                ind_print("Tiras la escalera de una patada. Mejor asegurarse de que nadie venga detrás de mi.")
            elif choice in c.answerN:
                ind_print("Dejas la escalera por si pudieras necesitar en el camino de vuelta.")
                time.sleep(3)
                ind_print("Entras por la ventana. Dentro hay una criatura enorme tirada en el suelo y atada en cadenas.")
                time.sleep(3)
                ind_print("Parece que esta criatura es un cíclope. Decides saltar y golpear al cíclope en el ojo con tu cuchillo.")
                ind_print("Le haces 60 puntos de daño al cíclope!.")
                time.sleep(3)
                ind_print("El cíclope se levanta del dolor y vuelve al suelo desplomado delante de la puerta de entrada a la sala con su ojo cubierto de sangre.")
                time.sleep(3)
                ind_print("Parece que estaba ligado encima de una trampilla metálica. En la superficie de la trampilla hay lo que parece un grabado de una flor de lirio. ")
                time.sleep(3)
                ind_print("No tengo otra opción que bajar por la trampilla, el acceso por la puerta está bloqueado por el cíclope.")
                if c.ladderDown == True:
                    time.sleep(3)
                    ind_print("Abres la trampilla, bajas las escaleras descendiendo sin ver a donde llevan debido a la falta de luz.")
                    option_hatch()
                elif c.ladderDown == False:
                    ind_print("Qué es ese ruido?")
                    time.sleep(3)
                    ind_print("Oh no! Parece que algo está subiendo por las escaleras...! ")
                    time.sleep(3)
                    ind_print("Una criatura de orejas puntiagudas y ojos amarillos cae de un salto desde la ventana. ")
                    time.sleep(3)
                    ind_print("Parece agresiva. No tengo otra opción que pelear.")
                    ask_for_weapon()

                    combat(c.goblin,c.generatedUser.userWeapon)
                    
                    ind_print("El goblin pierde el conocimiento. El goblin tenía una cuerda colgando de su cinturón. La coges y la colocas en tu bolsa.")

                    c.rope.item_get()

                    ind_print("Abres la trampilla, bajas las escaleras descendiendo sin ver a donde llevan debido a la falta de luz.")
                    option_hatch()
    elif c.ladder.itemGet == 0:
            time.sleep(3)
            ind_print("Mejor busco otra entrada.")
            time.sleep(3)
            ind_print("Corriendo hacia ti se acerca una criatura con orejas puntiagudas y ojos amarillos.")
            time.sleep(3)
            ind_print("Parece agresivo. No queda otra opción que pelear.")
            
            ask_for_weapon()

            combat(c.goblin,c.generatedUser.userWeapon)

            ind_print("El goblin pierde el conocimiento. El goblín tenía una cuerda colgando de su cinturón. La coges y la colocas en tu bolsa.")
            c.rope.item_get()
            time.sleep(3)
            ind_print("Parece que puedo alcanzar esa ventana con la cuerda.")
            time.sleep(3)
            ind_print("Tiras la cuerda y subes por la ventana.")
            time.sleep(3)
            ind_print("Entras por la ventana. Dentro hay una criatura enorme tirada en el suelo y atada en cadenas.")
            time.sleep(3)
            ind_print("Parece que esta criatura es un cíclope. Decides saltar y golpear al cíclope en el ojo con tu cuchillo.")
            ind_print("Le haces 60 puntos de daño al cíclope!.")
            time.sleep(3)
            ind_print("El cíclope se levanta del dolor y vuelve al suelo desplomado delante de la puerta de entrada a la sala con su ojo cubierto de sangre.")
            time.sleep(3)
            ind_print("Parece que estaba ligado encima de una trampilla metálica. En la superficie de la trampilla hay lo que parece un grabado de una flor de lirio. ")
            time.sleep(3)
            ind_print("No tengo otra opción que bajar por la trampilla, el acceso por la puerta está bloqueado por el cíclope.")
            time.sleep(3)
            ind_print("Abres la trampilla, bajas las escaleras descendiendo sin ver a donde llevan debido a la falta de luz.")
            option_hatch()

#Punto de convergencia entre option_hall y option_window, encuentro con el elfo.

def option_hatch():
    #Coges anillo y empieza el encuentro con el elfo
    ind_print("Entre la oscuridad localizas una leve fuente de luz.")
    time.sleep(3)
    ind_print("Te bajas de la escalera. La falta de aire te hace llegar a la conclusión que este sitio lleva siglos sin ser visitado.")
    if ("fira") in c.spellBag:
        time.sleep(3)
        ind_print("Usas una carga del hechizo Fira para iluminar tu alrededor.")
        c.fireSpell.spellDurability -= 1
        time.sleep(3)
        ind_print("De tu mano aparece una llama que ilumina las paredes de un corredor hasta la pequeña habitación de donde procedía esa luz.")
        time.sleep(5)
        ind_print("En el centro de dicha habitación, avistas un altar de piedra.")
        time.sleep(3)
        ind_print("A mano izquierda ves la fuente de luz reflejada en un espejo. ")
        time.sleep(3)
        ind_print("A mano derecha ves una estatua tallada en piedra.")
        time.sleep(3)
        ind_print("Parece que la figura representa un sujeto de la antigua raza élfica, ya extinta despues del genocidio orco, quinientos años atrás. En sus manos está sosteniendo un libro.")
        time.sleep(8)
    else:
        time.sleep(3)
        ind_print("No tengo ningún método de iluminar la zona, voy a tener que ir donde está la luz a ciegas.") 
        time.sleep(3)
        ind_print("Con la mano rozas una pared, te apoyas a ella y caminas a paso ligero.")
        time.sleep(3)
        ind_print("La luz se va acentuando. Parece que procede de un objeto situado en un altar.")
        time.sleep(3)
        ind_print("Entras en la habitación y miras a ambos lados. En el lado izquierdo ves la luz que emana el objeto del altar reflejada en un espejo.")
        time.sleep(5)
        ind_print("A mano derecha no percibes nada.")
        time.sleep(3)
        ind_print("Te acercas al espejo y lo coges.")
        time.sleep(3)
        ind_print("Al coger el espejo la luz del objeto ilumina toda la habitación, revelando una figura al otro extremo.")
        time.sleep(5)
        ind_print("Parece que es una estatua tallada en piedra.")
        time.sleep(3)
        ind_print("Esta representa un sujeto de la antigua raza élfica, ya extinta después del genocidio de los orcos, quinientos años atrás. ")
        time.sleep(8)
        ind_print("En sus manos está sosteniendo un libro")
    
    ind_print("Te acercas al espejo y lo coges.")
    
    c.mirror.item_get()
    
    time.sleep(3)
    ind_print("Al cogerlo la fuente de luz se intensifica, iluminando toda la habitación.")
    time.sleep(3)
    ind_print("La parte trasera del espejo esta hecha de madera, y parece que hay un par de frases talladas en cuchillo.")
    time.sleep(5)
    ind_print("“Los espejos son como libros. Sólo se ve en ellos lo que uno ya lleva dentro.”")
    time.sleep(3)
    ind_print("“Los espejos son como hielo que no se derrite. Sólo se derriten aquellos que se admiran en ellos.”")
    time.sleep(5)
    ind_print("Parece que el espejo me está queriendo decir algo.")
    time.sleep(3)
    ind_print("Te giras finalmente hacia al altar. Tienes la sensación de que la estatua te está siguiendo con la mirada.")
    time.sleep(5)
    ind_print("Detrás del foco de luz divisas un elegante anillo de plata, bordado con platino en la zona del chatón y grabado por vidrios de zafiro en el mismo.")
    time.sleep(8)
    ind_print("*Así que las leyendas estaban en lo cierto*.")
    time.sleep(3)
    ind_print("Te inunda un sentimiento de determinación al saber que la dura tarea de tu trayecto no ha sido en vano.")
    time.sleep(5)
    ind_print("Apoyas ambas manos en el altar de piedra y recoges el anillo con mucha precaución.")
    time.sleep(5)
    ind_print("Colocas el aro en tu palma. Te corroe una sensación de pesantez y miedo.")
    time.sleep(3)
    ind_print("Te guardas el anillo en la bolsa mientras miras de reojo la estatua.")
    time.sleep(2)
    ind_print("...")
    time.sleep(2)
    ind_print("AAAAAAAAAAH...")
    time.sleep(2)
    ind_print("¿Qué? Alguien está gritando ahí arriba?!")
    time.sleep(3)
    ind_print("Oyes varios crujidos en la habitación.")
    time.sleep(3)
    ind_print("Bajas tu mirada de donde provenía el grito hasta el lugar donde está la estatua.")
    time.sleep(3)
    ind_print("La cual ahora se está desmenuzando de arriba a abajo, revelando a un ser calcado a la figura que representaba.")
    time.sleep(5)
    ind_print("Retrocedes para escapar por donde has venido, pero una pared ocupa el lugar.")
    time.sleep(3)
    ind_print("La estatua se empieza a mover, ya transformada en un elfo mágico.")
    time.sleep(3)
    ind_print("La criatura saca una varita de su túnica, mientras registra la sala que estuvo habitando en forma de piedra durante décadas.")
    time.sleep(5)
    ind_print("El elfo se acerca hacia tí con aire despreocupado.")
    time.sleep(3)
    ind_print("De orejas puntiagudas y alegres cabellos despeinados, con algún hilo de plata revelando su edad tardía, ojos vivos e inteligentes y más delgado que tú, pero aparentemente más fuerte.")
    time.sleep(8)
    ind_print("VUESTRA RAZA NO TIENE NINGÚN REPARO EN MOSTRAR SU IMPERTINENCIA CARACTERÍSTICA.")
    time.sleep(5)
    ind_print("TRUNCAR EL DESCANSO DE UNA RELIQUIA SAGRADA NO VIENE CASTIGADO CON UN PRECIO BAJO, ACOMÓDATE EN TU NICHO DE MUERTE,JOVEN " + c.generatedUser.userVocation.upper() + ".") 
    time.sleep(8)

    combat(c.elf,c.generatedUser.userWeapon)

    ind_print("El elfo cae al suelo con el cuerpo encogido.")
    time.sleep(3)
    ind_print("A sus manos emblanquecidas les falta la fuerza para sostener el libro que lleva, que cae al suelo con un golpe seco.")
    time.sleep(3)
    ind_print("¿Quieres coger el libro?")
    ind_print("Si/No")
    
    choice = input_check(c.myAnswersWord)

    if choice in c.answerN:
        ind_print("Decides no cogerlo y salir de aquí lo antes posible")
    else:
        ind_print("Coges el libro por una de las puntas")
    
    ind_print("Las paginas del libro empiezan a crepitar, de forma similar al de las hojas de otoño dejandose llevar por el viento. ")
    time.sleep(3)
    ind_print("Del libro surge una voz familiar que se dirige a ti, pero esta vez con un tono más sosegado.")
    time.sleep(3)
    ind_print("LOS HUMANOS NUNCA DEJAIS DE SORPRENDREME, TE DEJARÉ SALIR SI PASAS ANTES UNA PEQUEÑA PRUEBA")
    time.sleep(3)
    ind_print("DE QUE MATERIAL ESTA HECHO EL ANILLO QUE POSEES?")
    time.sleep(1)
    ind_print("A. Carbón.")
    time.sleep(1)
    ind_print("B. Plata.")
    time.sleep(1)
    ind_print("C. Acero. ")

    choice = input_check(c.myAnswersLet)

    #if choice not in 

# Recoges al anillo, sales del templo, encuentro con el mago

def option_backtrack():
    ind_print("Unfinished")
