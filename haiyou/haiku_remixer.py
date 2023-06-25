import random
import nltk
from nltk.corpus import wordnet
from haiku_validator import HaikuValidator

class HaikuRemixer:
    def __init__(self, haikus):
        self.haikus = haikus
        self.validator = HaikuValidator()

    def get_similar_words(self, word):
        synsets = wordnet.synsets(word)
        similar_words = []
        for synset in synsets:
            similar_words.extend([lemma.name() for lemma in synset.lemmas()])
        return similar_words

    def remix_haiku(self):
        lines = [line.split() for haiku in self.haikus for line in haiku.split("\n")]
        unique_words = set(word for line in lines for word in line)
        word_similarity = {}

        for word in unique_words:
            similar_words = self.get_similar_words(word)
            similar_words = [w for w in similar_words if w != word and w in unique_words]
            word_similarity[word] = similar_words

        remixed_haiku = []
        for line in lines:
            remixed_line = []
            for word in line:
                if word in word_similarity:
                    similar_words = word_similarity[word]
                    if similar_words:
                        remixed_line.append(random.choice(similar_words))
                    else:
                        remixed_line.append(word)
                else:
                    remixed_line.append(word)
            remixed_haiku.append(" ".join(remixed_line))

        return remixed_haiku
