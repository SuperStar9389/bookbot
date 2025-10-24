from stats import get_word_count, count_letters, organize_dict

def get_book_text(filepath):
	with open(filepath) as file:
		return file.read()

def main():
	book = get_book_text("books/frankenstein.txt")
	word_count = get_word_count(book)
	letter_count = organize_dict(count_letters(book))
	print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
	print(f"Found {word_count} total words")
	print("--------- Character Count -------")
	for i in letter_count:
		print(f"{i["char"]}: {i["num"]}")


main()