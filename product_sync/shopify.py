import requests
from database.config import Config


class ShopifyAPI():
    api_version = '2022-07'
    api_endpoint = "admin/api"
    
    def __init__(self, shopify_domain=Config.SHOPIFY_DOMAIN, shopify_token=Config.SHOPIFY_TOKEN):
        self.shopify_domain = shopify_domain
        self.headers = {
            "Content-Type": "application/json",
            "X-Shopify-Access-Token": shopify_token
        }
        self.URL_PREFIX = f"https://{self.shopify_domain}/{self.api_endpoint}/{self.api_version}"


    def make_request(self, method, url, json_body=None, params=None):
        func = {
            "GET": requests.get,
            "POST": requests.post,
            "PUT": requests.put,
            "DELETE": requests.delete,
        }.get(method)
        response = func(
            url=url,
            params=params,
            headers=self.headers,
            json=json_body
        )
        if response.ok:
            print(f"Success : For {method} {url} got {response.status_code}")
            response_json = response.json()
            return response_json

        print(f"Failure : For {method} {url} got {response.status_code} {response.text}")
        return {}


class ProductsAPI(ShopifyAPI):

    def create(self, product_json):
        response_json = self.make_request(
            method="POST",
            url = f"{self.URL_PREFIX}/products.json",
            json_body = {"product": product_json}
        )
        return response_json

    def get_by_id(self, product_id):
        response_json = self.make_request(
            method = "GET",
            url = f"{self.URL_PREFIX}/products/{product_id}.json"
        )
        return response_json