import requests
import threading


urls = [
    'https://www.example1.com',
    'https://www.example2.com',
    'https://www.example3.com',

]

def get_url_content(url):
    response = requests.get(url)
    print(f'Содержимое веб-страницы {url}:')
    print(response.text)
    print('\n')


threads = []
for url in urls:
    t = threading.Thread(target=get_url_content, args=(url,))
    threads.append(t)


for thread in threads:
    thread.start()


for thread in threads:
    thread.join()

print('Все запросы завершены')

