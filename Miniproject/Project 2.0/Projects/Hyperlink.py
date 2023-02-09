from urllib.parse import urlparse

text_url = "https://www.example.com"
parsed_url = urlparse(text_url)

# check if the URL is valid
if parsed_url.scheme and parsed_url.netloc:
    # create an anchor tag
    link = f"<a href='{text_url}'>{text_url}</a>"
    print(link)
else:
    print("Invalid URL")
    
from html import escape

text_url = "https://www.example.com"
link = f"<a href='{escape(text_url)}'>{escape(text_url)}</a>"
print(link)