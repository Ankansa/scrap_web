# StubHub Events Scraper

This project contains a Scrapy spider to scrape event information from StubHub.

## Project Structure

- `scrap_web/spiders/spider_stubhub.py`: Contains the Scrapy spider to scrape events from StubHub.

## How to Run

1. Navigate to the project directory:
    ```sh
    cd /d:/Projects/task
    ```

2. Run the Scrapy spider:
    ```sh
    scrapy crawl events
    ```

3. The scraped data will be saved in JSON files named `op_json_1.json`, `op_json_2.json`, etc., each containing 5 events.

## Requirements

- Python 3.x
- Scrapy

## Installation

1. Install Scrapy using pip:
    ```sh
    pip install scrapy
    ```

2. Clone this repository and navigate to the project directory.

3. Run the spider as described above.