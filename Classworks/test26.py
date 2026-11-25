import re

text = "Order 66 placed on 2026-10-27; order 7 shipped on 2026-10-29."

print(re.findall(r"order", text, re.IGNORECASE))
print(re.findall(r"order", text))



print(re.match(r"order", text, re.IGNORECASE))
print(re.match(r"order", text))

print(re.sub(r"\d{4}-\d{2}-\d{2}", "<DATE>", text))

print(re.split(r"[;,]\s", "a; b,c ,  d"))


print(bool(re.fullmatch(r"\d{6}", text)), bool(re.fullmatch(r"\d{6}", "5600291")))

print(bool(re.match(r"\d{6}", "560029")), bool(re.match(r"\d{6}", "5600291")))

for match in re.finditer(r"Order", text):
    print("Found:", match.group(), "at index:", match.span())
    
print(re.subn(r"\d{4}-\d{2}-\d{2}", "<DATE>", text))