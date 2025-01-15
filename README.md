# Web Crawler for Discovering Product URLs on E-commerce Websites

## **Problem Statement**
The goal of this project is to build a scalable and robust web crawler that discovers and lists all product URLs across multiple e-commerce websites. The output is a structured mapping of each domain to its respective product URLs.

---

## **Features**
1. **URL Discovery**:
   - Identifies product URLs based on patterns such as `/product/`, `/item/`, `/dp/`, and `/gp/product/`.
2. **Scalability**:
   - Handles deep hierarchies and large websites using asynchronous requests for improved performance.
3. **Robustness**:
   - Manages edge cases, including dynamic content, pagination, and variations in URL structures.
4. **Output**:
   - Generates a structured JSON file mapping each domain to its product URLs.

---

## **Tech Stack**
- **Language**: Python
- **Libraries**:
  - `aiohttp` - Asynchronous HTTP requests.
  - `BeautifulSoup` - HTML parsing.
  - `re` - Regex for URL pattern matching.
  - `urllib.parse` - For URL joining and normalization.

---

## **Setup Instructions**

### Install Dependencies
1. Clone this repository:
   ```bash
   git clone https://github.com/vikaaas-99/web-crawler.git
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   cd crawler
   ```

2.	Install required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

---

## **Run the Script**
1.	Execute the crawler:
    ```bash
    python main.py
    ```

2. Output will be saved in a JSON file (output/product_urls.json) in the following format:
    ```json
    {
        "example1.com": ["https://example1.com/product/123", "https://example1.com/product/456"],
        "example2.com": ["https://example2.com/item/789"]
    }
    ```

---

## **Approach**
1\. Pattern Matching:
- Uses predefined patterns like /dp/, /gp/product/, and /item/ to identify product URLs.
- Employs regex for robust URL filtering.

2\. Asynchronous Crawling:
- Handles multiple domains and pages concurrently with aiohttp and asyncio.

3\. Pagination Handling:
- Detects and follows pagination links to crawl category pages deeply.

---

## **Known Limitations**
- Websites requiring CAPTCHA or anti-bot measures may not be fully crawlable.
- JavaScript-heavy sites may require additional setup (e.g., Selenium).

---

## **Future Enhancements**
- Implement retry mechanisms for failed requests.
- Expand product URL patterns to support more e-commerce platforms.

---

## **Output Example**

### Sample output (product_urls.json):

 ```json
 {
     "www.amazon.in": [
         "https://www.amazon.in/GRECIILOOKS-Women-Rayon-Regular-X-Large/dp/B0CNZYHGT4?_encoding=UTF8&pd_rd_w=IgnGN&content-id=amzn1.sym.20f90b4c-138e-4c87-8bfd-4c0edd6f78bf&pf_rd_p=20f90b4c-138e-4c87-8bfd-4c0edd6f78bf&pf_rd_r=N6E0GFSRK6DREAVHQFBP&pd_rd_wg=8lo9J&pd_rd_r=b1bd3dd1-e250-4998-aaa2-e97d8677f718&ref_=pd_hp_d_btf_SPB",
         "https://www.amazon.in/Crompton-Storage-Heater-Advanced-Safety/dp/B08GSQXLJ2?_encoding=UTF8&pd_rd_w=ynDNx&content-id=amzn1.sym.21c54421-6876-41ac-9da2-30c4fcf91bf8&pf_rd_p=21c54421-6876-41ac-9da2-30c4fcf91bf8&pf_rd_r=N6E0GFSRK6DREAVHQFBP&pd_rd_wg=8lo9J&pd_rd_r=b1bd3dd1-e250-4998-aaa2-e97d8677f718&ref_=pd_hp_d_btf_homenKitchen",
     ],
     "www.flipkart.com": [
         "https://www.flipkart.com/oneplus-buds-3-tws-ear-earbuds-sliding-volume-control-49db-anc-bluetooth/p/itmfccde298e032a?pid=ACCGRNFMDTYGWMW9"
     ]
 }
 ```
