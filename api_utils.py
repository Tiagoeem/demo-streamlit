import requests

# Configuração
BASE_URL = "http://localhost:5000"

def get_all_bikes():
    try:
        response = requests.get(f"{BASE_URL}/bikes")
        response.raise_for_status()
        return True, response.json()
    except Exception as e:
        return False, {"message": str(e)}

def get_bike_by_id(bike_id):
    try:
        response = requests.get(f"{BASE_URL}/bikes/{bike_id}")
        response.raise_for_status()
        return True, response.json()
    except Exception as e:
        return False, {"message": str(e)}

def add_new_bike(data):
    try:
        response = requests.post(f"{BASE_URL}/bikes", json=data)
        response.raise_for_status()
        return True, response.json()
    except Exception as e:
        return False, {"message": str(e)}

def update_bike(bike_id, data):
    try:
        response = requests.put(f"{BASE_URL}/bikes/{bike_id}", json=data)
        response.raise_for_status()
        return True, response.json()
    except Exception as e:
        return False, {"message": str(e)}

def delete_bike(bike_id):
    try:
        response = requests.delete(f"{BASE_URL}/bikes/{bike_id}")
        response.raise_for_status()
        return True, response.json()  # Supondo que o endpoint retorna JSON. Se não, pode simplesmente ser True.
    except Exception as e:
        return False, {"message": str(e)}

