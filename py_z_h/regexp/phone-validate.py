import re

def extract_phone(inp):
    phone_reg = re.compile(r'\b\d{3} \d{3}-?\d{4}\b')
    match = phone_reg.search(inp)
    if match:
        return match.group()

def extract_all_phones(inp):
    phone_reg = re.compile(r'\b\d{3} \d{3}-?\d{4}\b')
    matches = phone_reg.findall(inp)
    return matches

def validate_phone(inp):
    # phone_reg = re.compile(r'^\d{3} \d{3}-?\d{4}$')
    # valid = phone_reg.search(inp)
    phone_reg = re.compile(r'\b\d{3} \d{3}-?\d{4}\b')
    valid = phone_reg.fullmatch(inp)
    return True if valid else False



# print(validate_phone("432 567-4888"))
print(extract_phone("qwe 432 567-4888 qwer"))
# print(extract_all_phones("wqefqwe 432 567-4888 erfgsrgf 432 567-4899 "))