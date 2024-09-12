from bs4 import BeautifulSoup

class Parser:
  def __init__(self, soup):
      self.soup = soup
      self.parsing_functions = []

  @classmethod
  def get_items(cls, elements, **kwargs):
      def parse_page(content):
          soup = BeautifulSoup(content, 'lxml')
          results = []
          for tag, kwargs in elements:
            results.extend(soup.find_all(tag, **kwargs))
          return results
      return parse_page