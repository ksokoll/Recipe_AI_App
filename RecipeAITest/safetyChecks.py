# External Imports
from pydantic import BaseModel, Field
from enum import Enum
import concurrent.futures
import logging

# Internal Imports
from prompts import safetySystemPrompt, completionSystemPrompt
from errors import RecipeValidationError

# Configure Logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class safe(str, Enum):
    yes = "yes"
    no = "no"

class SafetyReply(BaseModel):
    content: str = Field(description="The answer to the query")
    category: safe = Field(description="Evaluate the safety of the recipe")

def safetyCheck(client, query):
    try:
        logger.info(f"Starting safety check with query: {query[:50]}...")
        reply = client.chat.completions.create(
            model="gpt-4o-mini",
            response_model=SafetyReply,
            messages=[{"role": "system", "content": safetySystemPrompt}, {"role": "user", "content": query}]
        )
        if not reply:
            raise RecipeValidationError("No response received from the safety check.")
        if not reply.category:
            raise RecipeValidationError("Category missing in the safety check response.")
        logger.info(f"Safety check completed. Result: {reply.category}")
        return reply.category
    except Exception as e:
        logger.error(f"Error in safety check: {str(e)}")
        raise RecipeValidationError(f"Error in safety check: {str(e)}")

class complete(str, Enum):
    yes = "yes"
    no = "no"

class CompletionReply(BaseModel):
    content: str = Field(description="The answer to the query")
    category: safe = Field(description="Evaluate the completion of the recipe")

def completionCheck(client, query):
    try:
        logger.info(f"Starting completeness check with query: {query[:50]}...")
        reply = client.chat.completions.create(
            model="gpt-4o-mini",
            response_model=SafetyReply,
            max_retries=3,
            messages=[
                {"role": "system", "content": completionSystemPrompt},
                {"role": "user", "content": query}
            ]
        )
        if not reply:
            raise RecipeValidationError("No response received from the completeness check.")
        if not reply.category:
            raise RecipeValidationError("Category missing in the completeness check response.")
        logger.info(f"Completeness check completed. Result: {reply.category}")
        return reply.category
    except Exception as e:
        logger.error(f"Error in completeness check: {str(e)}")
        raise RecipeValidationError(f"Error in completeness check: {str(e)}")

def checks(client, recipe):
    try:
        logger.info("Starting parallel checks...")
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            future_safety = executor.submit(safetyCheck, client, recipe)
            future_completion = executor.submit(completionCheck, client, recipe)

            safety_result = future_safety.result()
            completion_result = future_completion.result()

        logger.info(f"Check results: Safety={safety_result}, Completeness={completion_result}")

        if safety_result == "yes" and completion_result == "yes":
            logger.info("Recipe successfully validated.")
            return True
        else:
            raise RecipeValidationError(f"Recipe not validated. Safety: {safety_result}, Completeness: {completion_result}")
    
    except Exception as e:
        logger.error(f"Error during execution of parallel checks function: {str(e)} for the recipe: {recipe}")
        raise RecipeValidationError(f"Error during execution of parallel checks function: {str(e)} for the recipe: {recipe}")