from execute_import import *
import win32clipboard
import sys

# One indexed
# Name, Primary path, Keystone, R1, R2, R3, Secondary Path, R1, R2, R3
# In the secondary R1, R2, R3, one of them has to be zero
page = ["UNTITLED", 0, 0, 0, 0, 0, 0, 0, 0, 0]

# -1 = Path
# 0 = Keystone
# 1 = R1
# 2 = R2
# 3 = R3
table = {
    # Paths
    'PRECISION': (-1, 1),
    'DOMINATION': (-1, 2),
    'SORCERY': (-1, 3),
    'RESOLVE': (-1, 4),
    'INSPIRATION': (-1, 5),

    # Precision
    'PRESS THE ATTACK': (0, 1),
    'LETHAL TEMPO': (0, 2),
    'FLEET FOOTWORK': (0, 3),
    'OVERHEAL': (1, 1),
    'TRIUMPH': (1, 2),
    'PRESENCE OF MIND': (1, 3),
    'LEGEND: ALACRITY': (2, 1),
    'LEGEND: TENACITY': (2, 2),
    'LEGEND: BLOODLINE': (2, 3),
    'COUP DE GRACE': (3, 1),
    'CUT DOWN': (3, 2),
    'LAST STAND': (3, 3),

    # Domination
    'ELECTROCUTE': (0, 1),
    'PREDATOR': (0, 2),
    'DARK HARVEST': (0, 3),
    'CHEAP SHOT': (1, 1),
    'TASTE OF BLOOD': (1, 2),
    'SUDDEN IMPACT': (1, 3),
    'ZOMBIE WARD': (2, 1),
    'GHOST PORO': (2, 2),
    'EYEBALL COLLECTION': (2, 3),
    'RAVENOUS HUNTER': (3, 1),
    'INGENIOUS HUNTER': (3, 2),
    'RELENTLESS HUNTER': (3, 3),

    # Sorcery
    'SUMMON AERY': (0, 1),
    'ARCANE COMET': (0, 2),
    'PHASE RUSH': (0, 3),
    'NULLIFYING ORB': (1, 1),
    'MANAFLOW BAND': (1, 2),
    'THE ULTIMATE HAT': (1, 3),
    'TRANSCENDENCE': (2, 1),
    'CELERITY': (2, 2),
    'ABSOLUTE FOCUS': (2, 3),
    'SCORCH': (3, 1),
    'WATERWALKING': (3, 2),
    'GATHERING STORM': (3, 3),

    # Resolve
    'GRASP OF THE UNDYING': (0, 1),
    'AFTERSHOCK': (0, 2),
    'GUARDIAN': (0, 3),
    'UNFLINCHING': (1, 1),
    'DEMOLISH': (1, 2),
    'FONT OF LIFE': (1, 3),
    'IRON SKIN': (2, 1),
    'MIRROR SHELL': (2, 2),
    'CONDITIONING': (2, 3),
    'OVERGROWTH': (3, 1),
    'REVITALIZE': (3, 2),
    'SECOND WIND': (3, 3),

    # Inspiration
    'UNSEALED SPELLBOOK': (0, 1),
    'GLACIAL AUGMENT': (0, 2),
    'KLEPTOMANCY': (0, 3),
    'HEXTECH FLASHTRAPTION': (1, 1),
    'BISCUIT DELIVERY': (1, 2),
    'PERFECT TIMING': (1, 3),
    'MAGICAL FOOTWEAR': (2, 1),
    'FUTURE’S MARKET': (2, 2),
    'FUTURE\'S MARKET': (2, 2),
    'MINION DEMATERIALIZER': (2, 3),
    'COSMIC INSIGHT': (3, 1),
    'APPROACH VELOCITY': (3, 2),
    'CELESTIAL BODY': (3, 3),
}

try:
    win32clipboard.OpenClipboard()
    clipboard = win32clipboard.GetClipboardData().strip().split('\r\n\r\n')
    win32clipboard.CloseClipboard()
    clipboard = list(filter(None, clipboard))
    if clipboard[0] == '# RUNE FILE':
        print('Importing rune page from file...')
        page[0] = clipboard[1]
        page[1:] = [int(x) for x in clipboard[2].split(',')]
        execute(False, page)
    else:
        if len(clipboard) is 8:
            title = 'UNTITLED'
        elif len(clipboard) is 9:
            title = clipboard[0].strip().split('\r\n')[0]
            clipboard.pop(0)
        else:
            raise SyntaxError('Invalid input')

        page[0] = title

        print(title + ':')

        state = -1
        for c in clipboard:
            c = c.strip().split('\r\n')[0]
            if table[c][0] is -1:
                state += 1
            if table[c][0] is not -1 and state is 1:
                page[state * 5 + 1 + table[c][0]] = table[c][1]
            else:
                page[state * 5 + 2 + table[c][0]] = table[c][1]

            if table[c][0] is -1 and state is 1 and page[1] < table[c][1]:
                page[state * 5 + 2 + table[c][0]] -= 1
            print('- ' + c)
        execute(len(sys.argv) > 1 and sys.argv[1] == "champselect", page)
        print('')
        print('# RUNES FILE\r\n')
        print(page[0] + '\r\n')
        print(','.join([str(s) for s in page[1:]]))

except:
    raise SyntaxError("Make sure to copy a valid runeforge.gg or probuilds.net page, optionally including the title,\
    and have a rune page open in the client")

