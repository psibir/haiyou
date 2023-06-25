import random
import os
import sqlite3
from haiku_validator import HaikuValidator

class HaikuGenerator:
    def __init__(self, data_source):
        self.data_source = data_source
        self.chain = self.build_markov_chain()
        self.validator = HaikuValidator()

    def build_markov_chain(self):
        chain = {}
        if os.path.isfile(self.data_source):
            # Handle a single text file
            with open(self.data_source, 'r') as file:
                lines = file.readlines()
        elif os.path.isdir(self.data_source):
            # Handle a directory of text files
            lines = []
            for file_name in os.listdir(self.data_source):
                file_path = os.path.join(self.data_source, file_name)
                if os.path.isfile(file_path):
                    with open(file_path, 'r') as file:
                        lines.extend(file.readlines())
        else:
            # Assume it's a database file
            conn = sqlite3.connect(self.data_source)
            cursor = conn.cursor()
            cursor.execute("SELECT line FROM haiku")
            lines = [row[0] for row in cursor.fetchall()]
            conn.close()

        chain = self.build_chain_from_lines(lines)
        return chain

    def build_chain_from_lines(self, lines):
        chain = {}
        for line in lines:
            words = line.strip().split()
            for i in range(len(words) - 1):
                current_word = words[i]
                next_word = words[i + 1]
                if current_word in chain:
                    chain[current_word].append(next_word)
                else:
                    chain[current_word] = [next_word]
        return chain

    def generate_line(self, seed_word, syllables):
        line = [seed_word]
        current_syllables = self.validator.count_syllables(seed_word)
        while current_syllables < syllables:
            if line[-1] in self.chain:
                next_word = random.choice(self.chain[line[-1]])
                line.append(next_word)
                current_syllables += self.validator.count_syllables(next_word)
            else:
                break
        if current_syllables == syllables:
            return " ".join(line)
        else:
            return None

    def generate_haiku(self):
        haiku = []
        haiku.append(self.generate_line(random.choice(list(self.chain.keys())), 5))
        haiku.append(self.generate_line(random.choice(list(self.chain.keys())), 7))
        haiku.append(self.generate_line(random.choice(list(self.chain.keys())), 5))
        return haiku
