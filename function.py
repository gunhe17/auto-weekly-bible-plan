from pptx import Presentation
from pptx.util import Pt
import os
import json

initial_presentation = "./data/table_format.pptx"

start_book = ""
start_chapter = ""

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

    weekly_plan = []
    current_book = start_book
    current_chapter = int(start_chapter)
    
    for _ in range(7):
        daily_start_book = current_book
        daily_start_chapter = current_chapter
        
        for _ in range(daily_reading):
            if current_chapter <= bible_chapters[current_book]:
                if current_chapter == bible_chapters[current_book]:
                    books = list(bible_chapters.keys())
                    current_book_index = books.index(current_book)
                    if current_book_index + 1 < len(books):
                        current_book = books[current_book_index + 1]
                        current_chapter = 1
                else:
                    current_chapter += 1
            else:
                break

        abbreviated_start_book = shortest_names.get(daily_start_book, daily_start_book)
        abbreviated_current_book = shortest_names.get(current_book, current_book)
        
        if abbreviated_start_book == abbreviated_current_book:
            reading_range = f"{abbreviated_start_book} {daily_start_chapter}장 - {current_chapter - 1}장"
        else:
            reading_range = f"{abbreviated_start_book} {daily_start_chapter}장 - {abbreviated_current_book} {current_chapter - 1}장"

        weekly_plan.append(reading_range)
    
    return weekly_plan

def patch_cell(cell, text):
    cell.text = ""
    text_frame = cell.text_frame
    p = text_frame.add_paragraph()
    run = p.add_run()
    run.text = text

    run.font.name = "배달의민족 한나체 Pro"
    run.font.size = Pt(46)

def patch_part_data(
        *,
        date,
        weekly_plan,
        selected_custom,
):
    pptx = Presentation(f"./custom/{selected_custom}.pptx")
    day_mapping = {
        "part_sun": 0,
        "part_mon": 1,
        "part_tue": 2,
        "part_wed": 3,
        "part_thu": 4,
        "part_fri": 5,
        "part_sat": 6,
    }

    for slide in pptx.slides:
        for shape in slide.shapes:
            if shape.has_text_frame:
                if "part_date" in shape.text:
                    shape.text = shape.text.replace("part_date", date)

                for day_key, plan_index in day_mapping.items():
                    if day_key in shape.text:
                        shape.text = shape.text.replace(day_key, weekly_plan[plan_index])

    pptx.save("./patched_pptx.pptx")

    return
    


###############
#   main
###############

def main():

    start_book = os.getenv('START_BOOK')
    start_chapter = os.getenv('START_CHAPTER')
    date = os.getenv('DATE')
    selected_custom = os.getenv('SELECTED_CUSTOM')
    
    weekly_plan = get_weekly_plan(start_book=start_book, start_chapter=start_chapter)
    patch_part_data(date=date, weekly_plan=weekly_plan, selected_custom=selected_custom)

if __name__ == "__main__":
    main()