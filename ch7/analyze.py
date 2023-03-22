"""В модуле analyze вычисляется индекс удобочитаемости Флеша-Кикейда
для заданного текста и на основе полученной оценки определяется
уровень удобочитаемости текста

"""

def count_syllables(words):
    """Эта функция получает список слов и возвращает общее
    число слогов во всех словах
    """
    count = 0

    for word in words:
        word_count = count_syllables_in_word(word)
        count = count + word_count

    return count

def count_syllables_in_word(word):
    """Эта функия получает слово в строковом формате и возвращает
       число слогов в немю Учтите, что это эвристическая функция, 
       поэтому её результат не всегда будет точным на 100%
    """
    count = 0

    endings = '.,;!?:' # это возможные знаки препинания в конце слов
    last_char = word[-1]

    if last_char in endings:
        processed_word = word[0:-1]
    else:
        processed_word = word

    if len(processed_word) <= 3:
        return 1

    if processed_word[-1] in 'eE':
        processed_word = processed_word[0:-1]

    vowels = "aeiouAEIOU"
    prev_char_was_vowels = False

    for char in processed_word:
        if char in vowels:
            if not prev_char_was_vowels:
                count = count + 1
            prev_char_was_vowels = True
        else:
            prev_char_was_vowels = False

    if processed_word[-1] in 'yY':
        count = count + 1

    return count

def count_sentences(text):
    """Эта функция подсчитывает число предложений в тексте, 
       используяточки, вопросительный и восклицательный знаки в 
       качестве концевых символов
    """
    count = 0

    terminals = '.?!'
    for char in text:
        if char in terminals:
            count = count + 1
    return count

def output_results(score):
    """Эта функция получает индекс Флешка-Кинкейда и сообщает 
       соответствующий ему уровень удобочитаемости текста.
    """
    if score >= 90:
        print('Уровень 5-го класса')
    elif score >= 80:
        print('Уровень 6-го класса')
    elif score >= 70:
        print('Уровень 7-го класса')
    elif score >= 60:
        print('Уровень 8-9-го класса')
    elif score >= 50:
        print('Уровень 10-11-го класса')
    elif score >= 30:
        print('Уровень студента вуза')
    else:
        print('Уровень выпускника вуза')

def compute_readability(text):
    """Эта функция получает строку текста произвольной длины и 
       сообщает уровень удобочитаемости в соответствии с 
       имеющейся шкалой оценок
    """
    total_words = 0
    total_sentences = 0
    total_syllables = 0
    score = 0

    words = text.split()
    total_words = len(words)
    total_sentences = count_sentences(text)
    total_syllables = count_syllables(words)

    score = (206.835 - 1.015 * (total_words / total_sentences)
                - 84.6 * (total_syllables / total_words))
    print(score)
    output_results(score)

if __name__ == "__main__":
    import ch1text
    print('Текст главы 1:')
    compute_readability(ch1text.text)
