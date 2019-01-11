from django.core.exceptions import ValidationError
import re

def phon_number(val):
    if re.match(r"^\d{3}-?\d{3}-?\d{4}$"):
        return val
    else:
        raise ValidationError
