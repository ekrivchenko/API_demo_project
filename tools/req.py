from woocommerce import API

class REQ():

    def __init__(self):

        admin_consumer_key = 'ck_b0e757156fb3090ef21818f4373b44d595aa68a4'
        admin_consumer_secret = 'cs_0f552468a1c7547ef6572155e47d9744fb9ab8b8'
        self.wcapi = API(
            url="http://127.0.0.1/eustore",
            consumer_key=admin_consumer_key,
            consumer_secret=admin_consumer_secret,
            version="v3")

    def test_api(self):
        print(self.wcapi.get('').json())

    def post(self, endpoint, data):
        result = self.wcapi.post(endpoint, data)
        rs_code = result.status_code
        rs_body = result.json()
        rs_url = result.url

        return [rs_code, rs_body, rs_url]

    def get(self, endpoint):
        result = self.wcapi.get(endpoint)
        rs_code = result.response_code
        rs_body = result.json()
        rs_url = result.url

        return [rs_code, rs_body, rs_url]

# x = REQ()
# x.test_api()
