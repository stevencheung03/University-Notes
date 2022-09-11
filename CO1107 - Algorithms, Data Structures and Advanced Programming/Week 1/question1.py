def letter_counter(word):
	word_length = len(word)

	word_split = list(word)

	letter_frequency = {}

	for i in range(0, len(word_split)):
		if word_split[i] in letter_frequency:
			letter_frequency[word_split[i]] = letter_frequency.get(word_split[i], 0) + 1
		else: 
			letter_frequency[word_split[i]] = 1

	return word_length, letter_frequency

print(letter_counter("yoooootg"))