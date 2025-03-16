Recipe_AI: AI-Powered Recipe Generator and Evaluator
Project Overview
Recipe_AI is an experimental project that leverages large language models (LLMs) to generate and evaluate recipes based on user inputs, such as ingredients, dietary preferences, and cooking techniques. The goal is to explore how LLMs can be utilized to assist in the creation of personalized, optimized recipes while evaluating the efficiency, creativity, and quality of the generated results.

The system allows users to input a set of ingredients and preferences, and the AI will generate multiple recipes. The recipes are evaluated based on predefined criteria, such as ease of preparation, taste profile, and health benefits.

Experimental Setup
Rules of the System
Input Parameters: A list of available ingredients, dietary preferences (e.g., vegan, gluten-free), and desired cuisine type.
Recipe Generation: The LLM generates several recipe suggestions based on the input parameters.
Evaluation: Each recipe is evaluated based on:
Preparation time
Ingredient compatibility
Nutritional balance (e.g., protein, carb, fat ratios)
Ease of execution (e.g., steps involved)
Recipe Output: A final ranking of the generated recipes, from best to least optimal.
Objective
The AI aims to generate the most suitable recipe by considering the user's input while optimizing for taste, preparation time, and nutritional balance. The iterative improvement process includes adjusting the LLM prompts and integrating additional evaluation metrics.

Iterations
Baseline Setup: Simple recipe generation using only the user inputs.
Setup 1: Introducing ingredient substitution suggestions to improve recipe variety.
Setup 2: Evaluating recipes based on dietary constraints (e.g., vegan or gluten-free).
Setup 3: Allowing the LLM to propose alternative cooking techniques or presentation styles.
Setup 4: Integrating user feedback to refine the recipe ranking and suggestions.
Results
Setup 1: Baseline vs. Ingredient Substitutions
Baseline: Average recipe score of 7.4/10
With Ingredient Substitutions: Average recipe score of 8.2/10
Improvement: 10.8% increase in recipe variety and adaptability.
Setup 2: Dietary Constraints (Vegan)
Vegan Recipes: Average recipe score of 7.8/10
Non-Vegan Recipes: Average recipe score of 6.9/10
Key Insight: Recipes tailored to specific dietary restrictions received higher ratings for creativity and satisfaction.
Setup 3: Alternative Cooking Techniques
Result: Recipe preparation time decreased by 15%, but taste ratings remained consistent.
Key Insight: Introducing alternative cooking techniques improved overall recipe appeal without compromising taste.
Setup 4: User Feedback Integration
Result: Average user rating of recipes increased to 9.1/10.
Key Insight: Continuous refinement based on user input led to more personalized and optimized results.
Conclusion
The Recipe_AI experiments show that LLMs can successfully generate personalized recipes that meet dietary preferences, maximize ingredient compatibility, and improve overall user satisfaction. Iterative feedback and incorporating ingredient substitutions or cooking alternatives proved to significantly enhance the AI’s recipe generation capabilities.

Future Work & Outlook
Extending Recipe Complexity: Investigating more advanced recipe structures (e.g., multi-course meals).
Refining Evaluation Metrics: Integrating machine learning models to further optimize recipe evaluations.
Personalization through User History: Implementing long-term learning from user preferences to improve recipe suggestions over time.
Installation
Dependencies
To run this project, you'll need the following dependencies:

bash
Kopieren
Bearbeiten
pip install python-dotenv openai httpx==0.23.0
How to Run
Clone the Repository:

bash
Kopieren
Bearbeiten
git clone https://github.com/yourusername/Recipe_AI.git
cd Recipe_AI
Enter your OpenAI API Key: In your .env file, add the following:

text
Kopieren
Bearbeiten
OPENAI_API_KEY='your_api_key'
Run the Script:

bash
Kopieren
Bearbeiten
python recipe_ai.py
License
This project is licensed under the MIT License. See the LICENSE file for details.

Special thanks to OpenAI's GPT-4o-mini for powering the LLM models and the developer community for their contributions.

Feel free to make any further adjustments based on your exact project details or preferences!







Du:
danke, bitte passe die readme etwas an. Recipe_AI ist kein experiment, sondern das backend zu einer App, welche in azure functions verfügbar ist
ChatGPT:
Natürlich, hier ist die angepasste README für Recipe_AI als Backend einer App, die in Azure Functions verfügbar ist:

Recipe_AI: Backend for AI-Powered Recipe Generator and Evaluator
Project Overview
Recipe_AI is the backend service for a recipe generation and evaluation app powered by AI. The app uses large language models (LLMs) to generate personalized recipes based on user inputs such as available ingredients, dietary preferences, and desired cuisine types. The backend is hosted as Azure Functions and handles the recipe generation and evaluation processes.

The goal of Recipe_AI is to provide users with optimized recipe suggestions tailored to their needs, ensuring efficiency, creativity, and nutritional balance. The AI continuously improves the recipe generation process by incorporating user feedback and adjusting the prompts used for recipe generation.

Features
Personalized Recipe Generation: Generate recipes based on user-provided ingredients, dietary preferences, and cuisine types.
Recipe Evaluation: Evaluate recipes based on preparation time, nutritional balance, ingredient compatibility, and ease of execution.
Dietary Preferences: Support for dietary restrictions such as vegan, gluten-free, and more.
Ingredient Substitutions: Suggest substitutions for missing ingredients or those that don’t fit the user's preferences.
Alternative Cooking Techniques: Propose alternative ways of preparing dishes for variety and efficiency.
Architecture
The Recipe_AI backend is deployed as a set of Azure Functions that handle different tasks:

Recipe Generation Function: Generates recipes based on user input.
Recipe Evaluation Function: Evaluates the generated recipes based on predefined criteria.
Feedback Integration Function: Collects and processes user feedback to improve future recipe suggestions.
Ingredient Substitution Function: Suggests ingredient replacements when necessary.
Installation and Setup
Prerequisites
To run this backend, you will need:

Python 3.8+
Azure Functions Core Tools: To run the functions locally.
Azure Subscription: For deployment to Azure Functions.
OpenAI API Key: For accessing the GPT-4o-mini model for recipe generation.
Dependencies
To install the required dependencies, run:

bash
Kopieren
Bearbeiten
pip install python-dotenv openai azure-functions httpx==0.23.0
Setting up the Environment
Clone the Repository:

bash
Kopieren
Bearbeiten
git clone https://github.com/yourusername/Recipe_AI.git
cd Recipe_AI
Create a .env file and add your OpenAI API key:

text
Kopieren
Bearbeiten
OPENAI_API_KEY='your_api_key'
Install dependencies:

bash
Kopieren
Bearbeiten
pip install -r requirements.txt
Running the Azure Functions Locally
Start the Azure Functions locally:

bash
Kopieren
Bearbeiten
func start
This will start the backend locally on a specified port. You can now test the endpoints through HTTP requests.

Deploying to Azure
Make sure you have an Azure subscription and have configured Azure CLI.

Deploy the functions to Azure using the following commands:

bash
Kopieren
Bearbeiten
func azure functionapp publish <your-function-app-name>
API Endpoints
The following are the available API endpoints for the Recipe_AI backend:

POST /generate-recipe
Generates a recipe based on user inputs.

Request Body:
json
Kopieren
Bearbeiten
{
  "ingredients": ["tomato", "onion", "garlic"],
  "dietary_preferences": ["vegan", "gluten-free"],
  "cuisine_type": "Italian"
}
Response:
json
Kopieren
Bearbeiten
{
  "recipe_name": "Vegan Tomato Pasta",
  "ingredients": ["tomato", "onion", "garlic", "pasta"],
  "steps": [
    "Boil the pasta.",
    "Prepare the tomato sauce with garlic and onion.",
    "Combine the pasta with the sauce."
  ],
  "prep_time": "20 minutes",
  "nutrition": {
    "calories": 350,
    "protein": "7g",
    "carbs": "50g",
    "fat": "8g"
  }
}
POST /evaluate-recipe
Evaluates the generated recipe based on user feedback.

Request Body:
json
Kopieren
Bearbeiten
{
  "recipe_name": "Vegan Tomato Pasta",
  "rating": 4,
  "feedback": "Too spicy"
}
Response:
json
Kopieren
Bearbeiten
{
  "status": "Success",
  "message": "Feedback received, recipe will be adjusted."
}
POST /suggest-substitute
Suggests an ingredient substitution based on available ingredients.

Request Body:
json
Kopieren
Bearbeiten
{
  "missing_ingredient": "cheese",
  "available_ingredients": ["tofu", "cashews"]
}
Response:
json
Kopieren
Bearbeiten
{
  "substitute": "tofu",
  "reason": "Tofu can provide a similar texture and protein content."
}
Future Work & Outlook
Personalized Recipe Learning: Use feedback to continuously improve recipe suggestions for individual users.
Expanded Dietary Preferences: Add more options for dietary restrictions (e.g., keto, paleo).
Nutritional Optimization: Incorporate a more advanced nutritional evaluation system to balance meals based on health goals.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Special thanks to OpenAI's GPT-4o-mini for powering the LLM models and the Azure community for their tools and resources.
