def counting_chars_without_ifs(filename):
    file_ref = open(filename, 'r')
    text = file_ref.read().lower()
    char_count = {char: text.count(char) for char in set(list(text))}
    file_ref.close()
    try:
        del char_count[" "]
    except:
        pass
    try:
        del char_count["\n"]
    except:
        pass
    return char_count
