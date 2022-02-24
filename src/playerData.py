import requests
import os
import re
import subprocess

def Node(id):
  h = id[20:len(id)]
  return ':'.join(h[i:i+2] for i in range(0,12,2))

def main(username):
  url = f'https://api.mojang.com/users/profiles/minecraft/{username}?'
  response = requests.get(url)
  uuid = response.json()['id']
  
  url = f'https://minotar.net/helm/{username}'
  
  r = requests.get(url)
  os.mkdir('playerData/{}'.format(username))
  global mac
  mac = Node(uuid)
  
  with open(f'playerData/{username}/{username}.png','wb') as f:
    f.write(r.content)
    f.close()
  json = {
    "username":username,
    "uuid":uuid,
    "mac":mac
}
  try:
    with open(f"playerData/{username}/{username}_data.json",'w') as f:      
        f.write(str(json))
        f.close()
  except:
    with open(f"playerData/{username}/{username}_data.json",'x') as f:
        f.write(str(json))
        f.close()

main(input("Input A Username > "))