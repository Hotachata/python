text = ["Tomorrow is gonna be a really nice day.", "Is it your birthday?", "I hope you have a great day!"]
# processed_text = text.strip(".").lower().split(" ")

def word_search (doc_list, keyword):
    processed_titles = []
    coincidences = []
    banned_signs = [".", ",", "!", "?", ";", ":"]
    for title in doc_list:
        if any(sign in title for sign in banned_signs):
            for sign in banned_signs:
                title = title.replace(sign, "")
        processed_titles.append(title.lower())
        
    for i in range(len(processed_titles)):
        title_words = processed_titles[i].split()
        if keyword in title_words:
            coincidences.append(i)
    return coincidences

# print(word_search(text, "day"))  # True

def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.  
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    processed_titles = []
    banned_signs = [".", ",", "!", "?", ";", ":"]
    for title in doc_list:
        if any(sign in title for sign in banned_signs):
            for sign in banned_signs:
                title = title.replace(sign, "")
        processed_titles.append(title.lower())


    coincidences = {keyword: [] for keyword in keywords}
    for i in range(len(processed_titles)):
        title_words = processed_titles[i].split()
        for keyword in keywords:
            if keyword in title_words:
                coincidences[keyword]+=[i]
    return coincidences

print(multi_word_search(["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"], ['casino', 'they', "dump"]))