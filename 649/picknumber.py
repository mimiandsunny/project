import xlrd
wb = xlrd.open_workbook(filename = 'digits.xlsx')
number_stats= {}
for i in range(1,wb.nsheets):
    sheet_value=wb.get_sheets(i)
    j=0
    while True:
        try:
           j_row = sheet_value.row_values(j)
        except:
           break
        else:
            j+1
            for i in  range(1,7):
                cell_value=j_row[i]
                if cell_value not in number_stats.keys():
                    number_stats.update({cell_value:1})
                else:
                    number_stats[cell_value]=+1
print(number_stats)

