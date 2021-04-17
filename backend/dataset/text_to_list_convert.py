items={}
with open("tickers_financial.txt", "r") as filestream:
    with open("ticker_output.txt", "w") as filestreamtwo:
        for line in filestream:
            currentline = line.split(",")
            total = '"' + currentline[0] + '" : ' + '[' + '"' + str(currentline[1]) + '"' + "," + '"' + str(currentline[2].rstrip()) + '",' + currentline[3] + ", " + currentline[4] + ", " + currentline[5] + ", " + currentline[6] + ", " + currentline[7] + ',' + currentline[4] + ", " + currentline[5] + ", " + currentline[6] + '],' + '\n'
            filestreamtwo.write(total)