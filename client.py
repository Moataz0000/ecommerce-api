import requests



class MakeRequest:

    @staticmethod
    def get_access_token():
        url = 'http://127.0.0.1:8000/api/v1/users/login/'
        body = {
            "email": "",
            "password": "",
        }
        response = requests.post(url,data=body)
        return response.json()

    @staticmethod
    def refresh_token():
        url = 'http://127.0.0.1:8000/api/v1/users/refresh/'
        refresh = ''
        data = {
            "refresh": refresh
        }
        response = requests.post(url, json=data)
        return response.json()

    @staticmethod
    def cartPost():
        access_token = ''
        url = 'http://127.0.0.1:8000/api/v1/shipping/cart/add/'
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        data = {
            "product_id": 1,
            "quantity": 2
        }
        try:
            response = requests.post(url, headers=headers, json=data)
            if response.status_code in (200, 201):
                return response.json()
            else:
                return {
                    "error": f"Request failed with status code {response.status_code}",
                    "details": response.text
                }
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    @staticmethod
    def cartGet():
        access_token = ''
        url = 'http://127.0.0.1:8000/api/v1/shipping/cart/'
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        response = requests.get(url, headers=headers).json()
        return response

    @staticmethod
    def cartPut():
        access_token = ''
        cart_item_id = 3
        url = f'http://127.0.0.1:8000/api/v1/shipping/cart/update/{cart_item_id}/'
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        data = {
            "product_id": 1,
            "quantity": 5
        }

        try:
            response = requests.put(url, headers=headers, json=data)
            if response.status_code in (200, 204):
                return {"message": "Cart Updated Successfully.", "data": response.json()}
            else:
                return {
                    "error": f"Request failed with status code {response.status_code}",
                    "details": response.text
                }
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    @staticmethod
    def cartDelete():
        access_token = ''
        cart_item_id = 3
        url = f'http://127.0.0.1:8000/api/v1/shipping/cart/delete/{cart_item_id}/'
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        try:
            response = requests.delete(url, headers=headers)
            if response.status_code == 204:
                return {"message": f"Cart item {cart_item_id} deleted successfully"}
            elif response.status_code == 200:
                return response.json()
            else:
                return {
                    "error": f"Request failed with status code {response.status_code}",
                    "details": response.text
                }
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}



if __name__ == '__main__':
    print(MakeRequest.get_access_token())