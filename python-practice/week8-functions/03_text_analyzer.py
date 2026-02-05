# Week 8: Mini Project - Text Analyzer
# Run: python3 week8-functions/03_text_analyzer.py

def count_characters(text):
    return len(text)

def count_words(text):
    return len(text.split())

def count_sentences(text):
    count = text.count('.') + text.count('!') + text.count('?')
    return count

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def count_consonants(text):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return sum(1 for char in text if char in consonants)

def most_common_word(text):
    words = text.lower().split()
    if not words:
        return None
    
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    max_count = 0
    common_word = ""
    for word, count in word_count.items():
        if count > max_count:
            max_count = count
            common_word = word
    
    return common_word, max_count

def analyze_text(text):
    print("Text Analysis")
    print("=" * 40)
    print(f"Characters: {count_characters(text)}")
    print(f"Words: {count_words(text)}")
    print(f"Sentences: {count_sentences(text)}")
    print(f"Vowels: {count_vowels(text)}")
    print(f"Consonants: {count_consonants(text)}")
    
    word, count = most_common_word(text)
    print(f"Most common word: '{word}' (appears {count} times)")

# Test the analyzer
sample_text = input("Enter text to analyze: ")
analyze_text(sample_text)

# TODO: Add a function to find the longest word
# TODO: Add a function to calculate average word length
# TODO: Add a function to count specific punctuation marks
