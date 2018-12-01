import os
import csv

budget_csv = os.path.join("..","..","RICEHOU201811DATA2","class-mw","03-Python","hw","Instructions","PyBank","Resources","budget_data.csv")
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    num_month = 0
    total_net = 0
    net_current = 0
    net_last = 0
    total_net_change = 0
    gre_inc_net = 0
    gre_dec_net = 0
    for row in csvreader:
        num_month += 1
        net_current = int(row[1])
        total_net += net_current
        if csvreader.line_num != 1:
            net_change = net_current - net_last
            total_net_change += net_change
            if net_change > gre_inc_net:
                gre_inc_net = net_change
                gre_inc_mon = row[0]
            if net_change < gre_dec_net:
                gre_dec_net = net_change
                gre_dec_mon = row[0]
        net_last = net_current
    ave_net_change = total_net_change/(num_month-1)
    print ("Financial Analysis")
    print ("----------------------------")
    print (f"Total Months: {num_month}")
    print (f"Total: ${total_net}")
    print (f"Average  Change: ${ave_net_change:.2f}")
    print (f"Greatest Increase in Profits: {gre_inc_mon} (${gre_inc_net})")
    print (f"Greatest Decrease in Profits: {gre_dec_mon} (${gre_dec_net})")

with open("budget_analysis.txt", 'w') as textfile:
    print ("Financial Analysis", file=textfile)
    print ("----------------------------", file=textfile)
    print (f"Total Months: {num_month}", file=textfile)
    print (f"Total: ${total_net}", file=textfile)
    print (f"Average  Change: ${ave_net_change:.2f}", file=textfile)
    print (f"Greatest Increase in Profits: {gre_inc_mon} (${gre_inc_net})",file=textfile)
    print (f"Greatest Decrease in Profits: {gre_dec_mon} (${gre_dec_net})",file=textfile)



