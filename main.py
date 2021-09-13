import json
import csv


with open('declarations.json') as f:
  data = json.load(f)

actions = []
data= data['Quin_doctors_Amsterdam']
for year in data:
  print(year)
  for quarter in data[year]:
      print(quarter)
      print(data[year][quarter])
      for key in data[year][quarter]:
        if isinstance(data[year][quarter][key], dict):
          for action_code in data[year][quarter][key]:
            print (action_code)
            print(data[year][quarter][key][action_code])
            quantity = data[year][quarter][key][action_code]
            month_str = key
            month_str = month_str.replace("month_", "")
            action = [action_code, quantity, year, "Q"+quarter,month_str]
            actions.append(action)
        else:
          print("not list")
          print(key)
          action_code = key
          print(data[year][quarter][key])
          quantity = data[year][quarter][key]
          action= [action_code,quantity,year,"Q"+quarter]
          actions.append(action)

cols = ['action_code','quantity','year', 'quarter', 'month']

with open('declarations.csv', 'w') as f:
  # using csv.writer method from CSV package
  write = csv.writer(f)

  write.writerow(cols)
  write.writerows(actions)

