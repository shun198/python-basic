import re
# Regular expression (正規表現)

email = "myemail@gmail.com"
matched = re.search("@\w+\.", email)
print(matched)
