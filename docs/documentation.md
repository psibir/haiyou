## Haiyou - A Haiku Validator

Haiyou is a Python program that validates the structure and syllable count of a haiku. It provides a `HaikuValidator` class that checks if a given haiku adheres to the traditional 5-7-5 syllable structure of a haiku. The program uses the `pyphen` library for syllable counting and provides language support for English and French (additional languages can be added).

### Prerequisites

To run Haiyou, you need to have Python installed on your system. The program has been developed and tested using Python 3. It also requires the `pyphen` library, which can be installed using the following command:

```
pip install pyphen
```

### Usage

To use Haiyou, follow these steps:

1. Save the code in a Python file named `haiyou.py`.
2. Run the program by executing the Python file: `python haiyou.py`.
3. Enter a haiku when prompted. A haiku consists of three lines, with each line separated by a newline.
4. Select the language for syllable counting by entering either "en" for English or "fr" for French.
5. The program will validate the haiku and display either "Valid haiku!" or the specific errors if the haiku is invalid.

### HaikuValidator Class

The `HaikuValidator` class is the core component of Haiyou. It provides methods for validating the structure and syllable count of a haiku.

#### Methods

- `__init__(self, haiku, language='en')`: Initializes a new instance of the `HaikuValidator` class with the provided haiku and language (defaults to English).
- `count_syllables(self, word)`: Counts the number of syllables in a given word using the selected language.
- `validate_haiku(self)`: Validates the structure and syllable count of the haiku. Raises a `HaikuStructureError` if the haiku is invalid.
- `sanitize_input(input_str)`: Static method that sanitizes the input haiku by removing leading/trailing whitespace and converting it to lowercase.
- `select_language()`: Static method that prompts the user to select a supported language.

### Error Handling

Haiyou defines a custom exception class `HaikuStructureError` to handle haikus with incorrect structure. If the haiku structure is invalid (not exactly 3 lines or incorrect syllable count per line), a `HaikuStructureError` is raised with an appropriate error message.

### Unit Testing

To ensure the correctness of the code, unit tests have been implemented using the `unittest` framework. The tests cover both valid and invalid haikus, as well as the functionality of the `main` function. To run the tests, execute the following command:

```
python -m unittest test_haiyou.py
```

Make sure to adjust the import statements and file names according to your code structure.

---
With Haiyou, you can easily validate the structure and syllable count of haikus, ensuring they adhere to the traditional rules.
