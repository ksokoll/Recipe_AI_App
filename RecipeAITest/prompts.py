# Internal Imports
from langchain.prompts import PromptTemplate

managerPrompt = PromptTemplate(
    input_variables=["query"],
    template="""Bitte gib mir ein Gericht inspiriert von meinen zutaten, in der Sprache meiner Zutatenliste.

Wichtig:
Halte dich an die Zutatenliste, sodass keine zusätzlichen Zutaten verwendet werden, außer unten steht etwas anderes.

Füge auch die Mengenangaben in der Zutatenliste hinzu sowie eine Kochanleitung.

Das Gericht muss nicht zwangsläufig aus allen genannten Zutaten bestehen und muss den Ernährungsstilen vegan oder vegeratisch entsprechen, wenn gefordert.

Bitte gliedere das Rezept in:

    - Name des Gerichts

    - Zutaten

    - Kochanleitung

    
{query}"""
)

safetySystemPrompt = """

Bitte prüfe das folgende Rezept, ob es schädliche Zutaten oder Anweisungen enthält, die Verletzungen herbeiführen könnten.

Antworte ausschließlich mit "yes" wenn das Rezept sicher ist, und mit "no" , falls nicht.

"""

completionSystemPrompt = """

Bitte prüfe das folgende Rezept, ob es die nötigen Inhalte enthält:

-  Name des Rezepts

- Zutatenliste mit Mengenangaben

- Kochanleitung

Antworte mit "yes" falls es komplett ist, und mit "no" falls nicht.

"""
