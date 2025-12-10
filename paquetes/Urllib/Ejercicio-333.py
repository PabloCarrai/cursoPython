from urllib.request import urlopen

url = "https://www.python.org"

try:
    with urlopen(url) as response:
        html_content_bytes = response.read()
        html_content_string = html_content_bytes.decode("utf-8")
        print(html_content_string)
except Exception as e:
    print(f"Error abriendo o leyendo url: {e}")
