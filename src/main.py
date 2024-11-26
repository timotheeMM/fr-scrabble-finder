values = {
    "a": 1,
    "b": 3,
    "c": 3,
    "d": 2,
    "e": 1,
    "f": 4,
    "g": 2,
    "h": 4,
    "i": 1,
    "j": 8,
    "k": 10,
    "l": 1,
    "m": 2,
    "n": 1,
    "o": 1,
    "p": 3,
    "q": 8,
    "r": 1,
    "s": 1,
    "t": 1,
    "u": 1,
    "v": 4,
    "w": 10,
    "x": 10,
    "y": 10,
    "z": 10
}

# Exemple d'utilisation
lettre = "e"
valeur = values.get(lettre, None)

if valeur is not None:
    print(f"La lettre '{lettre}' a une valeur de {valeur} au Scrabble.")
else:
    print(f"La lettre '{lettre}' n'a pas de valeur attribuée.")

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

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(' '.join(all_valid_words))

if __name__ == "__main__":
    letters = input("Quelles lettres avez-vous dans votre jeu ? ")
    filter_words('./words.txt', './output.txt', list(letters))
