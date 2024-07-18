
from urllib.parse import urlparse
def extract_source_name(url):
    domain = urlparse(url).netloc
    return domain.replace('www.', '')


print(extract_source_name('https://www.tipranks.com/news/company-announcements/tscan-therapeutics-advances-in-solid-and-hematological-cancer-therapy'))

print("added new feature")