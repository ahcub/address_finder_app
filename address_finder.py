
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




