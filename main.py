def get_book_text(filepath):
	with open(filepath) as file:
		return file.read()

def get_word_count(text):
	return len(text.split())


def main():
	book = get_book_text("books/frankenstein.txt")
	word_count = get_word_count(book)
	print(f"Found {word_count} total words")


main()