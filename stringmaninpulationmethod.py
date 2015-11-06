madlib = [
    ['text', "Once upon a time there was a "],
    ['slot', "an adjective"],
    ['text', ", "],
    ['slot', "another adjective"],
    ['text', " "],
    ['slot', "an animal"],
    ['text', ". He liked to "],
    ['slot', "a verb in the present tense"],
    ['text', " all day. One day, he went to "],
    ['slot', "an adjective"],
    ['text', " "],
    ['slot', "a place"],
    ['text', " to meet "],
    ['slot', "a person"],
    ['text', "."],
    ]

story = ""

for piece in madlib:
    if piece[0] == 'text':
        story += piece[1]
    elif piece[0] == 'slot':
        prompt = "Give me " + piece[1] + ": "
        answer = raw_input(prompt)
        story += answer

print story