import sys
from prettytable import PrettyTable, ALL
import subprograms
import Sub.TxtHtml

# Create variables
text1_fo = 0
text1_num = 0
dimension = ""
data = []
count = 1
last_row = []
main_list = []

# Assign values to variables to create a prettytable
perc_table = PrettyTable(border=True, header=False, padding_width=1)
perc_table.hrules = ALL

# Update the "NoOfResults" text file to create new text files for each result
text1_fo = open("NoOfResults.txt", "r")
text1_data = text1_fo.read()
text1_fo = open("NoOfResults.txt", "w")
text1_num = int(text1_data) + 1
text1_fo.write(str(text1_num))
text1_fo.close()

# Create simple percolation process
if len(sys.argv) != 2:  # When the user does not mention the dimensions
    for i in range(0, 5 * 5):
        data.append(subprograms.createRandomNums())
        main_list = subprograms.createSubLists(data, 5)
    for digit in main_list:
        perc_table.add_column(str(count), digit)
        count += 1
        if " " in digit:
            last_row.append("NO")
            continue
        else:
            last_row.append("OK")
            continue
    perc_table.add_row(last_row)
    print(perc_table)

    dimension = "5x5"  # Part of the text file name

    # Create HTML file for each result
    Sub.TxtHtml.createHtmlFile(text1_data, dimension, 5, main_list, last_row)  # Calling the "createHtmlFile" function


elif len(sys.argv) == 2:  # When the user mentions the dimensions
    console_num = sys.argv[1]
    console_list = list(console_num)
    start_console = int(console_list[0])
    mid_console = str(console_list[1])
    end_console = console_list[2]

    if (len(console_list) == 3) and (start_console >= 3) and (int(end_console) <= 9) and (
            mid_console == "x" or mid_console == "X"):
        for i in range(0, start_console * int(end_console)):
            data.append(subprograms.createRandomNums())
            main_list = subprograms.createSubLists(data, start_console)
        for digit in main_list:
            perc_table.add_column(str(count), digit)
            count += 1
            if " " in digit:
                last_row.append("NO")
                continue
            else:
                last_row.append("OK")
                continue
        perc_table.add_row(last_row)
        print(perc_table)

    # Display an error message when the user input does not satisfy the above "IF" condition
    elif ((len(console_list) != 3) or (len(console_list) == "") or (start_console < 3) or (int(end_console) > 9) or (
            mid_console != "x") or (mid_console != "X")):
        print("\n")
        print("*** 3x3 is the lowest dimension and 9x9 is the highest dimension ***")
        print("\n")

    dimension = str(console_num)  # Part of the text file name

    # Create HTML file for each result
    Sub.TxtHtml.createHtmlFile(text1_data, dimension, start_console, main_list,
                               last_row)  # Calling the "createHtmlFile" function

# Create text file for each result
Sub.TxtHtml.createTextFile(perc_table, text1_data, dimension)  # Calling the "createTextFile" function
