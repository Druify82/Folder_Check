# 01/12/2023 Second steps developed by ChatGPT
# Programm: Ordner-Dateizähler
# Quelle: ChatGPT, OpenAI
# Verfasser: ChatGPT
# Jahr der Veröffentlichung: 2023

import os
from pathlib import Path
import readline

def complete(text, state):
	return (glob.glob(text+'*')+[None])[state]

def count_files_in_directory(directory):
	file_count = {}
	for root, dirs, files in os.walk(directory):
		file_count[root] = len(files)	
	return file_count

def main():
	readline.set_completer_delims(' \t\n=')
	readline.parse_and_bind("tab: complete")
	readline.set_completer(complete)

	path_input = input("Enter directory path (leave empty for current directory): ")
	directory = path_input or "."

	file_counts = count_files_in_directory(directory)
	sorted_counts = sorted(file_counts.items(), key=lambda x: x[1], reverse=True)

	print("\nTop 10 folders with the most files:")
	for i, (path, count) in enumerate(sorted_counts[:10]):
		print(f"{i+1}: {path} - {count} files")

	show_all = input("\nShow all folders? (y/n): ").lower()
	if show_all == 'y':
		for path, count in sorted_counts:
			print(f"{path} - {count} files")

if __name__ == "__main__":
	main()
