import os
text = raw_input()

url_index = text.index("http")
end_index = text.index(".com")
beginning = text[:url_index]
ending = text[end_index + 5:]
text = beginning + ending
print(text)