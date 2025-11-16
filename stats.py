def word_count(text):
    """
    @text: string: The books content to count
    @return: number: number of words in the text
    """
    count = len(text.split())
    return count

def character_count(text):
    """
    @text: string: The books content to count
    @return: dictionary: A dictionary of the number of times each character appears in the string    
    """
    result = {}
    words = text.lower().split()

    for word in words:
        for character in word:
            if character in result:
                result[character] += 1
            else:    
                result[character] = 1
    
    return result

def sorted_list(character_dict):
    """
   @character_dict: dictionary: dictionary of characters and counts
   @return: list: A list of sorted dictionaries 
    """
    result_list = []

    for key in character_dict:
        temp = {}
        temp["char"] = key
        temp["num"] = character_dict[key]
        result_list.append(temp)

    result_list.sort(reverse=True, key=sort_on)
    return result_list

def sort_on(items):
    return items["num"]