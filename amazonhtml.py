import bs4, requests

def getAmazonPrice(productUrl) :
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#corePrice_feature_div > div > div > span.a-price.aok-align-center > span:nth-child(2) > span.a-price-whole')
    return elems[0].text.strip()

price = getAmazonPrice('https://www.amazon.com/Razer-DeathAdder-HyperSpeed-Wireless-Esports/dp/B0D4RF55QK/ref=sr_1_1_sspa?_encoding=UTF8&content-id=amzn1.sym.12129333-2117-4490-9c17-6d31baf0582a&dib=eyJ2IjoiMSJ9.gzMUG-9kmojrn6unwoaJ8ZTt5l9ViYaDoHxXFL4bnxzYZGDrCcX4-MX7rk_jw76mp1Y-eoHzJZXWyvoyfmedIssOwpTRURjIb9AcFUhhMrDBS6jbX6wv9876eFUIDn6Di-WwRLrF-82VRWqPKYHs_bg9hMuB94xlgBsTYem9MCHH_6xho0X9CmVAxpof2ypUkH6JTqbLuxP3AbuDCnM0rrinQVLBkLs6gWtS7Gt6VvI.O4kycDMfiBO_L6OYcB3euiPi7_NhrfWAyUtNaylufik&dib_tag=se&keywords=gaming+mouse&pd_rd_r=b79924c9-cab9-453e-b763-66b43d4f7ffd&pd_rd_w=bXBWZ&pd_rd_wg=9ZjmW&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=GFH32NKVFYW46QS2VZVP&qid=1722426268&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1')
print('The price is :' + price)
