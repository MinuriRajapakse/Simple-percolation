# Create a function 
def createTextFile(grid,text_file_name1,dimension):
    "This function will create a text file including the grid created by the main program"
    Text_fo = 0
    Text_fo = open(str(text_file_name1)+" ("+str(dimension)+").txt","w") # To get separate text files
    grid.border=False
    Text_fo.write(str(grid))
    Text_fo.close()

# Create a function
def createHtmlFile(text_file_name1,dimension,num,main_list,last_row):
    "This function will create a HTML file including the grid created by the main program"
    html_fo = 0
    html_fo = open(str(text_file_name1)+" ("+str(dimension)+").html","w")
    html_fo.write("""<html><head><body><table border="1" width="300" height="100">""")
    for a in range(0,num):
        html_fo.write("""<tr align="center">""")
        sub_value = [value[a] for value in main_list]
        for x in sub_value:
            html_fo.write("<td>"+str(x)+"</td>")
            continue
        html_fo.write("</tr>")

    html_fo.write("""<tr align="center" bgcolor="yellow">""")
    for b in last_row:
        html_fo.write("<td><b>"+str(b)+"</b></td>")
        continue
    html_fo.write("</tr></table></body></head></html>")
    html_fo.close()
