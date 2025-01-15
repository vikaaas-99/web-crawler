import re
import aiohttp
import asyncio
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Product URL pattern
PRODUCT_PATTERNS = ["/product/", "/item/", "/p/", "/dp/", "/gp/product/"]


async def fetch(session, url):
    try:
        async with session.get(url, timeout=10) as response:
            return await response.text()
    except Exception as e:
        print(f"Error fetching {url}: {str(e)}")
        return None


async def crawl_domain(domain):
    base_url = f"https://{domain}"
    visited_urls = set()
    product_urls = set()

    async with aiohttp.ClientSession() as session:
        html = await fetch(session, base_url)
        if not html:
            return product_urls

        soup = BeautifulSoup(html, "html.parser")
        # print(soup, "soup")
        for link in soup.find_all("a", href=True):
            href = link["href"]

            PAGINATION_REGEX = re.compile(r"\?page=\d+")
            if PAGINATION_REGEX.search(href):
                full_url = urljoin(base_url, href)
                print(full_url, "-->full_url")
                print("*" * 100)
                if full_url not in visited_urls:
                    visited_urls.add(full_url)
            else:
                full_url = urljoin(base_url, href)
                print(full_url, "-->full_url")
                print("*" * 100)
                if full_url not in visited_urls:
                    visited_urls.add(full_url)

            # Regex for product pages
            PRODUCT_REGEX = re.compile(r"(\/dp\/|\/gp\/product\/|\/product\/|\/item\/|\/p\/)")
            # Check if the URL matches the regex
            if PRODUCT_REGEX.search(href):
                product_urls.add(full_url)
    return product_urls


async def crawl_domains(domains):
    tasks = [crawl_domain(domain) for domain in domains]
    results = await asyncio.gather(*tasks)
    return {domain: list(result) for domain, result in zip(domains, results)}
