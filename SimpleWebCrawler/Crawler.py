from bs4 import BeautifulSoup

infos = []

with open("./web/new_index.html") as web_data:
    Soup = BeautifulSoup(web_data, 'lxml')
    images = Soup.select('body > div.main-content > ul > li > img')
    titles = Soup.select('body > div.main-content > ul > li > div.article-info > h3 > a')
    rates = Soup.select('body > div.main-content > ul > li > div.rate > span')
    tags = Soup.select('body > div.main-content > ul > li > div.article-info > p.meta-info')
    #print(images, titles, rates, tags, sep='\n----------\n')


for image, title, rate, tag in zip(images, titles, rates, tags):
    data = {
        'title': title.get_text(),
        'image': image.get('src'),
        'rate': rate.get_text(),
        'tag': list(tag.stripped_strings)
    }
    print(data)
    if float(data['rate']) > 3:
        infos.append(data)

for info in infos:
    print(info)
