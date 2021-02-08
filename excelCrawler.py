import openpyxl
from crawling_images_camping import crawling

excel_document = openpyxl.load_workbook('data.xlsx')
sheet = excel_document["sheet1"]
all_rows = sheet.rows
for row in all_rows:
    # print(row[8].value)
    # 8번이 i임을 잊지말자
    if row[8].value == "자동차야영장":
        name = row[7].value
        print(name)
        print("im here")
        crawling.search(name)
        # 위도
        # write_ws.append([region, city, name, road_add, loc_add, dim, facility, '0', ])
# write_wb.save('refined.xlsx')
