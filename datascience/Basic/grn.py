myDict = {"roll no":["01,02,03,04,05"],
"name":["ram","om","kumar","abid","abdul"],
"subject":["Bcom,BE, Mca,Msc,Mcom "],
"Marks":[87,96,89,91,90],
"Marks":[92,99,88,71,97]
}
del myDict["subject"]
print(myDict)

myDict.pop("name")
print(myDict)

print(myDict["Marks"])

myDict.clear()
print(myDict)

