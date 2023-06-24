# Haiyou

Haiyou is a Python program that allows you to validate the structure and syllable count of a haiku. It checks if a given haiku follows the traditional 5-7-5 syllable pattern and has exactly three lines. The program supports multiple languages using the Pyphen library for syllable counting.

## Requirements

- Python 3.6 or above
- Pyphen library

## Installation

1. Clone the repository or download the `haiyou.py` file.
2. Install the required dependencies by running the following command:

   ```bash
   pip install -r requirements.txt
   ```

   This will install the Pyphen library needed for syllable counting.

## Usage

1. Run the program using the following command:

   ```bash
   python haiyou.py
   ```

2. Enter a haiku when prompted. Make sure to follow the 5-7-5 syllable pattern and use exactly three lines.
3. Select the language (English or French) by entering `en` or `fr` when prompted.

## Example

Here's an example interaction with the Haiyou program:

```
Enter a haiku: An old silent pond
Enter the language (en/fr): en
Valid haiku!
```

## Customization

### Adding more supported languages

To add more supported languages for haiku validation, modify the `supported_languages` set in the `select_language()` function located in `haiyou.py`. Simply add the language code to the set. For example, to support Spanish and Japanese, the set would be updated as follows:

```python
supported_languages = {'en', 'fr', 'es', 'ja'}
```

### Extending the program

The Haiyou program can be extended to incorporate additional validation rules or customized features. You can modify the `HaikuValidator` class or add new functions to enhance the haiku validation process according to your requirements.

## License

This project is licensed under the MIT License. Feel free to use and modify it as per your needs.

## Acknowledgments

The Haiyou program uses the Pyphen library for syllable counting, which is based on the hyphenation dictionaries created by Franklin Mark Liang.
