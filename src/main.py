from letters import values


def word_value(word):
    value = 0

    for char in word:
        value += values.get(char, None)

    return value

def word_available(word, letters):
    available_letters = letters.copy()

    for char in word:
        if char in available_letters:
            available_letters.remove(char)
        else:
            return False
    return True

def filter_words(input_file, output_file, letters):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    words = content.split()

    all_valid_words = [word for word in words if word_available(word, letters)]

    all_valid_words.sort(key=word_value, reverse=True)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(' '.join(all_valid_words))

if __name__ == "__main__":
    letters = input("Quelles lettres avez-vous dans votre jeu ? ")
    filter_words('./words.txt', './output.txt', list(letters))
