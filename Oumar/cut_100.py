import os

my_file = r'C:\Users\surface\Desktop\YouWe\OCR\Oumar\Extracted Data\Voucher_IDs_Full.txt'
sorting = True
hold_lines = []
SAVEPATH = r'C:\Users\surface\Desktop\YouWe\OCR\Oumar\Extracted Data'
lines = 100
with open(my_file,'r') as text_file:
    for row in text_file:
        hold_lines.append(row)
outer_count = 1
line_count = 0
os.chdir(SAVEPATH)
while sorting:
    count = 0
    increment = (outer_count-1) * lines
    left = len(hold_lines) - increment
    file_name = "Voucher_IDs" + str(outer_count * lines) + ".txt"
    hold_new_lines = []
    if left < lines:
        while count < left:
            hold_new_lines.append(hold_lines[line_count])
            count += 1
            line_count += 1
        sorting = False
    else:
        while count < lines:
            hold_new_lines.append(hold_lines[line_count])
            count += 1
            line_count += 1
    outer_count += 1
    with open(file_name,'w') as next_file:
        for row in hold_new_lines:
            next_file.write(row)