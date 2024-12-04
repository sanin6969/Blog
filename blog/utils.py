import requests

def get_client_ip(request):
    return request.META.get('HTTP_X_FORWARDED_FOR', '').split(',')[0] or request.META.get('REMOTE_ADDR')

def get_public_ip():
    try:
        response = requests.get('https://api64.ipify.org?format=json', timeout=5)
        response.raise_for_status()
        return response.json().get('ip')
    except requests.RequestException as e:
        print(f"Error fetching public IP: {e}")
        return None

def get_user_country(request):
    ip = get_client_ip(request)
    if ip in {'127.0.0.1', '::1'}: 
        ip = get_public_ip()

    if not ip:
        return 'Unknown'
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}', timeout=5)
    except requests.RequestException as e:
        print(f"Error fetching country information: {e}")
        return 'Unknown'
    response.raise_for_status()
    country = response.json().get('country', 'Unknown')
    return country
