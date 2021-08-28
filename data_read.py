import csv
import re
import requests
import os

with open("C:/Users/cengi/Desktop/send_data.csv", "r") as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Sütun isimleri: {", ".join(row)}')
            local_file = "C:/Users/cengi/Desktop/"+f'{", ".join(row)}'
            print(local_file)
            try:
                # Create target Directory
                os.mkdir(local_file)
                print("Directory ", local_file, " Created ")
            except FileExistsError:
                print("Directory ", local_file, " already exists")

            line_count += 1
            print()
        else:
            url=str({row[2]})
            print(url)
            #url_bosluklu= r'.[^ ]+'
            #download_link= re.findall(url_bosluklu, url).strip("( ) } ' ")
            download_link =url.strip(" { ( ) '}")
            print("link="+download_link)

            print(f'Dosya adi={row[0]}.jpg Adres='+download_link)
            save_file = local_file+"/"+f'{row[0]}.jpg'
            print(save_file)

            data = requests.get(download_link)
            with open(save_file, 'wb')as file:
                file.write(data.content)
            line_count += 1
    print()
    print(f'{line_count} satır işlendi')