import requests

def main(username):
  url = f'https://api.mojang.com/users/profiles/minecraft/{username}?'
  response = requests.get(url)
  uuid = response.json()['id']
  
  url = f'https://minotar.net/helm/{username}'
  
  r = requests.get(url)
  
  with open(f'{username}.png','wb') as f:
    f.write(r.content)
    f.close()
  try:
    with open(f"playerData/{username}_data.txt",'w') as f:
      print(r.text)
      playerDat = "UUID: {}\n--".format(uuid)
      f.write(playerDat)
      f.close()
  except:
    with open(f"playerData/{username}_data.txt",'x') as f:
      f.write(f"UUID: {uuid}\n")
      f.close()

#main('SmartCoder3000')