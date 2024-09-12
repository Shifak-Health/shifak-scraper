import argparse
import json
from engine.Engine import Engine
from engine.Parser import Parser
from engine.WebScraper import WebScraper
from engine.Paginator import Paginator
from utils.UserAgent import UserAgent


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('url', type=str)

    parser.add_argument('--tag', type=str, default='body')
    parser.add_argument('--delay', type=int, default=1000)
    parser.add_argument('--pagination', type=bool, default=False)
    parser.add_argument('--pagination_param', type=str, default='page')
    parser.add_argument('--total_pages', type=int, default=1)

    args = parser.parse_args()

    if not args.url.startswith('http'):
        print("\033[91m {}\033[00m".format("Please include website scheme (http/https) in the provided address"))
        return

    scraper = WebScraper().with_user_agent(UserAgent().user_agent())

    if args.pagination:
        paginator = Paginator(base_url=args.url, page_param=args.pagination_param)\
            .set_total_pages(args.total_pages)\
            .with_delay(args.delay)

        scraper = scraper.set_url(paginator.get_next_url())
    else:
        scraper = scraper.set_url(args.url)

    engine = Engine\
        .run(scraper)\
        .parse(Parser.get_items([(args.tag, {})]))\
        .wait(args.delay)

    if args.pagination:
        engine = engine.with_paginator(paginator)

    output = engine.execute().collect()
    with open('data.txt', 'w') as file:
        file.write(str(output))

    print("\033[92m {}\033[00m".format("Data has been saved to data.txt"))

if __name__ == '__main__':
    main()