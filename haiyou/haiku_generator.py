import random
import os
from haiku_validator import HaikuValidator
from collections import defaultdict

class HaikuGenerator:
    def __init__(self, data_source="haiyou/corpus"):
        if not os.path.isdir(data_source):
            raise NotADirectoryError(f"Data source '{data_source}' is not a directory.")

        self.data_source = data_source
        self.chain = self.build_markov_chain()
        self.validator = HaikuValidator()
        self.line_starters = self.find_line_starters()

    def read_lines_from_file(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return lines

    def build_markov_chain(self):
        chain = defaultdict(list)
        lines = []
        for file_name in os.listdir(self.data_source):
            file_path = os.path.join(self.data_source, file_name)
            if os.path.isfile(file_path):
                lines.extend(self.read_lines_from_file(file_path))

        for line in lines:
            words = line.strip().split()
            for i in range(len(words) - 1):
                current_word = words[i]
                next_word = words[i + 1]
                chain[current_word].append(next_word)

        return chain

    def find_line_starters(self):
        return [word for word in self.chain.keys() if word[0].isupper()]

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
        return " ".join(line) if current_syllables == syllables else None

    def generate_haiku(self):
        haiku = [self.generate_line(random.choice(self.line_starters), 5),
                 self.generate_line(None, 7),
                 self.generate_line(None, 5)]
        return haiku

# Example usage:
data_source = "haiyou/corpus"  # Replace with the desired corpus directory path
generator = HaikuGenerator(data_source=data_source)
new_haiku = generator.generate_haiku()
print("Generated Haiku:")
for line in new_haiku:
    print(line)
