import requests

# URL adresi
url = "https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json"

# URL'den veriyi çekme
response = requests.get(url)

# Veriyi JSON formatına dönüştürme
data = response.json()

# 'price' anahtarına göre verileri sıralama
# Önce 'price' değerini ondalık sayıya çevirmemiz gerekiyor
sorted_data = sorted(data, key=lambda x: float(x['price']), reverse=True)

# En yüksek fiyatlı 10 kripto para birimini yazdırma
for item in sorted_data[:10]:
    print(f"Currency: {item['currency']}, Price: {item['price']}")