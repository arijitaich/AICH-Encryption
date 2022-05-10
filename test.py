from a2 import aich

def get_word_list(language):
    lang_layer = {'eng':'a2/dict.txt', 'hin':'a2/hindi_dict.txt'}
    with open(lang_layer[language]) as f:
        return f.read().split()

class TestClass:
    # Test For Words Present Inside The Text Dictionary
    def test_one(self):
        words_to_test = get_word_list('eng')
        for word in words_to_test:
            assert aich.aichout(aich.aichin(word)) == word

    # Test For Alpha Numeric Words
    def test_two(self):
        words_to_test = get_word_list('eng')
        numeric_characters = '0123456789'
        new_test_words = [ a + "" + numeric_characters for a in words_to_test ]

        for word in new_test_words:
            assert aich.aichout(aich.aichin(word)) == word

    # Test For Special Character Alpha Numeric Words
    def test_three(self):
            words_to_test = get_word_list('eng')
            numeric_characters = '0123456789'
            special_characters = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
            new_test_words = [ a + numeric_characters + special_characters for a in words_to_test ]

            for word in new_test_words:
                assert aich.aichout(aich.aichin(word)) == word

    # Test For Any Other Language Word (Hindi)
    def test_four(self):
        words_to_test = get_word_list('hin')
        for word in words_to_test:
            assert aich.aichout(aich.aichin(word)) == word


    # Test For Any Other Language Word (Hindi) And Alpha Numeric Special Character Words
    def test_five(self):
            words_to_test = get_word_list('hin')
            numeric_characters = '0123456789'
            special_characters = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
            new_test_words = [ a + numeric_characters + special_characters for a in words_to_test ]

            for word in new_test_words:
                assert aich.aichout(aich.aichin(word)) == word