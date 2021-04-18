import requests
import os
import time
headers = {
    'authority': 'api.nasdaq.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not\\"A\\\\Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Mobile Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'bm_mi=031BF403C5825E6CFE717C89A669651F~0iCDwjhiFM9Nx7uu8zB4jx4UqVAyPuvci2e+vvOgSsGHypTotLnYEqXtz8aNbp7vZDSz4ZPQLFCtWWm5mkYf8e23779uUSiD7dSwrTXEcXFdjpsuiSS+GhHBlSx4maa6KtE6R2/BVk72JQQC7ShqJEuhmn/cyl7AFaJVnI1TB12tP89hY5Hm0ZBxiXqkKzs9gxZBJhmLRpk9Xe4XLYhlDnS7yh0qqBiR566ozmoaX18VaQsHG9JhnEZwp8sE1tyg; recentlyViewedList=FB|Stocks,TSLA|Stocks,SPX|Index; bm_sv=DA130B94207F471CE906C04CE265CE96~+WzIO4cb3/mRwGny9PlJRuNYPLrU28B2d6/vTLEcraaJad3p9xaM5AI8tY/JRDLojmtgWt4cH1feKAj70bRrKorTlhg+HDknxfDEmg6FCaHFvtR6UMvNst52Mq6DCdE3L4OWemlRrZiuIrOw9WOJA1eBMeORaFcs3lbI106VSBE=; ak_bmsc=93AF947B58AA32D2A0336C5C534317DB17DF95848D51000039307B60CE856E02~pltHnMXnzhrQa621xAqmsQHO92qY3FMjxTABrfjtc/VXXR2IhPZ5DFNJ+dTWB4gkuPyFfJ9etMQUPQWxPm4yLu8CPeE30EVuneev/saZ993P761zBDn1MHwpH4teB8gCNutNoY2DLOLDBlx5CO7IikmoyYh5KSegc7fiv5JsrOC3HiBd0jrd8OTcWWyGQHa/zA4ejOXE/f9KgmxVaW1PWU18gu/ZgysKRkJh+e8jjUOk+g/hvjJVZZ3q+U8U6Xuo54U5z5PQclKbyAFv3Tb0aGZmwzM9Sf8bM+5PhAVBPydMlSNo9BLzs654vzGicvJLFk; NSC_W.OEBR.DPN.7070=ffffffffc3a08e3345525d5f4f58455e445a4a422dae',
}

params = (
    ('assetclass', 'stocks'),
    ('fromdate', '2015-03-17'),
    ('limit', '9999'),
    ('todate', '2021-04-17'),
)

tickers = open("nasdaq-tickers.csv")
lines = tickers.readlines()
count = 0
for line in lines:
    print(str(count) + " out of " + str(len(lines)))
    count += 1
    split_lines = line.split(",")
    cur_ticker = split_lines[0]
    file_name = cur_ticker + ".csv"
    file_path = os.path.join("nasdaq", file_name)

    if not os.path.exists(file_path):
        url = "https://api.nasdaq.com/api/quote/" + cur_ticker + '/historical'
        response = requests.get(url, headers=headers, params=params, allow_redirects=True)
        with open(file_path, 'wb') as outfile:
            outfile.write(response.content)
            time.sleep(0.5)
