#import 
from selenium import webdriver
import pickle
import re
#open chromedriver
driver = webdriver.Chrome("chromedriver.exe")
#make an empty dict for results
Player_info = {}
biggest_salary = ["a","2"]


## getting the conversions right
def get_salary(a):
    list1=[]
    try:
        if '달러' in a:
            list1.append(int(re.findall("\d+", a)[0])*0.1156)
        else:
            list1.append(int(re.findall("\d+", a)[0]))
        return list1
    except:
        print("no")
        
##### open file of player id tags in pickle folder
with open("./kbo.pkl", "rb") as f :
    player_id = pickle.load(f)
#for loop through each id page to find information
for id_ in player_id:
    driver.get("https://www.koreabaseball.com/Record/Player/HitterDetail/Basic.aspx?playerId={}".format(id_))
    #add to empty dict for re
    Player_info[id_] = {'선수명': (driver.find_element_by_id(id_="cphContents_cphContents_cphContents_playerProfile_lblName")).text, '등번호': (driver.find_element_by_id(id_="cphContents_cphContents_cphContents_playerProfile_lblBackNo")).text, '생년월일': (driver.find_element_by_id(id_="cphContents_cphContents_cphContents_playerProfile_lblBirthday")).text, '포지션': (driver.find_element_by_id(id_="cphContents_cphContents_cphContents_playerProfile_lblPosition")).text, '신장/체중': (driver.find_element_by_id(id_="cphContents_cphContents_cphContents_playerProfile_lblHeightWeight")).text, '경력': (driver.find_element_by_id(id_="cphContents_cphContents_cphContents_playerProfile_lblCareer")).text, '입단 계약금': (driver.find_element_by_id(id_="cphContents_cphContents_cphContents_playerProfile_lblPayment")).text, '연봉': (driver.find_element_by_id(id_="cphContents_cphContents_cphContents_playerProfile_lblSalary")).text, '지명순위': (driver.find_element_by_id(id_="cphContents_cphContents_cphContents_playerProfile_lblDraft")).text, '입단년도': (driver.find_element_by_id(id_="cphContents_cphContents_cphContents_playerProfile_lblJoinInfo")).text}
    #get biggest salary
    try:
        if (get_salary(biggest_salary[1]))[0] < ((get_salary((driver.find_element_by_id(id_="cphContents_cphContents_cphContents_playerProfile_lblSalary")).text))[0]):
            biggest_salary[0] =(driver.find_element_by_id(id_="cphContents_cphContents_cphContents_playerProfile_lblName")).text 
            biggest_salary[1] =(driver.find_element_by_id(id_="cphContents_cphContents_cphContents_playerProfile_lblSalary")).text
            print((driver.find_element_by_id(id_="cphContents_cphContents_cphContents_playerProfile_lblSalary")).text)
    except:
        print("0 salary")
##save it in a pickle file
with open("./Player_info.pkl", "wb") as f :
    pickle.dump(Player_info, f)