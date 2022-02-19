"""Generate sales report showing total melons each salesperson sold."""

def sales_report(file):
    ''' Calculating how many melons did each salesperson sold and printing it out'''

    salespeople = [] #initiating empty lists to append data later
    melons_sold = []
    report_file = open(file)#open a file
    for line in report_file:#looping in the file by line
       line = line.rstrip()#striping the white space at the end of each line
       entries = line.split('|')#spliting the words in the lines by '|'

       salesperson = entries[0]#indexing where is the salesperson reference in the line
       melons = int(entries[2])#indixing the melons in the line

       if salesperson in salespeople:#looping through the empty list to check for salesperson extracted
           position = salesperson.index(salesperson)
           melons_sold[position] += melons #add all melons for same salesperson from different positions
       else:
          salespeople.append(salesperson)# if salesperson found once in the file add that person to the list
          melons_sold.append(melons) #if melons for salesperson found once append it to the list

    for i in range(len(salespeople)): # looping through the salespersons list to print the name and,
        print(f'{salespeople[i]} sold {melons_sold[i]} melons') #print how many melons each salesperson slod
    report_file.close()
sales_report("sales-report.txt")
#a way to improve the code:
#using functions to organize the code
#closing the file
