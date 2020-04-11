#Q What is a Hash Table, and what is the average case and worst case time for each of its operations? How can we use this structure to find all anagrams in a dictionary?

#A. A Hash Table is a data structure for mapping values to keys of arbitrary type. The Hash Table consists of a sequentially enumerated array of buckets of a certain length. We assign each possible key to a bucket by using a hash function - a function that returns an integer number (the index of a bucket) for any given key. Multiple keys can be assigned to the same bucket, so all the (key, value) pairs are stored in lists within their respective buckets.
# Choosing the right hashing function can have a great impact on performance. A hash function that is good for a dataset that we want to store will result in hashes of different keys being a rare occurrence. Even though accessing, inserting and deleting have a worst case time complexity of O(N) (where N is the number of elements in the Hash Table), in practice we have an average time complexity of O(1).
# To find all anagrams in a dictionary, we just have to group all words that have the same set of letters in them. So, if we map words to strings representing their sorted letters, we could group words into lists by using their sorted letters as a key.
# FUNCTION find_anagrams(words)
# word_groups = HashTable<String, List>
# FOR word IN words
# word_groups.get_or_default(sort(word), []).push(word)
# END FOR
# anagrams = List
# FOR key, value IN word_groups
# anagrams.push(value)
# END FOR
# RETURN anagrams
# The hash table stores lists mapped to strings. For each word, we add it to the list at the appropriate key, or make a new list and add it to it then. On average, for a dictionary of N words of length less or equal to L, this algorithm works with an average time complexity of O(N L log L).


