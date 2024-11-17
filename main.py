def word_available(word, letters):
    return True

def filter_words(input_file, output_file, letters):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    words = content.split()

    all_valid_words = [word for word in words if word_available(word, letters)]

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(' '.join(all_valid_words))

filter_words('./words.txt', 'output.txt', 'test')
