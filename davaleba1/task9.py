# 9. დაწერეთ პროგრამა, რომელიც კითხულობს ტექსტს (ერთ სტრიქონს), ადგენს სიტყვების სიხშირეს
# (Case-insensitive), გამორიცხავს პუნქტუაციას, და ბეჭდავს Top-5 ყველაზე ხშირად გამოყენებულ სიტყვას
# სიხშირით; თანაბრობის შემთხვევაში დაალაგეთ ანბანურად.


import string


def get_word_frequencies(text):
    # 1. პუნქტუაციის წაშლა და პატარა ასოებში გადაყვანა
    # string.punctuation შეიცავს ყველა სიმბოლოს
    clean_text = ""
    for char in text.lower():
        if char not in string.punctuation:
            clean_text += char
        else:
            clean_text += " "

    # 2. სიტყვებად დაყოფა და სიხშირის დათვლა
    words = clean_text.split()
    freq_map = {}
    for word in words:
        freq_map[word] = freq_map.get(word, 0) + 1

    # 3. დახარისხება (ანბანურად და სიხშირის მიხედვით)
    all_words_sorted = sorted(freq_map.items(), key=lambda x: x[0])
    top_5 = sorted(all_words_sorted, key=lambda x: x[1], reverse=True)[:5]

    return top_5


input_text = "Apple, banana, apple! Orange - banana. Apple, grape, grape, kiwi, lemon, kiwi."
result = get_word_frequencies(input_text)

print("Top 5 სიტყვა:")
for word, count in result:
    print(f"{word}: {count}")