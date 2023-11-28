import socket
import urllib.parse
import re


def beginconnection(url):
    parsedurl = urllib.parse.urlparse(url)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sck:
        sck.connect((socket.gethostbyname(parsedurl.hostname), 80))

        req = f"GET {parsedurl.path if parsedurl.path is not None else '/'} HTTP/1.1\r\n"
        req += f"Host: {parsedurl.hostname}\r\n"
        req += f"\r\n"

        sck.sendall(req.encode())

        val: str = ''

        try:
            sck.settimeout(2)
            while True:
                buf = sck.recv(4096)

                if not buf:
                    break

                val += buf.decode()
        except:
            pass
        finally:
            sck.settimeout(None)

        amount = len(val)  # condition of ex. 4

        val = val.split('\r\n\r\n')[1]  # condition of ex. 5

        print(val[:3000] if amount >= 3000 else val)  # condition of ex. 2
        print('\n\n\n')
        print(amount, 'characters received')

        parcount = len(re.findall(r'(?<=<p>).+(?=<\/p>)', val, re.M))  # condition of ex. 4

        print('The count of paragraphs =', parcount)


while True:
    url = input("Enter URL: ")
    parsed = urllib.parse.urlparse(url)
    print(parsed.hostname)
    if parsed is None or parsed.hostname is None:
        print("Invalid URL! Try again.")
        continue
    try:
        beginconnection(url)
    except:
        print("Something went wrong!")
    break
