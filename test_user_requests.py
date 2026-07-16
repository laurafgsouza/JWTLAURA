import requests
import json

BASE_URL = "http://127.0.0.1:5000"

def main():
    print("=== Iniciando requisições ===\n")
    
    # 1. /login para obter o token
    print("1. Realizando login...")
    login_data = {
        "email": "test@example.com",
        "senha": "test123"
    }
    login_response = requests.post(f"{BASE_URL}/users/login", json=login_data)
    print(f"Status: {login_response.status_code}")
    print(f"Resposta: {json.dumps(login_response.json(), indent=2)}\n")
    
    if login_response.status_code != 200:
        print("Erro no login! Saindo...")
        return
    
    access_token = login_response.json().get("access_token")
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    # 2. [GET] /recurso para acessar algum recurso (usaremos /services)
    print("2. Realizando GET /services (recurso)...")
    get_response = requests.get(f"{BASE_URL}/services")
    print(f"Status: {get_response.status_code}")
    print(f"Resposta: {json.dumps(get_response.json(), indent=2)}\n")
    
    # 3. [POST] /recurso sem token para retornar erro de autorização
    print("3. Realizando POST /services sem token...")
    service_data = {
        "nome": "Serviço Teste",
        "descricao": "Descrição do serviço teste",
        "preco_base": 100.0
    }
    post_no_token_response = requests.post(f"{BASE_URL}/services", json=service_data)
    print(f"Status: {post_no_token_response.status_code}")
    print(f"Resposta: {json.dumps(post_no_token_response.json(), indent=2)}\n")
    
    # 4. [POST] /recurso com token para registrar recurso
    print("4. Realizando POST /services com token...")
    post_with_token_response = requests.post(f"{BASE_URL}/services", json=service_data, headers=headers)
    print(f"Status: {post_with_token_response.status_code}")
    print(f"Resposta: {json.dumps(post_with_token_response.json(), indent=2)}\n")

if __name__ == "__main__":
    main()
