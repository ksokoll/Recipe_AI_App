# Internal Imports
from prompts import managerPrompt
from safetyChecks import checks
from errors import RecipeCreationError, RecipeProposalError, RecipeValidationError
from helperFunctions import extraIngredientPrompt, timeRestriction, diet, portions

import logging
from typing import Any

def proposeRecipe(llm: Any, ingredients: str, userDiet: str, userPortions: int, extraIngredients: int, time: int) -> str:
    try:
        # Logging der Eingabeparameter
        logging.info(f"Eingabeparameter: ingredients={ingredients}, userDiet={userDiet}, userPortions={userPortions}, extraIngredients={extraIngredients}, time={time}")

        params = {
            "inputQuery": f"Hi!, meine Zutaten sind: {ingredients}",
            "queryDiet": diet(userDiet),
            "queryPortions": portions(userPortions),
            "queryIngredients": extraIngredientPrompt(extraIngredients),
            "queryTime": timeRestriction(time)
        }

        # Logging der formatierten Parameter
        logging.info(f"Formatierte Parameter: {params}")

        # Logging des formatierten Prompts
        formatted_prompt = managerPrompt.format(query=params)
        logging.info(f"Formatierter Prompt: {formatted_prompt}")

        # Aufruf des Sprachmodells mit Fehlerprüfung
        try:
            recipe = llm.invoke(formatted_prompt)
        except Exception as llm_error:
            raise RecipeProposalError(f"Fehler beim Aufruf des Sprachmodells: {llm_error} mit Parametern: {params}")

        # Überprüfung des Rückgabewerts
        if recipe is None:
            raise RecipeProposalError(f"Sprachmodell gab None zurück mit Parametern: {params}")

        # Logging des Rückgabetyps
        logging.info(f"Typ des Rückgabewerts vom Sprachmodell: {type(recipe)}")

        # Überprüfung auf das Vorhandensein des 'content'-Attributs
        if not hasattr(recipe, 'content'):
            raise RecipeProposalError(f"Unerwarteter Rückgabetyp vom Sprachmodell: {type(recipe)}. 'content'-Attribut nicht gefunden. Mit Parametern: {params}")

        if not recipe.content:
            raise RecipeProposalError(f"Leere Antwort vom Modell erhalten mit Parametern: {params}")
        
        return recipe.content
    
    except RecipeProposalError as e:
        logging.error(f"RecipeProposalError: {e}")
        raise
    except Exception as e:
        logging.error(f"Unerwarteter Fehler in proposeRecipe: {e} mit Parametern: {params}")
        raise RecipeProposalError(f"Unerwarteter Fehler beim Erstellen eines Rezeptvorschlags: {e} mit Parametern: {params}")


def createRecipe(client, llm, ingredients, userDiet, userPortions, extraIngredients, time):
    error_details = []  # Liste zur Speicherung von Fehlern während der Versuche
    
    for attempt in range(1, 4):  # 3 Versuche
        try:
            print(f"Versuch {attempt}: Generiere Rezept mit Zutaten: {ingredients}")
            recipeProposal = proposeRecipe(llm, ingredients, userDiet, userPortions, extraIngredients, time)
            
            if not recipeProposal:
                error_details.append(f"Versuch {attempt}: Rezeptvorschlag war leer.")
                raise RecipeProposalError("Rezeptvorschlag war leer.")
            
            print(f"Versuch {attempt}: Überprüfung des Rezepts startet.")
            validatedRecipe = checks(client, recipeProposal)
            
            if validatedRecipe:
                print(f"Versuch {attempt}: Rezept erfolgreich validiert.")
                return recipeProposal
            else:
                error_details.append(f"Versuch {attempt}: Rezeptvalidierung fehlgeschlagen.")
                raise RecipeValidationError("Rezeptvalidierung fehlgeschlagen.")
        
        except RecipeProposalError as e:
            error_details.append(f"Versuch {attempt}: Fehler beim Erstellen des Rezeptvorschlags - {e}")
            print(f"Fehler beim Erstellen des Rezeptvorschlags: {e}")
        
        except RecipeValidationError as e:
            error_details.append(f"Versuch {attempt}: Fehler bei der Validierung - {e}")
            print(f"Fehler bei der Validierung des Rezepts: {e}")
    
    # Nach drei Versuchen detaillierte Fehler ausgeben
    error_message = "Nach drei Versuchen konnte kein gültiges Rezept erstellt werden. Details:\n" + "\n".join(error_details)
    raise RecipeCreationError(error_message)
