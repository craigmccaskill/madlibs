
story_base = {
	1: "Once upon a time there was a",
	2: "noun",
	3: "who liked",
	4: "infinitive verb",
	5: "adverb"
}

slots = [2, 4, 5]

def get_input(story_base):
	bits = {}
	for slot in slots:
	    # bits[2]  =            Give me a + noun
		bits[slot] = raw_input("Give me a " + story_base[slot] + ": ")
	return bits


def create_story(bits, story_base):
	
	# { 2: "dog", 4: "to play", 5: "roughly"}
	new_story = story_base.update(bits)
	words = [story_base.get(index) for index in sorted(story_base.keys())]
	return " ".join(words)


if __name__=="__main__":
	bits = get_input(story_base)
	print create_story(bits, story_base)