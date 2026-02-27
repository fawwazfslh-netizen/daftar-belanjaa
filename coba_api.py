import urllib.request
import json

urls = [
     "https://api.open-notify.org/astros.json",
     "https://httpbin.org/get",
     "https://jsonplaceholder.typicode.com/posts"
]

for url in urls:
    try:
        print(f"mencoba {url}...")
        response = urllib.request.urlopen(url, timeout=5)
        data_json = response.read().decobe('utf-8')
        data = json.load(data_json)
        print("✅berhasil!\n")
        
        #tampilkan data sesuai URL
        if"astros" in URL
          print(f"astronaut di ISS: {data['number']}orang")
          for astronaut in data ['people']:
              print(f" - {astronaut['name']}")
        elif "httpbi" in url:
            print(f"origin IP: {data['origin']}")
        elif "jsonplaceholder" in url:
            print("contoh judul:", data[0]['title'])
        break #keluar dari loop jika berhasil
    except exception as e:
        print(f"Gagal: {e}\n")
else:
    #jika semua URL Gagal
    print("❎semua URL gagal. gunakan data lokal.")
    data = [{"title": "belajar API"}, {"title": "error Handling"}, {"title": "logging"}]
    print("\ndata lokal:")
    for i, post in enumerate(data, start-1)
        print(f"{i}. {post['title']}")