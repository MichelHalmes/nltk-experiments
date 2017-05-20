from pattern.en import parse
from pattern.en import pprint
from pattern.en import tag
import nltk
import re
import time

# pprint(parse('I eat pizza with a fork.', relations=True, lemmata=True))
# print tag('I work in the IT sector')


QUERIES = [
"ink for printer",
"shoes for ladies",

]


def filter_prep_regex(query):
    return [query for query in query.split(' ') if not _PREPOSITION_REGEX.match(query)]

def filter_prep_tag(query):
    return [query for query, pos in tag(query) if pos!='IN' ]

def filter_prep_nltk(query):
    return [query for query, pos in nltk.pos_tag(query) if pos!='IN' ]




def main():
    elapsed_1 = elapsed_2 = elapsed_3 = 0
    for query in QUERIES:

        start_1 = time.clock()
        filt_1 = filter_prep_regex(query)
        elapsed_1 += time.clock()-start_1

        start_2 = time.clock()
        filt_2 = filter_prep_tag(query)
        elapsed_2 += time.clock()-start_2

        start_3 = time.clock()
        filt_3 = filter_prep_nltk(query)
        elapsed_3 += time.clock()-start_3


        print filt_1, filt_2, filt_3

    print elapsed_1, elapsed_2, elapsed_3





_PREPOSITION_REGEX = re.compile('^({})$'.format(
    '|'.join(['about',
              'above',
              'abreast',
              'abroad',
              'absent',
              'across',
              'adjacent',
              'after',
              'a?gainst',
              'along',
              'alongside',
              'amid',
              'amidst',
              'among',
              'amongst',
              'mong',
              'around',
              'round',
              'as',
              'astride',
              '(at|@)',
              'atop',
              'ontop',
              'before',
              'behind',
              'below',
              'beneath',
              'neath',
              'beside',
              'besides',
              'between',
              'beyond',
              'but',
              'by',
              'circa',
              'come',
              'despite',
              'spite',
              'down',
              'during',
              'except',
              'for|4',
              'from',
              'in',
              'inside',
              'into',
              'less',
              'like',
              'minus',
              'near(er|est)?',
              'of',
              'on',
              'onto',
              'opposite',
              'out',
              'outside',
              'over',
              'past',
              'per',
              'post',
              'pre',
              'pro',
              're',
              'sans',
              'save',
              'short',
              'since',
              'than',
              'through|thru',
              'thr(ough|u)out',
              'to|2',
              'toward(s?)',
              'under',
              'underneath',
              'unlike',
              '(un)?til',
              'up',
              'upon',
              'upside',
              'via',
              'with',
              'within',
              'without',
              'worth',
    ])))

if __name__=="__main__":
    main()
