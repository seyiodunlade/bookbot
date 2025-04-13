import sys
from stats import get_num_words
def main():
    get_num_words(sys.argv[1])
if len(sys.argv) != 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)
else:    
    main()    