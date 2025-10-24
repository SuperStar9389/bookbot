from stats import get_word_count, count_letters, organize_dict
import sys

def get_book_text(filepath):
	with open(filepath) as file:
		return file.read()

def main(book_path):
	book = get_book_text(book_path)
	word_count = get_word_count(book)
	letter_count = organize_dict(count_letters(book))
	print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
	print(f"Found {word_count} total words")
	print("--------- Character Count -------")
	for i in letter_count:
		print(f"{i["char"]}: {i["num"]}")

if len(sys.argv) <= 1:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)
main(sys.argv[1])