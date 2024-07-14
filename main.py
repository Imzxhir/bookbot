def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()

    words = convert(file_contents)
    print(f"The book contains {len(words)} words.")

    char_count = count_characters(file_contents)
    print_report(char_count, len(words))


def convert(file_contents):
    words = file_contents.split()
    return words


def count_characters(text):
    text = text.lower()

    char_count = {}

    for char in text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    return char_count


def print_report(char_count, word_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    char_list = [{"char": char, "count": count} for char, count in char_count.items()]

    char_list.sort(key=lambda x: x["count"], reverse=True)

    for item in char_list:
        print(f"The '{item['char']}' character was found {item['count']} times")

    print("--- End report ---")


if __name__ == "__main__":
    main()
