import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
parser = BeautifulSoup(res.text, 'html.parser')
parser2 = BeautifulSoup(res2.text, 'html.parser')

links = parser.select('.titlelink')
subtext = parser.select('.subtext')

links2 = parser2.select('.titlelink')
subtext2 = parser2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def custom_hacker_news(links, subtext):
    hn = []

    for i, v in enumerate(links):

        title = links[i].getText()
        href = links[i].get('href', 'No href')
        vote = subtext[i].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})

    return sort_stories_by_votes(hn)


pprint.pprint(custom_hacker_news(mega_links, mega_subtext))