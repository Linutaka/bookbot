def get_book_text(file_path):
    with open(file_path) as file:
        file_contents = file.read()
    return file_contents

def get_num_words(words):
    words_list = words.split()      # nimmt jedes wort einzeln und packt es in eine Liste
    return len(words_list)          # returnt die Anzahl der Worte in der Liste

def get_counting_characters(words):
    text_lower = words.lower()      # wandelt den Text in lower Case um
    character_dict = {}
    

    for character in text_lower:
        if character in character_dict:     
            character_dict[character] += 1      # wenn Key schon im Dict dann erhoehe die Value des Keys um 1
            
        else: 
            character_dict[character] = 1       # falls character nicht im Dictionary -> fuege es als 'Key' hinzu und setze 'Value' auf 1
    return character_dict

def sort_on(item):
    return item["num"]     
   
def chars_sort(count_dict):
    char_list = []
    for i, u in count_dict.items():
        #entry = {"char": i, "num": u}
        char_list.append({"char": i, "num": u})
    char_list.sort(reverse=True, key =sort_on)
    return char_list