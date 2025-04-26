def mad_libs_generator():
    template = "The [ADJECTIVE] [NOUN] [VERB] [ADVERB] down the [NOUN]"

    print("Welcome to Mad Libs!")
    print("Please enter the words requested below t to fill in the blanks of the story:\n")
    print(template)

    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adverb = input("Enter an adverb: ")
    another_noun = input("Enter another noun: ")

    template = template.replace("[ADJECTIVE]", adjective, 1)
    template = template.replace("[NOUN]", noun, 1)
    template = template.replace("[VERB]", verb, 1)
    template = template.replace("[ADVERB]", adverb, 1)
    template = template.replace("[NOUN]", another_noun, 1)

    print(template)

    pass


mad_libs_generator()