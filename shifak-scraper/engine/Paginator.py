import time

class Paginator:
  def __init__(self, base_url, page_param='page'):
    self.base_url = base_url
    self.page_param = page_param
    self.current_page = 1
    self.total_pages = None
    self.delay = 0

  def set_total_pages(self, total_pages):
    self.total_pages = total_pages
    return self

  def with_delay(self, delay):
    self.delay = delay / 1000.0
    return self

  def get_next_url(self):
    if self.total_pages and self.current_page > self.total_pages:
      return None
    return f"{self.base_url}?{self.page_param}={self.current_page}"

  def next(self):
    self.current_page += 1
    if self.delay > 0:
      time.sleep(self.delay)