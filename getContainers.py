import requests, json

HOST = 'https://registry.hub.docker.com'

class dockerHub:
    def __init__(self, usr, version='v2'):
        self.__token = None
        self.version = version
        self.session = requests.Session()

        self.usr = usr
        
    def login(self, pw):
        rst = (self.session.post(
            '%s/%s/users/login' % (HOST, self.version),
            json={'username': self.usr, 'password': pw}
        )).json()

        if 'token' in rst:
            self.__token = rst['token']
    
    def listRepos(self, page_size=10000):
        if self.__token == None:
            raise BaseException('NOT_AUTHORIZED')
        
        rst = []

        repoRst = (self.session.get(
            '%s/%s/repositories/%s/?page_size=%s' % (HOST, self.version, self.usr, page_size),
            headers={'Authorization': 'JWT ${%s}' % (self.__token)}
        )).json()

        for repo in repoRst['results']:
            tags = (self.session.get(
                '%s/%s/repositories/%s/%s/tags/?page_size=%s' % (HOST, self.version, self.usr, repo['name'], page_size),
                headers={'Authorization': 'JWT ${%s}' % (self.__token)}
            )).json()

            rst.append({
                'repo': repo,
                'tags': tags['results']
            })

        return rst