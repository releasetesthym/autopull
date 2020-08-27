from getContainers import dockerHub
import os

DOCKERHUB_ID = os.environ['DOCKERHUB_ID']
DOCKERHUB_PW = os.environ['DOCKERHUB_PW']

dh = dockerHub(DOCKERHUB_ID)
dh.login(DOCKERHUB_PW)
datas = dh.listRepos()

for data in datas:
    reponame = data['repo']['name']
    namespace = data['repo']['namespace']
    tags = data['tags']

    for tag in tags:
        os.system('docker pull %s/%s:%s' % (namespace, reponame, tag['name']))
        os.system('docker rmi -f %s/%s:%s' % (namespace, reponame, tag['name']))
    
