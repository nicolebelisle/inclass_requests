import requests

# r = requests.get("https://api.github.com/repos/dward2/BME547/branches")
# print(type(r))
# print(r)
# print(r.text)
# print("")
# answer = r.json()
# print(type(answer))
# print(answer)
# for branch in answer:
#     print("Name of branch is {}".format(branch["name"]))

# r = requests.get("https://api.github.com/BME547_Class/nicolebelisle/blood_analysis/branches")
# print(type(r))
# print(r)
# print(r.text)
# print("")
# answer = r.json()
# print(type(answer))
# print(answer)
# for branch in answer:
#     print("Name of branch is {}".format(branch["name"]))

r = requests.get("https://vcm-7631.vm.duke.edu:5000/regions")
print(r.json)

# request_json = {"one": "Spain", "two": "Canada"}
# r = requests.post("http://vcm-7631.vm.duke.edu:5000/compare", json=request_json)
# print(r)
# print(r.status_code)
# print(r.text)
# if r.status_code == 200:
#     print(r.json)
# else:
#     print("There was an error with status code of {}".format(r.status_code)
