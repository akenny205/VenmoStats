import string
from nltk.corpus import words
from collections import Counter
import re
from venmo import get_all_first_and_last_names


word_list = set(words.words())


# Regular expression pattern to match emojis
emoji_pattern = re.compile(
    "["
    u"\U0001F600-\U0001F64F"  # emoticons
    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
    u"\U0001F680-\U0001F6FF"  # transport & map symbols
    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
    u"\U00002702-\U000027B0"  # dingbats
    u"\U000024C2-\U0001F251"  # enclosed characters
    "]+", flags=re.UNICODE)

def remove_emojis(text):
    return emoji_pattern.sub(r'', text)


# Function to calculate repetition score based on multiple characters
def calculate_repetition_score(message):
    total_length = len(message)
    char_counts = Counter(message)

    # Set a threshold for how many times a character must appear to count as repeated
    repetition_threshold = max(2, total_length % 5) #2

    # Sum the counts of all characters that appear more than the threshold
    repeated_char_sum = sum(
        count for char, count in char_counts.items() if count >= repetition_threshold)

    # Calculate repetition score as proportion of repeated characters
    if total_length > 0:
        repetition_score = repeated_char_sum / total_length
    else:
        repetition_score = 0  # Edge case: if message is empty

    return repetition_score

names = get_all_first_and_last_names()

# Function to score based on keyboard mashing likelihood
def keyboard_mashing_probability(message):
    message = remove_emojis(message)
    message = message.lower()
    total_length = len(message)

    if total_length <=1:
        return 0



    # Score 1: repetition of characters
    repetition_score = calculate_repetition_score(message)

    # Score 2: Proportion of non-alphabetical characters
    non_alphabet_count = sum(1 for char in message if char not in string.ascii_letters)
    non_alphabetic_score = non_alphabet_count / total_length

    # Score 3: Meaningfulness of words
    words_in_message = message.split()
    meaningful_word_count = sum(1 for word in words_in_message if word in word_list)
    meaningful_word_count += sum(1 for word in words_in_message if word in names)
    if len(words_in_message) > 0:
        meaningfulness_score = 1 - (meaningful_word_count / len(words_in_message))
    else:
        meaningfulness_score = 1  # No valid words at all, so full score

    # Score 4: Letter frequency analysis
    letter_counts = Counter(char.lower() for char in message if char.isalpha())
    if total_length > 0:
        unique_char_score = len(letter_counts) / total_length
    else:
        unique_char_score = 1  # Highly suspicious if no characters at all

    # check if there is a meaningful word, decrease the meaningfulness score
    if meaningful_word_count >= 1:
        meaningfulness_score /= len(words_in_message)

    # Combine scores into an overall score (between 0 and 1)
    # Assign weights to different scores, adjust as needed
    total_score = (0.35 * repetition_score +
                   0.05 * non_alphabetic_score +
                   0.55 * meaningfulness_score +
                   0.05 * unique_char_score)
    return round(total_score,2)



