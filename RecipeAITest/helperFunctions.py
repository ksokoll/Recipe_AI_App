def extraIngredientPrompt(extras):
  if extras > 0:
    extraIngredientPrompt = f" Du kannst bis zu {extras} nicht aufgeführte Zutaten hinzufügen, die deiner Meinung nach gut in das Gericht passen würden. Markiere diese als zusätzliche Zutat in der Zutatenliste. "
  else:
    extraIngredientPrompt = ""
  return extraIngredientPrompt

"""6.2 Time Restriction"""

def timeRestriction(minutes):
  if minutes > 0:
    timeRestriction = f" Die Zubereitungszeit darf {minutes} Minuten nicht überschreiten."
  else:
    timeRestriction = ""
  return timeRestriction

"""6.3 Diet"""

def diet(input):
  if input == "vegetarian":
    return " Achte darauf, dass alle Zutaten vegetarisch sind. "
  if input == "vegan":
    return" Achte darauf, dass alle Zutaten vegan sind. "
  else:
    return ""
  
"""6.4 Portions"""
def portions(persons):
  if persons > 0:
    servedPortions = f" Das Rezept soll für {persons} Personen sein. "
  else:
    servedPortions = ""
  return servedPortions