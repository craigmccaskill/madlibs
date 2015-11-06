import re
import random

story_base = """
Once upon a time there was a {random1} {noun} who liked to {verb} with {noun2}.
This particular {noun} was a very {random2} {noun} and he liked {noun2} a little too much..
It made him very {adjective2} and made it hard for him to {verb2} with {random3} {noun3}!
""" 

with open('data/adjectives1.txt') as f:
    adjectives = f.readlines()

adjectives = [a.strip() for a in adjectives]


variable_finder = re.compile('{\w+}')

number_finder = re.compile('([a-zA-Z]+)([0-9])*')


def get_input(story_base):
    variables = variable_finder.findall(story_base)
    bits = {}

    for variable in variables:
        variable = variable[1:-1]  # trim off the first { and the last } to get the actual name
        if variable in bits:  # if we already asked for it, it'll be stored in the bits dictionary
            continue
        # split into the name for the prompt (noun) and find whether there's a number at the end
        pieces = number_finder.search(variable).groups()
        type_of_variable = pieces[0]  # eg "noun" from "noun2"

        if type_of_variable == "random":
            bits[variable] = random.choice(adjectives)
            continue

        prompt = "a"
        if variable[0] in ('a', 'e', 'i', 'o', 'u'):
            prompt = "an"

        if pieces[1] is not None: # the number regex matched too eg 2 from noun2
            prompt = random.choice(["another", "a different", "a new", "a spooky", "a scary", "your favourite", "an unusual", "your grandmother's"])
        bits[variable] = raw_input("Give me " + prompt + " " + type_of_variable + ": ")
    return bits


def create_story(bits, story_base):
    return story_base.format(**bits)


if __name__=="__main__":
    bits = get_input(story_base)
    print create_story(bits, story_base)