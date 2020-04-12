import random
import string


def display_chapter(file_names):
    for file_name in file_names:
        with open(file_name) as f:
            chapter_content = ''

            for line in f:
                if '# Chapter' in line:
                    if not chapter_content:
                        chapter_content += line
                    else:
                        yield chapter_content
                        chapter_content = line
                else:
                    chapter_content += line
            yield chapter_content


def read_book(file_names):
    for x in display_chapter(file_names):
            print(x)
            val = ''
            while val != ' ':
                val = input('Press the spacebar to move to another chapter\n')

    print('No more chapters to show')

# read_book(['001.txt', '002.txt'])

##################################################################################


def generate_words(words_count):
    all_words = ''
    for i in range(words_count):
        word_length = random.randint(1, 10)
        all_words += ''.join(random.choice(string.printable) for i in range(word_length)) + ' '

    return all_words[:-1] + '\n'


def book_generator(chapters_count, chapter_length_range):  # 5 chapters x 100 words
    with open('new-book.txt', 'w') as f:
        written_chapters = 0

        while written_chapters < chapters_count:
            written_chapters += 1
            chapter_content = f'# Chapter {written_chapters}\n'
            chapter_content += generate_words(chapter_length_range) + '\n'
            f.write(chapter_content)


# book_generator(20000, 500)
read_book(['new-book.txt'])