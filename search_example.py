from regexps_examples import regexps
from lxml import html


def get_address_on_page(html_page):
    for br in html_page.xpath("*//br"):
        br.tail = "\n" + br.tail if br.tail else "\n"

    page_text = html_page.getroot().text_content()

    counter = 0
    for regexp in regexps:
        for match_res in regexp.finditer(page_text):
            print(match_res.group())
            print('='*40)
            counter += 1
    print(counter)

if __name__ == '__main__':
    html_page = html.parse(r'C:\Users\Alex\Desktop\basicdata\n\netop.com\www\classroom-management-software\company\contact.htm_crawled')
    get_address_on_page(html_page)
