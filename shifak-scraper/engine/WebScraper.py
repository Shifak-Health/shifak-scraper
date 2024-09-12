import requests

class WebScraper:
  def __init__(self):
    self.url = None
    self.headers = {}

  @classmethod
  def url(cls, url):
    scraper = cls()
    scraper.url = url
    return scraper

  def add_header(self, name, value):
    self.headers[name] = value
    return self

  def with_headers(self, headers):
    self.headers = headers
    return self

  def with_user_agent(self, agent):
    self.headers['User-Agent'] = agent
    return self

  def set_url(self, url):
    self.url = url
    return self

  def get_page(self):
    if not self.url:
      raise ValueError("URL is not set for WebScraper.")
    response = requests.get(self.url, headers=self.headers)
    if response.status_code == 200:
      return response.text
    else:
      raise Exception(f"Failed to retrieve page: {self.url}")
