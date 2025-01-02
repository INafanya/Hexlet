def make_censored(sentence, words):
    sentense_list = sentence.split(' ')
    censored_list = []
    cens_symbols = '$#%!'
    for w_s in sentense_list:
        print(w_s)
        text = ''
        for w_w in words:
            if text == cens_symbols: break
            print(w_w)
            if w_s == w_w:
                text = cens_symbols
                print(text)
            else:
                text = w_s
        censored_list.append(text)
    censored_text = ' '.join(censored_list)
    return censored_text


def make_censored(text, stop_words):
    words = text.split(' ')
    result = []

    for word in words:
        new_word = '$#%!' if word in stop_words else word
        result.append(new_word)

    return ' '.join(result)

#
# sentence1 = 'When you play the game of thrones, you win or you die'
# print(make_censored(sentence1, ['die', 'play']))
# # When you $#%! the game of thrones, you win or you $#%!
#
# sentence2 = 'chicken chicken? chicken! chicken'
# print(make_censored(sentence2, ['?', 'chicken']))
# # '$#%! chicken? chicken! $#%!';
#
# sentence3 = 'chicken chicken? chicken! ? chicken'
# print(make_censored(sentence3, ['?', 'chicken']))
# # '$#%! chicken? chicken! $#%! $#%!'


sentence4 = 'chicken chicken? chicken! ? ! @ chicken'
print(make_censored(sentence4, ['?', '!', '@', 'chicken']))
# '$#%! chicken? chicken! $#%! $#%! $#%! $#%!'
