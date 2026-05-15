import json
import urllib.request
import xml.etree.ElementTree as ET

# Fetch RSS feed (Medium may 403 requests without a browser-like User-Agent)
rss_url = "https://medium.com/feed/@freshsafoduker300"
try:
    req = urllib.request.Request(
        rss_url,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; PortfolioRSS/1.0; +https://nana-safo-duker.github.io)"
        },
    )
    with urllib.request.urlopen(req) as response:
        rss_content = response.read().decode('utf-8')
    
    # Parse XML
    root = ET.fromstring(rss_content)
    
    # Find all items (articles)
    articles = []
    for item in root.findall('.//item'):
        title = item.find('title')
        link = item.find('link')
        pub_date = item.find('pubDate')
        description = item.find('description')
        
        if title is not None and link is not None:
            article = {
                'title': title.text if title.text else '',
                'link': link.text if link.text else '',
                'pub_date': pub_date.text if pub_date is not None and pub_date.text else '',
                'description': description.text if description is not None and description.text else ''
            }
            articles.append(article)
    
    # Print articles as JSON
    print(json.dumps(articles, indent=2))
except Exception as e:
    print(f"Error: {e}")


