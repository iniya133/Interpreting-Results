import csv
import plotly.express as px

rows = []

with open("stars.csv", "r") as f:
  csvreader = csv.reader(f)
  for row in csvreader: 
    rows.append(row)

headers = rows[0]
star_data_rows = rows[1:]

star_names = []
star_masses = []
star_radiuses = []
star_distances = []
star_gravities = []

for star_data in star_data_rows:
    star_names.append(star_data[1])
    star_masses.append(star_data[3])
    star_radiuses.append(star_data[4])
    star_distances.append(star_data[2])
    star_gravities.append(star_data[5])

fig1 = px.bar(x = star_names, y = star_masses)
fig1.show()
fig2 = px.bar(x = star_names, y = star_radiuses)
fig2.show()
fig3 = px.bar(x = star_names, y = star_distances)
fig3.show()
fig4 = px.bar(x = star_names, y = star_gravities)
fig4.show()
