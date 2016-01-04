import os
from distutils.filelist import findall

from os.path import join, relpath

from regexps_examples import regexps
from lxml import html


def get_address_on_page(html_page):
    for br in html_page.xpath("*//br"):
        br.tail = "\n" + br.tail if br.tail else "\n"

    for script_block in html_page.xpath('*//script'):
        script_block.getparent().remove(script_block)

    page_text = html_page.getroot().text_content()

    counter = 0
    for regexp in regexps:
        for match_res in regexp.finditer(page_text):
            print(regexp)
            print(match_res.group())
            print('-'*40)
            counter += 1

    return counter

if __name__ == '__main__':
    base = r'C:\Users\Alex\Desktop\outsource'
    globa_counter = 0
    for root, dirs, files in os.walk(base):
        for file_ in files:
            file_path = join(root, file_)
            try:
                print(file_path)
                html_page = html.parse(file_path)
                res = get_address_on_page(html_page)
                globa_counter += res
                print('=' * 100)
            except:
                pass

    print(globa_counter)
