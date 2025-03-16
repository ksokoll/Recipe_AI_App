# Recipe_AI: Backend for AI-Powered Recipe Generator and Evaluator

## Project Overview
Recipe_AI is the backend service for a recipe generation app powered by AI. The app uses large language models (LLMs) to generate personalized recipes based on user inputs such as available ingredients, dietary preferences, and desired cuisine types. The backend is hosted as Azure Functions and handles the recipe generation and evaluation processes.

The goal of Recipe_AI is to provide users with optimized recipe suggestions tailored to their needs.

## Features
- **Personalized Recipe Generation**: Generate recipes based on user-provided ingredients, dietary preferences, and cuisine types.
- **Dietary Preferences**: Support for dietary restrictions such as vegan, gluten-free, and more.
- **Ingredient Substitutions**: Suggest substitutions for missing ingredients or those that don’t fit the user's preferences.
- **Alternative Cooking Techniques**: Propose alternative ways of preparing dishes for variety and efficiency.

## Architecture
The Recipe_AI backend is deployed as an Azure Function that handles different tasks:
- **Recipe Request Function**: Processes the user request via an HTTP trigger, validates input data, and initiates the recipe generation process.
- **Recipe Generation Function**: Receives the input data and passes it to the proposeRecipe() function, which generates the recipe using the LLM model.
- **Validation Function**: The generated recipe is validated using the checks() function, which performs security and completeness checks in parallel.
- **Error Handling Function**: The entire process is safeguarded with robust error handling. If the recipe proposal or validation fails, the system retries multiple times and returns a detailed error message after failure.

## Installation and Setup

### Prerequisites
To run this backend, you will need:
- **Python 3.8+**
- **Azure Functions Core Tools**: To run the functions locally.
- **Azure Subscription**: For deployment to Azure Functions.
- **OpenAI API Key**: For accessing the GPT-4o-mini model for recipe generation.

## How to Run
1. Clone the Repository
```bash
   git clone https://github.com/yourusername/Recipe_AI.git
cd Recipe_AI
```
2. Create a .env file and add your OpenAI API key. The current .env variable is empty!
```bash
OPENAI_API_KEY='your_api_key'
```
3. Install dependencies
```bash
pip install -r requirements.txt
```

You have now the possibility to run your azure function locally, or, like in my case, deploy it either directly in Azure productively in Azure oder Azure functions.


##Future Work & Outlook

- Personalized Recipe Learning: Use feedback to continuously improve recipe suggestions for individual users.
- Expanded Dietary Preferences: Add more options for dietary restrictions (e.g., keto, paleo).
- Nutritional Optimization: Incorporate a nutritional evaluation system to balance meals based on health goals and show nutricients like fat, carbs or protein.

