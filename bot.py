import requests
import json

class Bot:

    def __init__(self, botToken, auth, group):
        self.bot_token = botToken
        self.auth_token = auth
        self.group_id = group

    def __makePostRequest(self, url, params):
        base_url = 'https://api.groupme.com/v3'
        r = requests.post(base_url + url, params = params)

        print(r.status_code)
        print(r.text)
        return r.status_code

    def __post_data():
        base_url = 'https://7bfa877e.ngrok.io'
        payload = json.dumps({'user': 'pass'})

        r = requests.post(base_url, data=payload)
        print(r.status_code)

    def __getBinaryData(url):
        r_file = requests.get(url)
        content = r_file.content
        return content

        # with open('test.txt', 'wb') as fd:
        #     #for chunk in r_file.iter_content(chunk_size=128):
        #         fd.write(content)

    def postMessage(self, text):
        url = '/bots/post'
        params = {'bot_id': self.bot_token, 'text': text}
        return self.__makePostRequest(url, params)

    # def run(self):
    #     img_list = self.__post_images_FS()
    #     return img_list
