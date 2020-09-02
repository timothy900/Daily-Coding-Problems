''' 5/22/2020

This problem was asked by Google.

Given a word W and a string S, find all 
starting indices in S which are anagrams of W.

For example, given that W is "ab", and S is "abxaba", 
return 0, 3, and 4.
'''

from collections import Counter


# find anagrams of str1 in str2
def search_anagram(str1, str2):
	anagrams = []
	for i, char in enumerate(str2):
		if char in str1: 
			# portion of str2 that could possibly be an anagram of str2
			portion = str2[i:i+len(str1)]

			# number of each char in the portion and in str1
			n_char_portion = dict(Counter(list(portion)))
			n_char_str1 = dict(Counter(list(str1)))

			# if the amount of each char in each str is equal, it's an anagram
			if n_char_portion == n_char_str1:
				anagrams.append(i)

	return anagrams


W = 'ab'
S = "abxaba"
print(search_anagram(W, S))
