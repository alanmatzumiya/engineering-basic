import os
import requests
import json

modules = os.listdir("./")
modules.remove("README.md")
modules.remove(".git")
modules.remove("get_data.py")
if "notebooks_data.json" in modules:
    modules.remove("notebooks_data.json")
url_app = "https://jupyternbs.herokuapp.com/notebooks/engineering-basic"
url_github = "https://raw.githubusercontent.com/alanmatzumiya/engineering-basic/main"
data = {}

for module in modules:
    notebooks = os.listdir(module)
    notebooks.sort()
    data[module] = []
    for notebook in notebooks:
        if notebook.endswith(".ipynb"):
            data[module].append({"name": notebook,
                                 "url_app": f"{url_app}/{module}/{requests.utils.quote(notebook)}",
                                 "url_github": f"{url_github}/{module}/{requests.utils.quote(notebook)}"})                

with open("notebooks_data.json", "w") as outfile:
    json_file = json.dumps(data, indent=4, sort_keys=True)
    outfile.write(json_file)
    outfile.close()
