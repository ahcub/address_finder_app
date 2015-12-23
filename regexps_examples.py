import re

regexps = [
        r'(?P<house_number>\w+) (?P<street_direction>(N|NW|NE|S|SW|SE))? (?P<street_name>[\w ]+)\s+(?P<locality>\w+), (?P<province_abbreviation>\w+) (?P<postal_code>\w+)\s+(?P<country>(united states|USA))',
        r'(?P<house_number>\w+) (?P<street_direction>(N|NW|NE|S|SW|SE))? (?P<street_name>[\w ]+), (?P<building>[\w\s]+)\s+(?P<locality>\w+), (?P<province_abbreviation>\w+) (?P<postal_code>\w+)\s+(?P<country>(united states|USA))',
        r'(?P<street_name>[\w\. ]+) (?P<building>[\w –]+)?\s(?P<postal_code>\w+) (?P<city>[\w -]+)',
        r'(?P<street_name>[\w\. ]+) (?P<building>[\w -]+)?\s(?P<postal_code>[\w-]+) (?P<city>[\w -]+),? ?(?P<country>\w+)?',
        r'(?P<street_name>[\w\. ]+), NO. (?P<building>\w+), (?P<apartment>[\w ]+)\s(?P<district>[\w ]+)\s(?P<city>[\w -]+)\s(?P<country>\w+)',
]

regexps = [re.compile(re_str, re.I) for re_str in regexps]
