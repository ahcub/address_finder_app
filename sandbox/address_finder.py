import glob
from distutils.filelist import findall
from glob import glob

from lxml import html


def find_company_address_from_web_page(url, company, page_tree):

    address = {
        'company_id': company['id'],
        'url': url, # The path where you found it. Notice that this changes per element in the list
        'name': company['name'],
        'street': 'highway to hell',
        'number': '666',
        'postcode': '12345',
        'city': 'New York',
        'countrycode': 'US',
        'countycode': 'NY',
        'statecode': 'NY',
        'geolevel2': 'NY',
        'province': 'New York County',
        'state': 'New York',
        'phone': '0206666666',
        'fax': '0207777777',
        'email': 'burning@inferno.com',
        'lat': '40.765048',  # may be empty
        'long': '-73.981012',  # may be empty
        'is_hq': 1, # 0 or 1
        'blocked': 0
    }




a = ['Alabama', 'AL',
'Alaska', 'AK',
'Arizona', 'AZ',
'Arkansas', 'AR',
'California', 'CA',
'Colorado', 'CO',
'Connecticut', 'CT',
'Delaware', 'DE',
'Florida', 'FL',
'Georgia', 'GA',
'Hawaii', 'HI',
'Idaho', 'ID',
'Illinois', 'IL',
'Indiana', 'IN',
'Iowa', 'IA',
'Kansas', 'KS',
'Kentucky', 'KY',
'Louisiana', 'LA',
'Maine', 'ME',
'Maryland', 'MD',
'Massachusetts', 'MA',
'Michigan', 'MI',
'Minnesota', 'MN',
'Mississippi', 'MS',
'Missouri', 'MO',
'Montana', 'MT',
'Nebraska', 'NE',
'Nevada', 'NV',
'New Hampshire', 'NH',
'New Jersey', 'NJ',
'New Mexico', 'NM',
'New York', 'NY',
'North Carolina', 'NC',
'North Dakota', 'ND',
'Ohio', 'OH',
'Oklahoma', 'OK',
'Oregon', 'OR',
'Pennsylvania', 'PA',
'Rhode Island', 'RI',
'South Carolina', 'SC',
'South Dakota', 'SD',
'Tennessee', 'TN',
'Texas', 'TX',
'Utah', 'UT',
'Vermont', 'VT',
'Virginia', 'VA',
'Washington', 'WA',
'West Virginia', 'WV',
'Wisconsin', 'WI',
'Wyoming', 'WY',
]
if __name__ == '__main__':
    for file_ in findall(r'C:\Users\Alex\Desktop\basicdata\n'):
        html_page = html.parse(file_)
        for br in html_page.xpath("*//br"):
            br.tail = "\n" + br.tail if br.tail else "\n"
        for p_block in html_page.iter():
            if p_block.tag == 'p':
                if p_block.find('br') is not None:
                    t = p_block.text_content()
                    for entry in a:
                        if entry+' ' in t and ('USA' in t or 'United States' in t):
                            print(t)
                            print('=' * 50)
                            break

addresses_regexs = {
    'US': [
        r'',
    ],
}


def is_block_contains_us_address(block_text):
    if entry+' ' in block_text and ('USA' in block_text or 'United States' in block_text):
        return True
