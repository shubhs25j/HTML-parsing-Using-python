from bs4 import BeautifulSoup
import json

with open('TCPIP_ConsolidatedReport.html', 'r') as file:
    html = file.read()
soup = BeautifulSoup(html, 'html.parser')
tables = soup.find_all('table')
data = {}

first_table = tables[0]  

rows = first_table.find_all('tr')
for row in rows:
    cells = row.find_all('td')

    if len(cells) == 2:
        key = cells[0].text.strip()
        value = cells[1].text.strip()
        data[key] = value
        if key=="Total Number of SLOCs":
            total_sloc=float(value)
        elif key=="Number of SLOCs Covered In Unit Testing":
            cov_sloc=float(value)
        elif key=="Number of SLOCs Partially Covered In Unit Testing":
            par_sloc=float(value)
        
persentage=((par_sloc+cov_sloc)/total_sloc)*100
# print(persentage)
data['Total Percentage Coverage (%)'] = persentage
save_file = open("data.json", "w")  
json.dump(data,save_file,indent=4)
save_file.close()
json_data = json.dumps(data,indent=4)
print(json_data)
