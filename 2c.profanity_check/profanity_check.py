import urllib


def read_text():
    # open - Python Built-in Function
    # https://docs.python.org/2/library/functions.html#open
    quotes = open("/Users/euijin/dev/python/Programming Fundations with Python/2c.profanity_check/movie_quotes.txt")
    contents_of_files = quotes.read()
    print(contents_of_files)
    quotes.close()
    check_profanity(contents_of_files)


def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    output = connection.read()
    print(output)
    connection.close()


read_text()
