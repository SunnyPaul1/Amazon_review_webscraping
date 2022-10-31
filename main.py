
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

reviewlist = []
def get_soup(url):
    s = HTMLSession()
    r = s.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def get_reviews(soup):
    reviews = soup.find_all('div', {'data-hook':'review'})
    try:
        for item in reviews:
            review={
                #'product': 'Vitamin D3 + K2 Depot, 180 Tablets, Premium: 99.7+% All Trans MK7 (K2VITAL® by Kappa) + 5,000 IU Vitamin D3, High Dose and Made in Germany',
                #'title': item.find('a', {'data-hook': 'review-title'}).text.strip(),
                #'rating': float(item.find('i', {'data-hook': 'review-star-rating'}).text.replace('out of 5 stars', '').strip()),
                #'body':
                    item.find('span', {'data-hook': 'review-body'}).text.strip()
            }
            reviewlist.append(review)
    except:
        pass



for x in range(1,50):
    soup = get_soup(f'https://www.amazon.de/-/en/Vitamin-Depot-180-Tablets-Premium/product-reviews/B01M36DP4F/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber={x}')
    print(f'Getting page: {x}')
    get_reviews(soup)
    print(len(reviewlist))
    if not soup.find('li', {'class': 'a-disabled a list'}):
        pass
    else:
        break


df = pd.DataFrame(reviewlist)
#df.to_excel('Amazon_review2.xlsx', index = False)
np.savetxt(r'amazon_reviews50.txt', df.values, fmt='%s')