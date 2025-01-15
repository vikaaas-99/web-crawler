import asyncio
import json
from scraper import crawl_domains

# Input domains
domains = ["www.amazon.in", "www.flipkart.com"]


# Start crawling
async def main():
    results = await crawl_domains(domains)
    # Save results
    with open("output/product_urls.json", "w") as f:
        json.dump(results, f, indent=4)


if __name__ == "__main__":
    asyncio.run(main())
