import os
import re
import pyphen
import random
from haiku_validator import HaikuValidator, HaikuStructureError

class HaikuGenerator:
    def __init__(self, data_source):
        self.data_source = data_source

    def count_syllables(self, word):
        """Count the number of syllables in a word using Pyphen."""
        dic = pyphen.Pyphen(lang='en')
        return len(dic.inserted(word).split('-'))

    def read_corpus(self, directory):
        """Read text files from the specified directory and extract words."""
        words = []
        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                filepath = os.path.join(directory, filename)
                with open(filepath, "r", encoding="utf-8") as file:
                    for line in file:
                        line = line.strip().lower()
                        words.extend(re.findall(r"[\w']+|[.,!?;]", line))
        return words

    def create_markov_chain(self, words):
        """Create a Markov chain based on the input words."""
        chain = {}
        prefix = ("", "")

        for word in words:
            if word in [".", ",", "!", "?", ";"]:
                prefix = ("", "")
                continue

            if prefix not in chain:
                chain[prefix] = []

            chain[prefix].append(word)
            prefix = (prefix[1], word)

        return chain

    def generate_markov_haiku(self, chain):
        """Generate a haiku using the Markov chain."""
        haiku = ""
        line_syllables = [5, 7, 5]

        for syllables in line_syllables:
            line = self.generate_markov_line(chain, syllables)
            haiku += line + "\n"

        return haiku.strip()

    def generate_markov_line(self, chain, syllables):
        """Generate a line of the haiku using the Markov chain and the desired syllable count."""
        line = ""
        current_syllables = 0
        prefix = random.choice(list(chain.keys()))

        while current_syllables < syllables:
            if prefix not in chain:
                break

            suffix = random.choice(chain[prefix])
            word_syllables = self.count_syllables(suffix)

            if current_syllables + word_syllables <= syllables:
                line += suffix + " "
                current_syllables += word_syllables
                prefix = (prefix[1], suffix)
            else:
                break

        return line.strip()

    def generate_haiku(self):
        words = self.read_corpus(self.data_source)
        chain = self.create_markov_chain(words)
        generated_haiku = self.generate_markov_haiku(chain)
        return generated_haiku.split("\n")
