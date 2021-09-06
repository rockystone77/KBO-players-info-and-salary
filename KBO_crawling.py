#import 
import pickle
import requests
from bs4 import BeautifulSoup as BS
## getting the conversions right
def get_salary(player_info):
    maximum = 0
    player_name = ""
    for data in player_info:
        if data['연봉'][-2:] == "만원":
            compare = int(data['연봉'][:-2]) * 10000
        elif data['연봉'][-2:] == "달러":
            compare = int(data['연봉'][:-2]) * 1100
        if maximum < compare:
            maximum = compare
            player_name = data['선수명']
    return (player_name, maximum)
        
##### open file of player id tags in pickle folder
with open("./kbo.pkl", "rb") as f :
    player_id = pickle.load(f)
#for loop through each id page to find information
def crawling_kbo(kbo_id):
    url = "https://www.koreabaseball.com/Record/Player/PitcherDetail/Basic.aspx?playerId={}"
    target_url = url.format(kbo_id)    
    r = requests.get(target_url)
    bs = BS(r.text)
    bs_rt = bs.find("div", class_='player_basic').findAll("li")
    player = [x.find("span").text for x in bs_rt]
    player_key = [x.find("strong").text.split(":")[0] for x in bs_rt]
    return dict(zip(player_key, player))
player_info = []
for idx, id_ in enumerate(player_id):
    if idx % 100 == 0: print(idx)
    player_info.append(crawling_kbo(id_))
    
print(get_salary(player_info))