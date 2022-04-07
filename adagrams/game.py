from random import sample


LETTER_DICT = {
    'A': {'count': 9, 'score': 1}, 
    'B': {'count': 2, 'score': 3}, 
    'C': {'count': 2, 'score': 3}, 
    'D': {'count': 4, 'score': 2}, 
    'E': {'count': 12, 'score': 1}, 
    'F': {'count': 2, 'score': 4}, 
    'G': {'count': 3, 'score': 2}, 
    'H': {'count': 2, 'score': 4}, 
    'I': {'count': 9, 'score': 1}, 
    'J': {'count': 1, 'score': 8}, 
    'K': {'count': 1, 'score': 5}, 
    'L': {'count': 4, 'score': 1}, 
    'M': {'count': 2, 'score': 3}, 
    'N': {'count': 6, 'score': 1}, 
    'O': {'count': 8, 'score': 1}, 
    'P': {'count': 2, 'score': 3}, 
    'Q': {'count': 1, 'score': 10}, 
    'R': {'count': 6, 'score': 1}, 
    'S': {'count': 4, 'score': 1}, 
    'T': {'count': 6, 'score': 1}, 
    'U': {'count': 4, 'score': 1}, 
    'V': {'count': 2, 'score': 4}, 
    'W': {'count': 2, 'score': 4}, 
    'X': {'count': 1, 'score': 8}, 
    'Y': {'count': 2, 'score': 4}, 
    'Z': {'count': 1, 'score': 10}
}


def draw_letters():
    """Returns a list of 10 random letters from LETTER_DICT"""

    letters = LETTER_DICT.keys()
    frequency = [letter['count'] for letter in LETTER_DICT.values()] 
    
    return sample(letters, counts=frequency, k=10)


# Helper function
def get_letter_count(sequence):
    """Returns a dictionary containing the frequency of each character from a sequence"""

    frequency_dict = {}

    for character in sequence:
        if character not in frequency_dict:
            frequency_dict[character] = 1
        else: 
            frequency_dict[character] += 1

    return frequency_dict


def uses_available_letters(word, letter_bank):
    """Returns True if word uses only letters from letter_bank
    Returns False if word uses letters not from letter_bank"""

    word_count_dict = get_letter_count(word.upper())
    letter_bank = get_letter_count(letter_bank)

    for character, count in word_count_dict.items():
        if count > letter_bank.get(character, 0):
            return False

    return True


def score_word(word):
    """Return the score of a word according to SCORE_DICT mapping"""
    
    score = 0

    for letter in word.upper():
        if letter in LETTER_DICT:
            score += LETTER_DICT[letter]["score"]
    
    # if the length of the word is 7, 8, 9, or 10 
    # then the word gets an additional 8 points
    if len(word) in [7,8,9,10]:
        score += 8
        
    return score


def get_highest_word_score(word_list):
    """Returns a word with the highest score & its score 
    from a list of words.
    """

    highest_score = 0
    highest_score_word = None

    for word in word_list:
        current_score = score_word(word)

        # when a strictly better scored word found
        if current_score > highest_score:
            highest_score = current_score
            highest_score_word = word

        # in case of tie
        elif current_score == highest_score and len(highest_score_word) != 10:
            if len(word) == 10 or len(word) < len(highest_score_word):
                highest_score_word = word

    return highest_score_word, highest_score
