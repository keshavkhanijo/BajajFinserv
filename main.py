import json
from json2html import *




with open("data.json") as f:
    d = json.load (f)
    scanOutput = json2html.convert(json=d)
    htmlfiler = ("output.html")
    with open (htmlfiler,'w') as htmlfile:
        htmlfile.write(str(scanOutput))
        print("Json file is converted into html successfully....")
