import xlrd
wb = xlrd.open_workbook(filename = 'digits.xlsx')
number_stats= {}

sheet_value=wb.sheet_by_index(0)
j=0
print(sheet_value.row_values(j) )
while True:
     try:
         j_row = sheet_value.row_values(j)
     except IndexError:
          break
     else:
         j=j+1
         for i in  range(1,7):
              cell_value=j_row[i]
              if cell_value not in number_stats.keys():
                   number_stats.update({cell_value:1})
              else:
                   number_stats[cell_value]=number_stats[cell_value]+1
print(number_stats)
print(sorted(number_stats.items(), key=lambda x:x[1]))

