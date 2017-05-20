from pattern.en import pluralize, singularize
import time


WORDS_TO_PLURALIZE = [
"cat",
"computer",
"dog",
"women",
"fairy",
"aircraft",
"wolf",
"axis",
"child",
"diagnosis",
"fish",
"half"
]

def naive_pluralise(noun):
    if not noun:
        return noun
    elif noun.endswith('ch') or noun.endswith('x') or noun.endswith('s'):
        return noun + 'es'
    elif noun.endswith('y') and not (noun.endswith('ay') or noun.endswith('ey')
                                     or noun.endswith('iy') or noun.endswith('oy') or noun.endswith('uy')):
        return noun[:-1] + 'ies'
    else:
        return noun + 's'



if __name__=="__main__":
    elapsed_1 = elapsed_2 = 0
    for word in WORDS_TO_PLURALIZE:

        start_1 = time.clock()
        plur_1 = pluralize(word)
        elapsed_1 += time.clock()-start_1

        start_2 = time.clock()
        plur_2 = naive_pluralise(word)
        elapsed_2 += time.clock()-start_2


        print plur_1, plur_2

    print elapsed_1, elapsed_2
