import re
from counting_duplicate import duplicate_count

print(duplicate_count('abcda'))
url = "http://www.google.com"
from counting_duplicate import duplicate_count

def domain_name(url):
    return ''.join(re.findall('(?:\/\/w{3}.|\/\/|w{3}.)(.*?)\.', url))


print(domain_name(url))
