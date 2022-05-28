from nose.tools import *
from Example48 import Lexicon
from Example48 import Parser

def test_direction():
    assert_equal(Lexicon.scan("north"), [("direction", "north")])
    result = Lexicon.scan("north south east")
    assert_equal(result, [("direction", "north"),
                          ("direction", 'south'),
                          ('direction', 'east')])


def test_verbs():
    assert_equal(Lexicon.scan("go"), [("verb", "go")])
    result = Lexicon.scan("go kill eat")
    assert_equal(result, [("verb", "go"),
                          ("verb", 'kill'),
                          ('verb', 'eat')])

def test_stops():
    assert_equal(Lexicon.scan("the"), [('stop', 'the')])
    result = Lexicon.scan('the in of')
    assert_equal(result, [('stop', 'the'), ('stop', 'in'), ('stop', 'of')])

def test_nouns():
    assert_equal(Lexicon.scan('bear'), [('noun', 'bear')])
    result = Lexicon.scan("bear princess")
    assert_equal(result, [("noun", "bear"),
                          ("noun", "princess")])


def test_numbers():
    assert_equal(Lexicon.scan("1234"), [('number', 1234)])
    result = Lexicon.scan("3 91234")
    assert_equal(result, [('number', 3), ('number', 91234)])



def test_errors():
    assert_equal(Lexicon.scan("ASDFADFASDF"),
                 [('error', 'ASDFADFASDF')])
    result = Lexicon.scan("bear IAS princess")
    assert_equal(result, [('noun', 'bear'),
                          ('error', "IAS"),
                          ('noun', 'princess')])


def my_tests():
    result = Lexicon.scan("NoRtH kILL thE BeAR PRINcess")
    assert_equal(result, [('direction', 'north'),
                          ('verb', 'kill'),
                          ('stop', 'the'),
                          ('noun', 'bear'),
                          ('noun', 'princess')])

def example48_tests():
    # Now run the tests:
    test_direction()
    test_verbs()
    test_stops()
    test_nouns()
    test_numbers()
    test_errors()
    my_tests()


def example49_tests():
    # Simple examples first:
    sentence = "The bear run south"
    result = Lexicon.scan(sentence)
    assert_equal(result, [('stop', 'the'), ('noun', 'bear'), ('verb', 'run'),
                          ('direction', 'south')])

    result = [('stops', 'teh'), ('noun', 'bear'), ('berb', 'run'),
              ('direction', 'south')]

    # Now parse the sentence using Parser.
    assert_raises(Parser.ParserError, Parser.parse_sentence, result)

    # Random crash:
    foo = [('this', 'the'), ('should', 'not'), ('work', 'but'),
           ('no', 'one'), ('will', 'know'), ('that', '.')]
    assert_raises(Parser.ParserError, Parser.parse_sentence, foo)



# Now run the tests:
#example48_tests()
example49_tests()
