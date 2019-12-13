import xlrd


file1 = open("a.txt","w+")

wb = xlrd.open_workbook("Distance.xlsx")
wb1 = xlrd.open_workbook("Time.xlsx")
sheet = wb.sheet_by_index(0)
sheet1 = wb1.sheet_by_index(0)
sheet.cell_value(0,0)
sheet1.cell_value(0,0)

print(sheet.nrows)
print(sheet1.nrows)
print(sheet.ncols)
print(sheet1.ncols)

print(sheet.cell_value(1,1))

start = 0

for i in range(0 ,(sheet.ncols)-2,1):
    for j in range(0,(sheet.ncols)-2,1):
        if(sheet.cell_value(i,j)!=0):
            print(i+1)
            print(j+1)
            print(sheet.cell_value(i,j))
            start=start+1
            file1.write("%d %d %d \n" % (i+1, j+1, sheet.cell_value(i,j)))
        print("#############################")
        print(start)
        print("#############################")
print(start)
