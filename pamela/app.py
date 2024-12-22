import requests

class Pamela:
    def __init__(self):
        pass

    def receive_data(self, address, session=None, json=True ,username=None, password=None, parameters=None, data=None, headers=None, cookies=None, files=None, timeout=None, allow_redirects=True, proxies=None, hooks=None, stream=None, verify=None, cert=None):
        if session:
            response = session.get(address, params=parameters, headers=headers, cookies=cookies, files=files, timeout=timeout, allow_redirects=allow_redirects, proxies=proxies, hooks=hooks, stream=stream, verify=verify, cert=cert)

            # Check if the response is successful
            if response.status_code == 200:
                if json:
                    data = response.json()
                else:
                    data = response.text
                return data

        # if the session didn't work, use a regular request
        if username and password:
            auth = requests.auth.HTTPBasicAuth(username, password)
            response = requests.get(address, auth=auth, params=parameters, headers=headers, cookies=cookies, files=files, timeout=timeout, allow_redirects=allow_redirects, proxies=proxies, hooks=hooks, stream=stream, verify=verify, cert=cert)
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

class Session:
    def __init__(self):
        pass
    
    def create(address, username, password):
        session = requests.Session()
        session.auth = (username, password)
        session.post(address)
        return session
    
    def status(address, session):
        response = session.post(address)
        return response.status_code