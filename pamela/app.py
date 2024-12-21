import requests

class Pamela:
    def __init__(self):
        self.session = requests.Session()
    
    def create_session(self, address, username=None, password=None):
        self.session.auth = (username, password)

        return self.session.post(address)
    
    def close_session(self):
        self.session.close()

    def receive_data(self, address, json=True ,username=None, password=None, parameters=None, data=None, headers=None, cookies=None, files=None, timeout=None, allow_redirects=True, proxies=None, hooks=None, stream=None, verify=None, cert=None):
        try:
            response = self.session.get(address, params=parameters, headers=headers, cookies=cookies, files=files, timeout=timeout, allow_redirects=allow_redirects, proxies=proxies, hooks=hooks, stream=stream, verify=verify, cert=cert)

            # Check if the response is successful
            if response.status_code == 200:
                if json:
                    data = response.json()
                else:
                    data = response.text
                return data
        except:
            pass

        # if the session didn't work, use a regular request
        if username and password:
            response = requests.post(address, auth=(username, password), params=parameters, headers=headers, cookies=cookies, files=files, timeout=timeout, allow_redirects=allow_redirects, proxies=proxies, hooks=hooks, stream=stream, verify=verify, cert=cert)
        else:
            response = requests.get(address, params=parameters, headers=headers, cookies=cookies, files=files, timeout=timeout, allow_redirects=allow_redirects, proxies=proxies, hooks=hooks, stream=stream, verify=verify, cert=cert)
            
            # Check if the response is successful
            if response.status_code == 200:
                if json:
                    data = response.json()
                else:
                    data = response.text
                return data
            else:
                return None
