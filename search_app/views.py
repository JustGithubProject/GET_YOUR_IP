import requests
from django.shortcuts import render


def main(request):
    r = requests.get(f"https://api.ipify.org?format=json")
    res = r.json()
    ip = res["ip"]
    context = {
        "ip": ip
    }
    return render(request, 'main.html', context)


