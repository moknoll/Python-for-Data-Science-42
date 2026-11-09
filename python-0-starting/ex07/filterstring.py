import sys

def filter_words():
    """Function to filter words that are longer then the second input"""
    try:
        assert len(sys.argv) == 3

        text = sys.argv[1]
        n = int(sys.argv[2])

        words = [word for word in text.split()]

        result = list(filter(lambda word: len(word) > n, words))

        print(result)

    except (AssertionError, ValueError):
        print("AssertionError: The arguments are bad")


def main():
    filter_words()


if __name__ == "__main__":
    main()