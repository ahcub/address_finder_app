from ast import literal_eval

import requests
from lxml import html

a = 'http://www.addressdoctor.com/index.php?eID=ad_worldMAP&SAMPLE=%s&lang=1'


result_dict = {}

with open('addresses_types', encoding='utf-8') as data_file:
    v = literal_eval(data_file.read())

for item in v:
    req = a % (item['cosiso3'].lower() + '%%2B' + item['cosnameen'].lower().replace(' ', '+'))

    html_page = html.parse(req)

    for br in html_page.xpath("*//br"):
            br.tail = "\n" + br.tail if br.tail else "\n"

    key = (item['cosiso3'], item['cosnameen'])
    result_dict[key] = []
    for el in html_page.xpath('//*[@id="cosaddressformat"]/div/div/p'):
        result_dict[key] = el.text_content()


with open('address_styles', 'w', encoding='utf-8') as address_styles:
    address_styles.write(str(result_dict))
