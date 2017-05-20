from pattern.en import suggest
import enchant
from nltk.metrics import edit_distance


class SpellingReplacer(object):
    def __init__(self, dict_name='en', max_dist=2):
        self.spell_dict = enchant.Dict(dict_name)
        self.max_dist = max_dist

    def replace(self, word):
        if self.spell_dict.check(word):
            return word
        suggestions = self.spell_dict.suggest(word)

        if not suggestions:
            return word

        return min(suggestions, key=lambda sugg: edit_distance(word, sugg))

        # for sugg in suggestions:
        #     print sugg, edit_distance(word, sugg)


if __name__=="__main__":
    SENTENCE = 'Yesteday I wrnt to the pqrk!'.split(' ')

    print " ".join([suggest(word)[0][0] for word in SENTENCE])

    sr = SpellingReplacer()


    print " ".join([sr.replace(word) for word in SENTENCE])


    # print " ".join([d.suggest(word) for word in SENTENCE])
