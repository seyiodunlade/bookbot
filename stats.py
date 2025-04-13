def sort_dict(dict):
    return dict["count"]

def print_result(num_words, sorted_list):

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
        
    for char_count in sorted_list:
        print(f"{char_count["char"]}: {char_count["count"]}")

    print("============= END ===============")

def get_num_words(filepath):
    result = {}
    sorted_lst = []
    num_words = 0
    with open(filepath) as file:
        file_contents = file.read()
        num_words += len(file_contents.split())
        for char in file_contents:
            if char.lower() in result:
                result[char.lower()] += 1
            else:
                result[char.lower()] = 1

        sorted_lst = [ {"char": key, "count": value} for key,value in result.items() ]
        sorted_lst.sort(reverse=True, key=sort_dict)

    print_result(num_words, sorted_lst) 
    

