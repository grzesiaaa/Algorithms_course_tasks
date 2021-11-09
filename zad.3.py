def counting_chars_without_ifs(filename):
  file_ref = open(filename, 'r')
  text = file_ref.read().lower()
  char_count = {char: text.count(char) for char in set(list(text))}
  try:
    del char_count[" "]
    del char_count["\n"]
  except:
    pass
  return char_count


print(counting_chars_without_ifs("L3_ZAD3_sample_text.txt"))
