def sponge_case(sentence):
    # Write your solution here!
    # To solve the sponge case problem, the main idea is to:
    # - Process each word individually,
    # - Convert the first letter of each word to lowercase,
    # - Then alternate the casing (uppercase/lowercase) for each following letter in that word.

    words = sentence.split()
    modified_words = []

    for word in words:
        modified_word = ""
        index = 0
        for char in word:
            if index % 2 == 0:
                modified_word += char.lower()
            else:
                modified_word += char.upper()
            index +=1
        modified_words.append(modified_word)
    
    return " ".join(modified_words)





# Test cases
assert sponge_case("spongebob") == "sPoNgEbOb"
assert sponge_case("Who are YOU calling A Pinhead") == "wHo aRe yOu cAlLiNg a pInHeAd"
assert sponge_case("WHAT is UP my dude") == "wHaT iS uP mY dUdE"
assert sponge_case("E") == "e"
assert sponge_case("e") == "e"

print("All tests passed!")
print("Discuss time and space complexity if there's time remaining")