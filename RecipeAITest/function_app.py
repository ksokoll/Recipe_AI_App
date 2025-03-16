import azure.functions as func
import logging
import json
import os
from langchain.chat_models import ChatOpenAI
import instructor
from openai import OpenAI
from recipeFunctions import createRecipe
from errors import RecipeCreationError, ModelError

app = func.FunctionApp()

@app.function_name(name="create_recipe")
@app.route(route="create_recipe", auth_level=func.AuthLevel.ANONYMOUS)
def create_recipe(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request for recipe creation.')

    try:
        openai_api_key = os.environ["OPENAI_API_KEY"]
        if not openai_api_key:
            raise ModelError("API-Schlüssel nicht gefunden.")
        
        client = instructor.from_openai(OpenAI())
        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.8, api_key=openai_api_key)
        
        req_body = req.get_json()
        ingredients = req_body.get('ingredients')
        vegan = req_body.get('vegan', False)
        vegetarian = req_body.get('vegetarian', False)
        quick = req_body.get('quick', False)
        user_portions = req_body.get('user_portions', 2)
        extra_ingredients = req_body.get('extra_ingredients', 0)

        if not ingredients:
            return func.HttpResponse(
                "Bitte stellen Sie alle erforderlichen Parameter bereit: ingredients.",
                status_code=400
            )
        
        if quick:
            time_limit = 15 
        else: time_limit = 0

        if vegan:
            userDiet = "vegan"
        elif vegetarian:
            userDiet = "vegetarisch"
            vegan = ""
        else: userDiet = ""

        recipe = createRecipe(client, llm, ingredients, userDiet, user_portions, extra_ingredients, time_limit)
        return func.HttpResponse(json.dumps({"recipe": recipe}), mimetype="application/json")
    
    except RecipeCreationError as e:
        return func.HttpResponse(str(e), status_code=400)
    except ValueError:
        return func.HttpResponse("Ungültiger Request-Body. Bitte senden Sie gültiges JSON.", status_code=400)
    except Exception as e:
        logging.error(f"Unerwarteter Fehler: {str(e)}")
        return func.HttpResponse(f"Ein unerwarteter Fehler ist aufgetreten: {str(e)}", status_code=500)
