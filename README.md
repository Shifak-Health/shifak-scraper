# Shifak WebScraper

> This is a part of the Shifak project, designed to collect drug data from various websites. It will later be enhanced with LLMs (Large Language Models).

WebScraper is a Python tool for scraping medical websites. It's designed to be both simple and effective, while avoiding detection by website security measures.

## Features

### Random Time Intervals

Simulates human browsing by varying the time between requests, so it looks more like real user activity.

### Changable User-Agent

Helps prevent blocks by automatically changing the User-Agent for each request, making the requests appear more like they come from different users.

### Paginator

Handles pagination by navigating through multiple pages of data.

## Getting Started

### Prerequisities

- Python 3.x
- Pip

### Installation

```bash
docker build -t shifak-scraper -f Dockerfile .
```

To run WebScraper using Docker, execute the following command:

```bash
docker run -d -v $(pwd):/app -w /app/shifak-scraper shifak-scraper \
   python -m shifak-scraper URL
```


## Usage

| Argument           | Type   | Default  | Description                                                             |
|--------------------|--------|----------|-------------------------------------------------------------------------|
| url                | String | Required | The target URL of the website to scrape.                                |
| --tag              | String | 'body'   | The HTML tag to search for (default is body).                           |
| --delay            | Int    | 1000     | The delay (in milliseconds) between requests to mimic human browsing.   |
| --pagination       | Bool   | False    | Enable or disable pagination for scraping multiple pages.               |
| --pagination_param | String | 'page'   | The pagination parameter to be used in the URL (e.g., ?page=2).         |
| --total_pages      | Int    | 1        | The total number of pages to paginate through if pagination is enabled. |

