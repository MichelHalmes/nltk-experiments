from pattern.en import wordnet, NOUN

from pattern.en.wordlist import PROFANITY
from nltk.corpus import wordnet as wn_nltk
# print PROFANITY



def get_synonym_pat(word):
    synset = wordnet.synsets(word, pos=NOUN)[0]

    print [str(syn) for syn in synset.synonyms] \
     + [str(syn) for hyp in synset.hypernyms() for syn in hyp.synonyms ]

def get_synonym_nltk(word):

    synset = wn_nltk.synsets(word)[0]

    print [str(syn) for syn in synset.lemma_names()]


if __name__=="__main__":
    word = 'computer_screen'
    get_synonym_pat(word)
    get_synonym_nltk(word)
