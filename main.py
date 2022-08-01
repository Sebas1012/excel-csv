from openpyxl import load_workbook

def excel_csv(book_path, sheet_name, separator):
    book = load_workbook(str(book_path))
    sheet = book[str(sheet_name)]

    for row in sheet.iter_rows(min_row=1,values_only=True):
        print(str(row))


excel_csv('./docs/prueba.xlsx', 'MCA195MOCA20200930NI0080005', '|')