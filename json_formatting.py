import json

with open ("input_file.json") as f:
  data = json.load(f)

print(data["job_name"])
for key in (data["test1"]["stages"]):
  print key['Inventory']['url']
