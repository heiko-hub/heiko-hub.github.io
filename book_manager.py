import tkinter
import datetime
import json

LABEL_FONT_STYLE = ("Cambria", 14, "bold")
LABEL_WIDTH = 14
LABEL_BOOK_ID_WIDTH = 5
LABEL_BOOK_TITLE_WIDTH = 30
LABEL_BOOK_AUTHOR_WIDTH = 20
LABEL_BOOK_YEAR_WIDTH = 5
LABEL_FUNCTION_WIDTH = 6
LABEL_BG = "black"
LABEL_FG = "white"
LABEL_PADX = 4
LABEL_PADY = 4

REPORT_EVEN_BG = "azure3"
REPORT_ODD_BG = "azure1"

BORROW_BOOKS_LIMIT = 10

ROW_HEADER = 0
ROW_BOOKS= 10
COLUMN_BOOK_ID = 0
COLUMN_DUE_DATE = 1
COLUMN_CALL_NUMBER = 2
COLUMN_BOOK_TITLE = 3
COLUMN_BOOK_AUTHOR = 4
COLUMN_BOOK_YEAR = 5
COLUMN_BOOK_RENEW = 6
COLUMN_BOOK_RETURN = 7

ROW_NEW_BORROW_DATE = ROW_HEADER + ROW_BOOKS + 2
ROW_NEW_CALL_NUMBER = ROW_NEW_BORROW_DATE + 1
ROW_NEW_BOOK_TITLE = ROW_NEW_BORROW_DATE + 2
ROW_NEW_BOOK_AUTHOR = ROW_NEW_BORROW_DATE + 3
ROW_NEW_BOOK_YEAR = ROW_NEW_BORROW_DATE + 4
COLUMN_NEW_LABEL = 2
COLUMN_NEW_ENTRY = 3

ENTRY_FONT_STYLE = ("Cambria", 14, "bold")
ENTRY_WIDTH = 30
ENTRY_PADX = 4
ENTRY_PADY = 4

ROW_BOOK_BORROW = ROW_NEW_BOOK_YEAR + 1
COLUMN_BOOK_BORROW = COLUMN_NEW_ENTRY

BUTTON_FONT_STYLE = ("Cambria", 14, "bold")
BUTTON_BG = "azure3"
BUTTON_PADX = 4
BUTTON_PADY = 4

FIRST_PADY = (20,4)

window = tkinter.Tk()
window.title("Book Manager")
window.config(padx=20, pady=20, bg="azure4")

BOOK_DATA_FILE = "book_data.json"
ID_DATA_FILE = "book_id.txt"

# ================ Borrow Books ========================================
def get_borrowed_books_count():
    borrowed_books = []
    with open(BOOK_DATA_FILE, "r") as data_file:
            data = json.load(data_file)
    for book_id, book_info in data.items():
        if book_info["status"] == "borrowed":
            borrowed_books.append({book_id: book_info})
    return len(borrowed_books)

def get_due_date():
    borrow_date_str = new_borrow_date_entry.get()
    b_year, b_month, b_day = borrow_date_str.split("-")
    borrow_date = datetime.datetime(
        year=int(b_year), month=int(b_month), day=int(b_day)
    )
    
    due_date = borrow_date + datetime.timedelta(days=14)
    d_year, d_month, d_day = due_date.year, due_date.month, due_date.day
    due_date_str = f"{d_year}-{d_month}-{d_day}"
    return due_date_str

def borrow_book():
    with open(ID_DATA_FILE, "r") as id_file:
        id = id_file.read().strip()
        
    try:
        due_date = get_due_date()
    except ValueError:
        print("Invalid Borrow Date")
    else:
        new_book = {
            id: {
                "due_date": due_date,
                "status": "borrowed",
                "call_number": new_call_number_entry.get(),
                "book_title": new_book_title_entry.get(),
                "book_author": new_book_author_entry.get(),
                "book_year": new_book_year_entry.get()
            }
        }
    
        with open(BOOK_DATA_FILE, "r") as data_file:
            data = json.load(data_file)
            
            borrowed_books_count = get_borrowed_books_count()
            if borrowed_books_count < BORROW_BOOKS_LIMIT:
                data.update(new_book)
    
                with open(BOOK_DATA_FILE, "w") as data_file:
                    json.dump(data, data_file, indent=4)

                with open(ID_DATA_FILE, "w") as id_file:
                    id_file.write(str(int(id)+1))

        new_borrow_date_entry.delete(0, tkinter.END)
        new_call_number_entry.delete(0, tkinter.END)
        new_book_title_entry.delete(0, tkinter.END)
        new_book_author_entry.delete(0, tkinter.END)
        new_book_year_entry.delete(0, tkinter.END)

    create_report()
 
# ================ Create Report =======================================
def create_report():
    for index in range(ROW_BOOKS):
        book_ids[index].config(text="")
        due_dates[index].config(text="")
        call_numbers[index].config(text="")
        book_titles[index].config(text="")
        book_authors[index].config(text="")
        book_years[index].config(text="")

    borrowed_books = []
    with open(BOOK_DATA_FILE, "r") as data_file:
            data = json.load(data_file)
    for book_id, book_info in data.items():
        if book_info["status"] == "borrowed":
            borrowed_books.append({book_id: book_info})
    print(borrowed_books)
    
    for index, book in enumerate(borrowed_books):
        for book_id in book.keys():
            book_ids[index].config(text=book_id)
        book_info = book[book_id]
        due_date = book_info["due_date"]
        call_number = book_info["call_number"]
        book_title = book_info["book_title"]
        book_author = book_info["book_author"]
        book_year = book_info["book_year"]
        due_dates[index].config(text=due_date)
        call_numbers[index].config(text=call_number)
        book_titles[index].config(text=book_title)
        book_authors[index].config(text=book_author)
        book_years[index].config(text=book_year)
 
# ================ Renew Books =========================================
def renew_book0():
    renew_book_id = book_ids[0].cget("text")
    print(f"Book 0 renewed (Book ID: {renew_book_id}).")
    renew_book(renew_book_id)

def renew_book1():
    renew_book_id = book_ids[1].cget("text")
    print(f"Book 1 renewed (Book ID: {book_ids[1].cget("text")}).")
    renew_book(renew_book_id)
    
def renew_book2():
    renew_book_id = book_ids[2].cget("text")
    print(f"Book 2 renewed (Book ID: {book_ids[2].cget("text")}).")
    renew_book(renew_book_id)
    
def renew_book3():
    renew_book_id = book_ids[3].cget("text")
    print(f"Book 3 renewed (Book ID: {book_ids[3].cget("text")}).")
    renew_book(renew_book_id)
    
def renew_book4():
    renew_book_id = book_ids[4].cget("text")
    print(f"Book 4 renewed (Book ID: {book_ids[4].cget("text")}).")
    renew_book(renew_book_id)
    
def renew_book5():
    renew_book_id = book_ids[5].cget("text")
    print(f"Book 5 renewed (Book ID: {book_ids[5].cget("text")}).")
    renew_book(renew_book_id)
    
def renew_book6():
    renew_book_id = book_ids[6].cget("text")
    print(f"Book 6 renewed (Book ID: {book_ids[6].cget("text")}).")
    renew_book(renew_book_id)
    
def renew_book7():
    renew_book_id = book_ids[7].cget("text")
    print(f"Book 7 renewed (Book ID: {book_ids[7].cget("text")}).")
    renew_book(renew_book_id)

def renew_book8():
    renew_book_id = book_ids[8].cget("text")
    print(f"Book 8 renewed (Book ID: {book_ids[8].cget("text")}).")
    renew_book(renew_book_id)

def renew_book9():
    renew_book_id = book_ids[9].cget("text")
    print(f"Book 9 renewed (Book ID: {book_ids[9].cget("text")}).")
    renew_book(renew_book_id)
    
renew_books = {
    0: renew_book0,
    1: renew_book1,
    2: renew_book2,
    3: renew_book3,
    4: renew_book4,
    5: renew_book5,
    6: renew_book6,
    7: renew_book7,
    8: renew_book8,
    9: renew_book9,
}

def get_new_due_date():
    today = datetime.date.today()
    due_date = today + datetime.timedelta(days=14)
    d_year, d_month, d_day = due_date.year, due_date.month, due_date.day
    due_date_str = f"{d_year}-{d_month}-{d_day}"
    return due_date_str

def renew_book(update_book_id):
    with open(BOOK_DATA_FILE, "r") as data_file:
        data = json.load(data_file)
        print(data)
        print(data[update_book_id])
        new_due_date = get_new_due_date()
        data[update_book_id]["due_date"] = new_due_date
    
    with open(BOOK_DATA_FILE, "w") as data_file:
        json.dump(data, data_file, indent=4)

    create_report()

# ================ Return Books ========================================
def return_book0():
    return_book_id = book_ids[0].cget("text")
    print(f"Book 0 returned (Book ID: {return_book_id}).")
    return_book(return_book_id)

def return_book1():
    return_book_id = book_ids[1].cget("text")
    print(f"Book 1 returned (Book ID: {return_book_id}).")
    return_book(return_book_id)

def return_book2():
    return_book_id = book_ids[2].cget("text")
    print(f"Book 2 returned (Book ID: {return_book_id}).")
    return_book(return_book_id)

def return_book3():
    return_book_id = book_ids[3].cget("text")
    print(f"Book 3 returned (Book ID: {return_book_id}).")
    return_book(return_book_id)

def return_book4():
    return_book_id = book_ids[4].cget("text")
    print(f"Book 4 returned (Book ID: {return_book_id}).")
    return_book(return_book_id)

def return_book5():
    return_book_id = book_ids[5].cget("text")
    print(f"Book 5 returned (Book ID: {return_book_id}).")
    return_book(return_book_id)

def return_book6():
    return_book_id = book_ids[6].cget("text")
    print(f"Book 6 returned (Book ID: {return_book_id}).")
    return_book(return_book_id)

def return_book7():
    return_book_id = book_ids[7].cget("text")
    print(f"Book 7 returned (Book ID: {return_book_id}).")
    return_book(return_book_id)

def return_book8():
    return_book_id = book_ids[8].cget("text")
    print(f"Book 8 returned (Book ID: {return_book_id}).")
    return_book(return_book_id)

def return_book9():
    return_book_id = book_ids[9].cget("text")
    print(f"Book 9 returned (Book ID: {return_book_id}).")
    return_book(return_book_id)
    
return_books = {
    0: return_book0,
    1: return_book1,
    2: return_book2,
    3: return_book3,
    4: return_book4,
    5: return_book5,
    6: return_book6,
    7: return_book7,
    8: return_book8,
    9: return_book9,
}

def return_book(update_book_id):
    with open(BOOK_DATA_FILE, "r") as data_file:
        data = json.load(data_file)
        print(data)
        print(data[update_book_id])
        data[update_book_id]["status"] = "returned"
    
    with open(BOOK_DATA_FILE, "w") as data_file:
        json.dump(data, data_file, indent=4)

    create_report()

# ================ Report Books Header Labels ==========================
report_book_id_label = tkinter.Label(
    text="ID", width=LABEL_BOOK_ID_WIDTH,
    font=LABEL_FONT_STYLE, bg=LABEL_BG, fg=LABEL_FG
)
report_book_id_label.grid(
    row=ROW_HEADER, column=COLUMN_BOOK_ID, 
    padx=LABEL_PADX, pady=LABEL_PADY
)

report_due_date_label = tkinter.Label(
    text="Due Date", width=LABEL_WIDTH,
    font=LABEL_FONT_STYLE, bg=LABEL_BG, fg=LABEL_FG
)
report_due_date_label.grid(
    row=ROW_HEADER, column=COLUMN_DUE_DATE, 
    padx=LABEL_PADX, pady=LABEL_PADY
)

report_call_number_label = tkinter.Label(
    text="Call Number", width=LABEL_WIDTH,
    font=LABEL_FONT_STYLE, bg=LABEL_BG, fg=LABEL_FG
)
report_call_number_label.grid(
    row=ROW_HEADER, column=COLUMN_CALL_NUMBER, 
    padx=LABEL_PADX, pady=LABEL_PADY
)

report_book_title_label = tkinter.Label(
    text="Book Title", width=LABEL_BOOK_TITLE_WIDTH,
    font=LABEL_FONT_STYLE, bg=LABEL_BG, fg=LABEL_FG
)
report_book_title_label.grid(
    row=ROW_HEADER, column=COLUMN_BOOK_TITLE, 
    padx=LABEL_PADX, pady=LABEL_PADY
)

report_book_author_label = tkinter.Label(
    text="Book Author", width=LABEL_BOOK_AUTHOR_WIDTH,
    font=LABEL_FONT_STYLE, bg=LABEL_BG, fg=LABEL_FG
)
report_book_author_label.grid(
    row=ROW_HEADER, column=COLUMN_BOOK_AUTHOR, 
    padx=LABEL_PADX, pady=LABEL_PADY
)

report_book_year_label = tkinter.Label(
    text="Year", width=LABEL_BOOK_YEAR_WIDTH,
    font=LABEL_FONT_STYLE, bg=LABEL_BG, fg=LABEL_FG
)
report_book_year_label.grid(
    row=ROW_HEADER, column=COLUMN_BOOK_YEAR, 
    padx=LABEL_PADX, pady=LABEL_PADY
)

report_renew_book_label = tkinter.Label(
    text="Renew", width=LABEL_FUNCTION_WIDTH,
    font=LABEL_FONT_STYLE, bg=LABEL_BG, fg=LABEL_FG
)
report_renew_book_label.grid(
    row=ROW_HEADER, column=COLUMN_BOOK_RENEW, 
    padx=LABEL_PADX, pady=LABEL_PADY
)

report_return_book_label = tkinter.Label(
    text="Return", width=LABEL_FUNCTION_WIDTH,
    font=LABEL_FONT_STYLE, bg=LABEL_BG, fg=LABEL_FG
)
report_return_book_label.grid(
    row=ROW_HEADER, column=COLUMN_BOOK_RETURN, 
    padx=LABEL_PADX, pady=LABEL_PADY
)

# ================ Report Books ID Labels ==============================
def get_bg_color(row_index):
    return REPORT_ODD_BG if row_index % 2 else REPORT_EVEN_BG

# ================ Report Books ID Labels ==============================
book_ids = []
for index in range(ROW_BOOKS):
    book_ids.append(tkinter.Label(
        width=LABEL_BOOK_ID_WIDTH, font=LABEL_FONT_STYLE, 
        bg=get_bg_color(index)
        )
    )
    book_ids[index].grid(
        row=ROW_HEADER+index+1, column=COLUMN_BOOK_ID,
        padx=LABEL_PADX, pady=LABEL_PADY
    )

# ================ Report Books Due Date Labels ========================
due_dates = []
for index in range(ROW_BOOKS):
    due_dates.append(tkinter.Label(
        width=LABEL_WIDTH, font=LABEL_FONT_STYLE, 
        bg=get_bg_color(index)
        )
    )
    due_dates[index].grid(
        row=ROW_HEADER+index+1, column=COLUMN_DUE_DATE,
        padx=LABEL_PADX, pady=LABEL_PADY
    )

# ================ Report Books Call Number Labels =====================
call_numbers = []
for index in range(ROW_BOOKS):
    call_numbers.append(tkinter.Label(
        width=LABEL_WIDTH, font=LABEL_FONT_STYLE, 
        bg=get_bg_color(index)
        )
    )
    call_numbers[index].grid(
        row=ROW_HEADER+index+1, column=COLUMN_CALL_NUMBER,
        padx=LABEL_PADX, pady=LABEL_PADY
    )

# ================ Report Books Book Title Labels ======================
book_titles = []
for index in range(ROW_BOOKS):
    book_titles.append(tkinter.Label(
        width=LABEL_BOOK_TITLE_WIDTH, font=LABEL_FONT_STYLE, 
        bg=get_bg_color(index)
        )
    )
    book_titles[index].grid(
        row=ROW_HEADER+index+1, column=COLUMN_BOOK_TITLE,
        padx=LABEL_PADX, pady=LABEL_PADY
    )

# ================ Report Books Book Author Labels =====================
book_authors = []
for index in range(ROW_BOOKS):
    book_authors.append(tkinter.Label(
        width=LABEL_BOOK_AUTHOR_WIDTH, font=LABEL_FONT_STYLE, 
        bg=get_bg_color(index)
        )
    )
    book_authors[index].grid(
        row=ROW_HEADER+index+1, column=COLUMN_BOOK_AUTHOR,
        padx=LABEL_PADX, pady=LABEL_PADY
    )

# ================ Report Books Book Year Labels =======================
book_years = []
for index in range(ROW_BOOKS):
    book_years.append(tkinter.Label(
        width=LABEL_BOOK_YEAR_WIDTH, font=LABEL_FONT_STYLE, 
        bg=get_bg_color(index)
        )
    )
    book_years[index].grid(
        row=ROW_HEADER+index+1, column=COLUMN_BOOK_YEAR,
        padx=LABEL_PADX, pady=LABEL_PADY
    )

# ================ Renew Book Buttons ==================================
renew_buttons = []
for index in range(ROW_BOOKS):
    renew_command = renew_books[index]
    renew_buttons.append(tkinter.Button(
        text="Renew", highlightthickness=0, 
        font=BUTTON_FONT_STYLE, bg=BUTTON_BG,
        command=renew_command
        )
    )
    renew_buttons[index].grid(
        row=ROW_HEADER+index+1, column=COLUMN_BOOK_RENEW,
        padx=LABEL_PADX, pady=LABEL_PADY
    )

# ================ Return Book Buttons =================================
return_buttons = []
for index in range(ROW_BOOKS):
    return_command = return_books[index]
    return_buttons.append(tkinter.Button(
        text="Return", highlightthickness=0, 
        font=BUTTON_FONT_STYLE, bg=BUTTON_BG,
        command=return_command
        )
    )
    return_buttons[index].grid(
        row=ROW_HEADER+index+1, column=COLUMN_BOOK_RETURN,
        padx=LABEL_PADX, pady=LABEL_PADY
    )

# ================ New Books Labels ====================================
new_borrow_date_label = tkinter.Label(
    text="Borrow Date:", width=LABEL_WIDTH,
    font=LABEL_FONT_STYLE, bg=LABEL_BG, fg=LABEL_FG
)
new_borrow_date_label.grid(
    row=ROW_NEW_BORROW_DATE, column=COLUMN_NEW_LABEL, 
    padx=LABEL_PADX, pady=FIRST_PADY
)

new_call_number_label = tkinter.Label(
    text="Call Number:", width=LABEL_WIDTH,
    font=LABEL_FONT_STYLE, bg=LABEL_BG, fg=LABEL_FG
)
new_call_number_label.grid(
    row=ROW_NEW_CALL_NUMBER, column=COLUMN_NEW_LABEL, 
    padx=LABEL_PADX, pady=LABEL_PADY
)

new_book_title_label = tkinter.Label(
    text="Book Title:", width=LABEL_WIDTH,
    font=LABEL_FONT_STYLE, bg=LABEL_BG, fg=LABEL_FG
)
new_book_title_label.grid(
    row=ROW_NEW_BOOK_TITLE, column=COLUMN_NEW_LABEL, 
    padx=LABEL_PADX, pady=LABEL_PADY
)

new_book_author_label = tkinter.Label(
    text="Book Author:", width=LABEL_WIDTH,
    font=LABEL_FONT_STYLE, bg=LABEL_BG, fg=LABEL_FG
)
new_book_author_label.grid(
    row=ROW_NEW_BOOK_AUTHOR, column=COLUMN_NEW_LABEL, 
    padx=LABEL_PADX, pady=LABEL_PADY
)

new_book_year_label = tkinter.Label(
    text="Year:", width=LABEL_WIDTH,
    font=LABEL_FONT_STYLE, bg=LABEL_BG, fg=LABEL_FG
)
new_book_year_label.grid(
    row=ROW_NEW_BOOK_YEAR, column=COLUMN_NEW_LABEL, 
    padx=LABEL_PADX, pady=LABEL_PADY
)
# ================ New Books Entries ===================================
new_borrow_date_entry = tkinter.Entry(
   width=ENTRY_WIDTH, font=ENTRY_FONT_STYLE
)
new_borrow_date_entry.grid(
    row=ROW_NEW_BORROW_DATE, column=COLUMN_NEW_ENTRY, 
    padx=ENTRY_PADX, pady=FIRST_PADY
)
new_borrow_date_entry.focus()

new_call_number_entry = tkinter.Entry(
   width=ENTRY_WIDTH, font=ENTRY_FONT_STYLE
)
new_call_number_entry.grid(
    row=ROW_NEW_CALL_NUMBER, column=COLUMN_NEW_ENTRY, 
    padx=ENTRY_PADX, pady=ENTRY_PADY
)

new_book_title_entry = tkinter.Entry(
   width=ENTRY_WIDTH, font=ENTRY_FONT_STYLE
)
new_book_title_entry.grid(
    row=ROW_NEW_BOOK_TITLE, column=COLUMN_NEW_ENTRY, 
    padx=ENTRY_PADX, pady=ENTRY_PADY
)

new_book_author_entry = tkinter.Entry(
   width=ENTRY_WIDTH, font=ENTRY_FONT_STYLE
)
new_book_author_entry.grid(
    row=ROW_NEW_BOOK_AUTHOR, column=COLUMN_NEW_ENTRY, 
    padx=ENTRY_PADX, pady=ENTRY_PADY
)

new_book_year_entry = tkinter.Entry(
   width=ENTRY_WIDTH, font=ENTRY_FONT_STYLE
)
new_book_year_entry.grid(
    row=ROW_NEW_BOOK_YEAR, column=COLUMN_NEW_ENTRY, 
    padx=ENTRY_PADX, pady=ENTRY_PADY
)

borrow_book_button = tkinter.Button( 
    text="Borrow", highlightthickness=0, 
    font=BUTTON_FONT_STYLE, bg=BUTTON_BG,
    command=borrow_book)
borrow_book_button.grid(
    row=ROW_BOOK_BORROW, column=COLUMN_BOOK_BORROW, 
    padx=BUTTON_PADX, pady=BUTTON_PADY
)

create_report()
window.mainloop()
