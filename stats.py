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