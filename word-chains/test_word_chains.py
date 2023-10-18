from word_chains import word_chains

# test_cases = [
#     ["dog", "cat"],
#     ["gold", "lead"],
#     ["ruby", "code"],
#     ["code", "ruby"],
# ]


def test_word_chains_cat_to_dog():
    result = word_chains("cat", "dog")

    assert result == ["cat", "cot", "cog", "dog"]


# def test_word_chains_lead_to_gold():
#     result = word_chains("lead", "gold")

#     assert result == ["lead", "load", "goad", "gold"]
