from random import randint

def main():
    world = {}

    world['size'] = dice(2, 6, -2)

    world['atm'] = dice(2, 6, -7 + world['size'])

    world['temp'] = dice(2, 6, temp_DM_atm(world))

    world['hydro'] = dice(2, 6, -7 + world['size'] + hydro_DM(world))

    if world['size'] <= 1:
        world['hydro'] = 0

    world['pop'] = dice(2, 6, -2)

    world['gov'] = dice(2, 6, -7 + world['pop'])

    world['law'] = dice(2, 6, world['gov'])

    world['culture'] = (dice(1, 6) * 10) + dice(1, 6)

    world['starport'] = compute_starport_class(dice(2, 6))

    world['tech'] = dice(1, 6, tech_DM(world))

    world['code'] = amber(world)

    world['trade'] = compute_trade_codes(world)

    f = open('world.txt', 'w')

    for key, value in world.iteritems():
        f.write(''.join([key, ' = ', str(value), '\n']))



def dice(a, b, mod=0):
    s = 0;
    for i in range(1, a+1):
        s = s + randint(1, b)
    if s + mod >= 0:
        return s
    else:
        return 0

def temp_DM_atm(world):
    atm = world['atm']
    if atm < 2:
        return 0
    else:
        return {2 : -2,  3 : -2, 
                4 : -1,  5 : -1, 
                6 : 0,   7 : 0,
                8 : 1,   9 : 1,
                10 : 2,  11 : 6,
                12 : 6,  13 : 2,
                14 : -1, 15 : 2}[atm]

def hydro_DM(world):
    atm = world['atm']
    temp = world['atm']
    
    if atm <= 1 or (atm >= 10 and atm <= 12):
        dm = -4
    else:
        dm = 0
    
    if atm == 13:
        dm += 0
    elif temp == 10 or temp == 11:
        dm -= 2
    elif temp >= 12:
        dm -= 6
    else:
        dm += 0

    return dm


def compute_starport_class(roll):
    if roll <= 2:
        return 'X'
    if roll <= 4:
        return 'E'
    if roll <= 6:
        return 'D'
    if roll <= 8:
        return 'C'
    if roll <= 10:
        return 'B'
    if roll >= 11:
        return 'A'

def tech_DM(world):
    dm = 0

    starport = world['starport']
    if starport == 'A':
        dm += 6
    if starport == 'B':
        dm += 4
    if starport == 'C':
        dm += 2
    if starport == 'X':
        dm += -4

    size = world['size']
    if size <= 1:
        dm += 2
    if size <= 4:
        dm += 1

    atm = world['atm']
    if atm <= 3 or atm >= 10:
        dm += 1

    hydro = world['hydro']
    if hydro == 1 or hydro == 9:
        dm += 1
    if hydro == 10:
        dm += 2
    
    pop = world['pop']
    if pop == 0:
        dm += 0
    if pop <= 5 or pop == 9:
        dm += 1
    if pop == 10:
        dm += 2
    if pop == 11:
        dm += 3
    if pop == 12:
        dm += 4
    
    gov = world['gov']
    if gov == 0 or gov == 5:
        dm += 1
    if gov == 7:
        dm += 2
    if gov == 13 or gov == 14:
        dm += -2

    return dm

def amber(world):
    if world['atm'] >= 10:
        return True 
    if world['gov'] == 0 or world['gov'] == 7 or world['gov'] == 10: 
        return True
    if world['law'] == 0 or world['law'] >= 9:
        return True
    else:
        return False

def compute_trade_codes(world):
    size = world['size']
    atm = world['atm']
    hydro = world['hydro']
    pop = world['pop']
    gov = world['gov']
    law = world['law']
    tech = world['tech']
    
    codes = []
    if atm >= 4 and atm <= 9 and hydro >= 4 and hydro <= 8 and pop >= 5 and pop <= 7:
        codes.append('Ag')
    if size == 0 and atm == 0 and hydro == 0:
        codes.append('As')
    if pop == 0 and gov == 0 and law == 0:
        codes.append('Ba')
    if atm >= 2 and hydro == 0:
        codes.append('De')
    if atm >= 10 and hydro >= 1:
        codes.append('Fl')
    if size >= 5 and atm >= 4 and atm <= 9 and hydro >= 4 and hydro <= 8:
        codes.append('Ga')
    if pop >= 9:
        codes.append('Hi')
    if tech >= 12:
        codes.append('Ht')
    if atm <= 1 and hydro >= 1:
        codes.append('Ic')
    if (atm == 0 or atm == 1 or atm == 2 or atm == 4 or atm == 7 or atm == 9) \
            and pop >= 9:
        codes.append('In')
    if pop >= 1 and pop <= 3:
        codes.append('Lo')
    if tech <= 5:
        codes.append('Lt')
    if atm <= 3 and hydro <= 3 and pop >= 6:
        codes.append('Na')
    if pop >= 4 and pop <= 6:
        codes.append('Ni')
    if atm >= 2 and atm <= 5 and pop <= 3:
        codes.append('Po')
    if (atm == 6 or atm == 8) and pop >= 6 and pop <= 8:
        codes.append('Ri')
    if atm == 0:
        codes.append('Va')
    if hydro == 10:
        codes.append('Wa')

    return codes

if __name__ == '__main__':
    main()
