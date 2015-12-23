import re
from ast import literal_eval
from lxml import html

html_page = html.parse(r'C:\Users\Alex\Desktop\basicdata\n\netop.com\www\classroom-management-software\company\contact.htm_crawled')

for br in html_page.xpath("*//br"):
    br.tail = "\n" + br.tail if br.tail else "\n"

page_text = html_page.getroot().text_content()

print(page_text)

with open('address_styles', encoding='utf-8') as address_styles:
    data = literal_eval(address_styles.read())

    results = {}
    for (key, country_name), address_type in data.items():
        result_regexp = ''
        for line in address_type.splitlines():
            re_line = ''
            if 'Not supported' not in line and 'Address format see' not in line:
                for el in line.split():
                    if country_name.lower() in line.lower():
                        re_line += el + ' '
                        break
                    else:
                        if 'STREET_NAME' in el:
                            regexp = '[\w\s]+'
                        else:
                            regexp = '\w+'
                        if el[0] == '[' and el[-1] == ']':
                            el_name = el[1:-1].lower()
                            if el_name[-1] == ',':
                                regexp += ','
                                el_name = el_name[:-1]

                            re_el = '(?P<%s>%s)?' % (el_name, regexp)
                        else:
                            re_el = '(?P<%s>%s)' % (el.lower(), regexp)

                        re_line += re_el + ' '

                re_line.strip()
                result_regexp += re_line + '\n'

        # result_regexp.strip()
        # if result_regexp:
        #     try:
        #         re_c = re.compile(result_regexp, re.I)
        #     except Exception:
        #         pass
        #     else:
        #         print(country_name)
        #         print(result_regexp)
        #         # results[country_name] = [result_regexp]
        #         result = re_c.search(page_text)
        #         if result:
        #             print(country_name)
        #             print(address_type)
        #             print(result)

# with open('regexps_examples', 'w', encoding='utf-8') as reg_examp:
#     reg_examp.write('{\n')
#     for key, value in results.items():
#         reg_examp.write('\t"%s": %s\n' % (key, value))
#     reg_examp.write('}')
