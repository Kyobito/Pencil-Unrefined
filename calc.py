import math

def sw_xp_to_lvl(xp):
    xps = [0, 20, 70, 150, 250, 500, 1000, 2000, 3500, 6000, 10000, 15000]
    if xp >= 15000:
        return (xp - 15000) / 10000. + 12
    else:
        for i in range(len(xps)):
            if xp < xps[i]:
                return math.floor(i + float(xp - xps[i-1]) / (xps[i] - xps[i-1]))

# Source: https://hypixel.net/threads/skywars-level-from-api.1912987/
# Name: QQB

def netexp_to_level(xp):
  networkLevel = (math.sqrt((2 * xp) + 30625) / 50) - 2.5
  networkLevel = math.floor(networkLevel)
  return networkLevel

# Source: https://hypixel.net/threads/convert-network-exp-to-network-level.1912930/
# Name: bdamja

# Do not change constants
# Constants
EASY_LEVELS = 4
EASY_LEVELS_XP = 7000
XP_PER_PRESTIGE = 96 * 5000 + EASY_LEVELS_XP
LEVELS_PER_PRESTIGE = 100
HIGHEST_PRESTIGE = 10
#
def xp_for_level(lvl):
  global EASY_LEVELS
  if lvl == 0:
    return 0
  respected_level = get_level_respecting_prestige(lvl)
  if respected_level > EASY_LEVELS:
    return 5000

  if respected_level == 1:
    return 500
  elif respected_level == 2:
    return 1000
  elif respected_level == 3:
    return 2000
  elif respected_level == 4:
    return 3500
  # Sorry for the yandere dev code
  return 5000
  
def get_level_respecting_prestige(lvl):
  global HIGHEST_PRESTIGE
  global LEVELS_PER_PRESTIGE
  if lvl > HIGHEST_PRESTIGE * LEVELS_PER_PRESTIGE:
    return lvl - HIGHEST_PRESTIGE * LEVELS_PER_PRESTIGE
  else:
    return lvl % LEVELS_PER_PRESTIGE

def bedexp_to_level(xp):
  global XP_PER_PRESTIGE
  global LEVELS_PER_PRESTIGE
  global EASY_LEVELS
  prestiges = math.floor(xp / XP_PER_PRESTIGE)
  level = prestiges * LEVELS_PER_PRESTIGE
  exp_without_prestiges = xp - (prestiges * XP_PER_PRESTIGE)
  for i in range(1,EASY_LEVELS):
    exp_for_easy_level = xp_for_level(i)

    if exp_without_prestiges < exp_for_easy_level:
      break
    level+=1
    exp_without_prestiges -= exp_for_easy_level
  return level + math.floor(exp_without_prestiges / 5000)

# Source: https://hypixel.net/threads/calculate-bedwars-level-from-exp-javascript.2022078/
# Name: KAD7 (Python redone)