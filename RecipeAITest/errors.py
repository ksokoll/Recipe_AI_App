class RecipeCreationError(Exception):
    """Basisklasse für Ausnahmen in der Rezepterstellung."""
    pass

class ModelError(Exception):
    """Basisklasse für Ausnahmen beim Aufrufen des LLM"""
    pass

class RecipeValidationError(RecipeCreationError):
    """Ausnahme für den Fall, dass ein Rezept nicht validiert werden kann."""
    def __init__(self, message="Das Rezept konnte nicht validiert werden."):
        self.message = message
        super().__init__(self.message)

class RecipeProposalError(RecipeCreationError):
    """Ausnahme für den Fall, dass kein Rezeptvorschlag erstellt werden kann."""
    def __init__(self, message="Es konnte kein Rezeptvorschlag erstellt werden."):
        self.message = message
        super().__init__(self.message)

class LLMInitializationError(ModelError):
    """Ausnahme für den Fall, dass der Key für das LLM nicht gültig ist."""
    def __init__(self, message="Der Key zum starten des LLM ist nicht gültig."):
        self.message = message
        super().__init__(self.message)