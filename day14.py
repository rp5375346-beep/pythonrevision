from email.mime import text


def analyze_text(text):
    text=input("Enter a text: ")
    cleaned_text = text.lower().strip()
    for char in cleaned_text:
        if char.isalnum() or char == " ":
            cleaned_text += char
    return cleaned_text
word_count={}
for word in word_count:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
        most_frequent_word=""
        max_count=0
        for word, count in word_count.items():
                if count > max_count:
                    max_count = count
                    most_frequent_word = word
                    result={
                        'total_words': len(word_count),
                        'most_frequent_word': most_frequent_word,
                    }
                    
                print(analyze_text)
                # task2
                def filter_words(text, min_length, min_count):
                    words = text.split()
                    filtered_words = [word for word in words if len(word) >= min_length and words.count(word) >= min_count]
                    return filtered_words
                min_length = 4
                min_count = 2
                filtered_words = filter_words(text, min_length, min_count)
                print("Filtered words:", filtered_words)
                # task3
                username=input("Enter a username: ")
                email=input("Enter an email: ")
                password=input("Enter a password: ")
                if email=="@gmail.com" and len(password)>=8:
                    print("Valid credentials")