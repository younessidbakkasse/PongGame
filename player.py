import re 

text = "iejfiefjfijfeifjei 737-882-1012 and 267-878-1883"
numberFormat = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
res = numberFormat.search(text)
if res == None:
    print("The sample deosn't contain any numbers")
else: 
    print("the phone number is : " + res.group() + ".")