import sys
import re
import string


def count_words(l: list):
    count = {}
    for word in l:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count


def is_url(s: str):
    regex = re.compile(
        r'^(?:http|ftp)s?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, s)


def get_words(s: str) -> list:
    words = []
    split_spaces = s.split(" ")
    for elem in split_spaces:
        if is_url(elem):
            continue
        words.extend(re.sub(f"[{string.punctuation}]", ' ', elem).split())
    return words


def get_needle(s: str):
    words = get_words(s)
    counted_words = count_words(words)
    filtered = filter(lambda x: x[1] > 1, counted_words.items())
    sorted_words = sorted(filtered, key=lambda item: item[1], reverse=True)
    return map(lambda item: item[0], sorted_words)


def main():
    if len(sys.argv) >= 2:
        some_string = " ".join(sys.argv[1:])
        print(*get_needle(some_string))
    else:
        exit()


if __name__ == '__main__':
    main()
