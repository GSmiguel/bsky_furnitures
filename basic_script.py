import requests
import random
from atproto import Client

# Substitua pelos seus dados de login
email = 'liminal_spacess@outlook.com'
password = 'frango94@'

# Chave da API do Pexels (substitua pela sua chave)
pexels_api_key = '39gP39gTncnngvQeh3DVqAgns3H8DZI0lMaPgTOJAsITFLSmOiQE2tm2'

# URL base da Pexels API
pexels_url = 'https://api.pexels.com/v1/search'

# Limite de tamanho da imagem (976.56KB)
image_size_limit = 976.56 * 1024  # em bytes

# Lista de termos-chave para sortear
search_terms = ['furniture', 'wood furniture', 'plastic furniture', 'metal furniture', 'glass furniture',
                'bamboo furniture', 'ceramic furniture', 'bathroom furniture', 'kitchen furniture',
                'restroom furniture', 'bedroom furniture', 'garden furniture', 'office furniture']

# Sorteia aleatoriamente um termo de busca
random_term = random.choice(search_terms)

# Número de resultados por página e o número de páginas consultadas
results_per_page = 100
max_pages = 5

# Sorteia uma página aleatória para consultar
random_page = random.randint(1, max_pages)

# Parâmetros para a busca de imagens
params = {
    'query': random_term,       # Termo de busca sorteado
    'per_page': results_per_page,  # Quantidade de imagens por página
    'page': random_page          # Página aleatória
}

# Cabeçalhos com a chave de API
headers = {
    'Authorization': pexels_api_key
}

# Fazendo a solicitação à API do Pexels
response = requests.get(pexels_url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
    
    # Verifica se há imagens nos resultados
    if data['photos']:
        suitable_image_found = False

        # Tenta encontrar uma imagem que esteja dentro do limite de tamanho
        while not suitable_image_found and data['photos']:
            # Sorteia aleatoriamente uma imagem entre os resultados
            random_image = random.choice(data['photos'])
            
            # Pega a URL da imagem sorteada
            image_url = random_image['src']['large']
            image_response = requests.get(image_url)
            
            if image_response.status_code == 200:
                image_data = image_response.content

                # Verifica o tamanho da imagem
                image_size = len(image_data)
                print(f"Tamanho da imagem: {image_size / 1024:.2f} KB")

                if image_size <= image_size_limit:
                    suitable_image_found = True
                else:
                    print("Imagem muito grande, tentando outra...")

            # Remove a imagem que foi tentada da lista
            data['photos'].remove(random_image)
        
        if suitable_image_found:
            # Descrição da imagem
            image_alt_text = f"{random_term.capitalize()}"

            # Tentando fazer login no Bluesky
            try:
                print("Tentando fazer login...")
                client = Client(base_url='https://bsky.social')
                client.login(email, password)
                print("Login realizado com sucesso!")
            except Exception as e:
                print(f"Erro ao fazer login: {e}")

            # Criando e enviando o post com imagem
            try:
                # Enviando a imagem
                upload_response = client.send_image(image=image_data, text='', image_alt=image_alt_text)
                
                # Verifique a resposta do upload da imagem
                print("Resposta do upload da imagem:", upload_response)
                    
            except Exception as e:
                print(f"Erro ao criar o post: {e}")
        else:
            print("Nenhuma imagem encontrada que esteja dentro do limite de tamanho.")
    else:
        print("Nenhuma imagem encontrada.")
else:
    print(f"Erro ao acessar a API do Pexels: {response.status_code}")
