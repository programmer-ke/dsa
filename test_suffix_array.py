from suffix_array import SuffixArray


def test_find_shortest_basic():
    sa = SuffixArray("banana")
    assert sa.find_shortest("a") == "a"
    assert sa.find_shortest("an") == "ana"
    assert sa.find_shortest("ban") == "banana"
    assert sa.find_shortest("na") == "na"
    assert sa.find_shortest("zz") is None


def test_find_longest_basic():
    sa = SuffixArray("banana")
    assert sa.find_longest("a") == "anana"
    assert sa.find_longest("an") == "anana"
    assert sa.find_longest("ban") == "banana"
    assert sa.find_longest("na") == "nana"
    assert sa.find_longest("zz") is None


def test_find_all_basic():
    sa = SuffixArray("banana")
    assert sa.find_all("a") == ["a", "ana", "anana"]
    assert sa.find_all("an") == ["ana", "anana"]
    assert sa.find_all("ban") == ["banana"]
    assert sa.find_all("na") == ["na", "nana"]
    assert sa.find_all("zz") == []


def test_single_character_haystack():
    sa = SuffixArray("a")
    assert sa.find_shortest("a") == "a"
    assert sa.find_longest("a") == "a"
    assert sa.find_all("a") == ["a"]
    assert sa.find_shortest("b") is None
    assert sa.find_all("b") == []


def test_empty_haystack():
    sa = SuffixArray("")
    assert sa.find_shortest("a") is None
    assert sa.find_longest("a") is None
    assert sa.find_all("a") == []


def test_needle_longer_than_haystack():
    sa = SuffixArray("abc")
    assert sa.find_shortest("abcd") is None
    assert sa.find_longest("abcd") is None
    assert sa.find_all("abcd") == []


def test_needle_equals_haystack():
    sa = SuffixArray("abc")
    assert sa.find_shortest("abc") == "abc"
    assert sa.find_longest("abc") == "abc"
    assert sa.find_all("abc") == ["abc"]


def test_repeated_characters():
    sa = SuffixArray("aaaa")
    assert sa.find_shortest("aa") == "aa"
    assert sa.find_longest("aa") == "aaaa"
    assert sa.find_all("aa") == ["aa", "aaa", "aaaa"]


def test_case_sensitivity():
    sa = SuffixArray("Banana")
    assert sa.find_shortest("ban") is None
    assert sa.find_shortest("Ban") == "Banana"
    assert sa.find_all("ban") == []


def test_empty_needle():
    sa = SuffixArray("abc")
    assert sa.find_all("") == ["abc", "bc", "c"]
    assert sa.find_shortest("") == "c"
    assert sa.find_longest("") == "abc"


def test_find_shortest_returns_shortest_not_first_lexicographic():
    sa = SuffixArray("aab")
    assert sa.find_shortest("a") == "ab"  # currently returns "aab"
