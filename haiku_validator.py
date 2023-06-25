import pyphen
import re

class HaikuStructureError(Exception):
    pass

class HaikuValidator:
    """Class to validate the structure and syllable count of a haiku."""

    def __init__(self, haiku, language='en'):
        self.haiku = haiku.lower()
        self.language = language
        self.syllable_counter = pyphen.Pyphen(lang=language)

    def count_syllables(self, word):
        """Count the number of syllables in a word."""
        syllables = self.syllable_counter.inserted(word).split("-")
        return len(syllables)

    def validate_haiku(self):
        """Validate the haiku's structure and syllable count."""
        lines = self.haiku.split("\n")

        if len(lines) != 3:
            raise HaikuStructureError("Haiku must have exactly 3 lines.")

        structure_errors = []
        for i, line in enumerate(lines):
            words = re.findall(r"[\w']+", line)
            syllable_count = sum(self.count_syllables(word) for word in words)

            if (i == 0 or i == 2) and syllable_count != 5:
                structure_errors.append(f"Incorrect syllable count in line {i+1}: expected 5, got {syllable_count}")
            elif i == 1 and syllable_count != 7:
                structure_errors.append(f"Incorrect syllable count in line {i+1}: expected 7, got {syllable_count}")

        if structure_errors:
            raise HaikuStructureError("\n".join(structure_errors))

        return True

def sanitize_input(input_str):
    """Sanitize the input haiku by removing leading/trailing whitespace and converting to lowercase."""
    return input_str.strip().lower()

def select_language():
    """Prompt the user to select a supported language."""
    supported_languages = {'en', 'fr'}  # Add more languages if needed
    language = input("Enter the language (en/fr): ").lower()

    if language not in supported_languages:
        print("Invalid language selection. Defaulting to English.")
        language = 'en'

    return language
