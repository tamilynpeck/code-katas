def word_chains(start, end):
    chain = WordChain(start, end)
    # possible_words =

    word_chain = [start]

    # for word in chain.possible_words:
    #     word_chain = get_next_possible_word(possible_words, word, word_chain, end)
    #     if word_chain[-1] == end:
    #         break
    print(word_chain)

    return word_chain


# from itertools import permutations as perm

# call same function until equals the end?
# queue
# append, pop to left

# each word has a permutation
# stack?


class WordsAlpha:
    def get_words_of_len(word_len):
        """Import words from words_alpha.txt and return a list of words of length word_len"""
        with open("words_alpha.txt") as word_file:
            words = word_file.read().split()
        return [word for word in words if len(word) == word_len]


class WordChain:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.possible_words = self.get_possible_words_for_chain()
        self.word_chain = [start]

    def get_possible_words_for_chain(self):
        words = WordsAlpha.get_words_of_len(len(self.start))
        possible_words = [
            word
            for word in words
            for i, letter in enumerate(word)
            if letter == self.start[i] or letter == self.end[i]
        ]
        print(len(words))
        print(len(possible_words))
        return possible_words

    def get_next_possible_word(self, word_chain):
        current_word = word_chain[-1]
        letter_count = len(current_word)

        for word in self.possible_words:
            count = 0
            for i, letter in enumerate(word):
                if letter == current_word[i]:
                    count += 1
            if count == letter_count - 1:
                word_chain.append(word)

            if word == self.end:
                return word_chain
            self.get_next_possible_word(self.possible_words, word_chain)

        return word_chain
