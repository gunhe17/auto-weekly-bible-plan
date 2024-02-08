import json

backgroud_image = "./data/background_img/img_no{n}"
initial_presentation = "./data/table_format.pptx"

start_book = ""
start_chapter = ""

import json

def get_weekly_plan(
        *, 
        start_book, 
        start_chapter, 
        daily_reading=3, 
        bible_index="./data/bible_index.json", 
        bible_shortest_names="./data/bible_shortest_name.json"
    ):

    with open(bible_index, 'r') as file:
        bible_chapters = json.load(file)
    
    with open(bible_shortest_names, 'r') as file:
        shortest_names = json.load(file)

    reading_list = []
    current_book = start_book
    current_chapter = int(start_chapter)
    
    for day in range(7):
        daily_start_book = current_book
        daily_start_chapter = current_chapter
        
        for _ in range(daily_reading):
            if current_chapter < bible_chapters[current_book]:
                current_chapter += 1
            else: 
                books = list(bible_chapters.keys())
                current_book_index = books.index(current_book)
                if current_book_index + 1 < len(books):
                    current_book = books[current_book_index + 1]
                    current_chapter = 1
                else:
                    break

        abbreviated_start_book = shortest_names.get(daily_start_book, daily_start_book)
        abbreviated_current_book = shortest_names.get(current_book, current_book)
        
        if abbreviated_start_book == abbreviated_current_book:
            abbreviated_current_book = ""
        
        reading_range = f"{abbreviated_start_book} {daily_start_chapter} - {abbreviated_current_book} {current_chapter - 1 if current_chapter > 1 else bible_chapters[daily_start_book]}"
        reading_list.append(reading_range)
    
    return reading_list


weekly_reading = get_weekly_plan(start_book="에스더", start_chapter="1")
print(weekly_reading)