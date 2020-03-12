from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


def parse_book_reviews(url):
    bookClient = uReq(url)
    book_html = bookClient.read()
    bookClient.close()
    book_soup = soup(book_html,"html.parser")
    reviewsTable = book_soup.find('div', attrs = {'id':'bookReviews'})
    reviews = []
    span_array = []
    for review in reviewsTable.find_all('div', {"class": "friendReviews elementListBrown"}):
        spans = review.find_all('span')
        span_array.append(spans)
        spans.pop()
        spans.pop()
        spans.pop()
        spans.pop()
        likes = int(spans.pop().text.split(' ')[0])
        reviewtext = spans.pop().text

        spans.reverse()
        username = spans.pop().text
        # Username will look like '\nKate\n',
        username = username[1:-1]
        reviews.append((username, reviewtext, likes) )
    return book_soup

book_url = 'https://www.goodreads.com/book/show/249.Tropic_of_Cancer'
soup = parse_book_reviews(book_url)

