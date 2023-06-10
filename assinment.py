from bs4 import BeautifulSoup
import json

with open('TCPIP_ConsolidatedReport.html', 'r') as file:
    html = file.read()

soup = BeautifulSoup(html, 'html.parser')
tables = soup.find_all('table')
data = {}

first_table = tables[0]  # Get the first table

table_title = first_table.find('td').text.strip()
table_data = {}
rows = first_table.find_all('tr')
for row in rows:
    cells = row.find_all('td')

    if len(cells) == 2:
        key = cells[0].text.strip()
        value = cells[1].text.strip()
        table_data[key] = value

total_sloc = float(table_data.get('Total Number of SLOCs', 0))
cov_sloc = float(table_data.get('Number of SLOCs Covered In Unit Testing', 0))
par_sloc = float(table_data.get('Number of SLOCs Partially Covered In Unit Testing', 0))

percentage = ((par_sloc + cov_sloc) / total_sloc) * 100
table_data['Total Percentage Coverage (%)'] = percentage

data[table_title] = table_data

json_data = json.dumps(data, indent=4)

print(json_data)
