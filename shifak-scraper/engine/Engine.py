import time

class Engine:
  def __init__(self):
    self.scraper = None
    self.parser_func = None
    self.results = []
    self.delay = 0
    self.paginator = None

  @classmethod
  def run(cls, scraper):
    engine = cls()
    engine.scraper = scraper
    return engine

  def parse(self, parser_func):
    self.parser_func = parser_func
    return self

  def with_paginator(self, paginator):
    self.paginator = paginator
    return self

  def wait(self, milliseconds):
    self.delay = milliseconds / 1000.0
    return self

  def apply(self, func):
    self.results = list(map(func, self.results))
    return self

  def collect(self):
    return self.results

  def execute(self):
    if not self.scraper or not self.parser_func:
      raise ValueError("Scraper and parser must be set before executing.")

    while True:
      page_content = self.scraper.get_page()
      new_results = self.parser_func(page_content)

      self.results.extend(new_results)

      if self.delay > 0:
        time.sleep(self.delay)

      if self.paginator:
        self.paginator.next()
        next_url = self.paginator.get_next_url()
        if not next_url:
          break
        self.scraper.url = next_url
      else:
        break

    return self