import requests
from bs4 import BeautifulSoup
import os
import time
import glob
import pandas as pd
import codecs

# child1 = "child1"
# child2 = "child2"
# growth = "growth"
# mature = "mature"
# per = "per"
# ultimate = "ultimate"
# armor = "armor"
# hybrid = "hybrid"
# wars = "wars"
# unknown = "unknown"

response = requests.get("http://www.b-boys.jp/series/digimon/reference/")
response.raise_for_status()

root_dir = "./digimon_pictures_and_profile/"

os.makedirs(root_dir, exist_ok=True)
# os.makedirs(root_dir + child1, exist_ok=True)
# os.makedirs(root_dir + child2, exist_ok=True)
# os.makedirs(root_dir + growth, exist_ok=True)
# os.makedirs(root_dir + mature, exist_ok=True)
# os.makedirs(root_dir + per, exist_ok=True)
# os.makedirs(root_dir + ultimate, exist_ok=True)
# os.makedirs(root_dir + armor, exist_ok=True)
# os.makedirs(root_dir + hybrid, exist_ok=True)
# os.makedirs(root_dir + wars, exist_ok=True)
# os.makedirs(root_dir + unknown, exist_ok=True)

soup = BeautifulSoup(response.text, 'lxml')
links = soup.find_all("div", class_="reference")

already_stored_file = glob.glob("./digimon_pictures_and_profile/*/*/*.jpg")
file_list = []
for f in already_stored_file:
    digi_pic = os.path.basename(f)
    file_list.append(digi_pic[:-4])

data_col = ["ja_name", "rome_name", "tag_name", "level", "type", "attribute", "tech", "url"]
# csvファイルに一から書き込む場合
if not os.path.exists(root_dir + "digimon_profiles.csv"):
    df = pd.DataFrame(columns=data_col)
    df.to_csv(root_dir + "digimon_profiles.csv")

for link in links:
    # 画像とテキストのまとまっているurlを取得
    get_href = link.find("a").get("href")         # ex: ('detail.php?dir=02-ka&name=kuramon')
    digimon_name = get_href.split("=")[-1]
    # 世代を取得
    get_li = link.find("li")
    level = get_li.get("class")[1]
    # 世代別フォルダの作成
    os.makedirs(root_dir + level, exist_ok=True)
    if digimon_name in file_list:
        print("{0} はすでに保存済みです".format(digimon_name))
        continue
    # 取得したデジモンの画像とテキストをまとめて保存するフォルダの作成
    digimon_profile_dir = root_dir + level + "/" + digimon_name
    os.makedirs(digimon_profile_dir, exist_ok=True)
    res = requests.get("http://www.b-boys.jp/series/digimon/reference/" + get_href)
    res.raise_for_status()
    digi_soup = BeautifulSoup(res.text, 'lxml')
    img_link = digi_soup.find("img")["src"]
    res = requests.get("http://www.b-boys.jp/" + img_link)
    
    ja_name = digi_soup.find("h1").text                     # 日本語名
    rome_name = digi_soup.find("p").text                    # ローマ字
    gene_class = digi_soup.find_all("li")[0].text           # 世代
    type_name = digi_soup.find_all("li")[1].text            # タイプ
    attribute_name = digi_soup.find_all("li")[2].text       # 属性
    tech_name = digi_soup.find_all("li")[3].text            # 技名
    digi_profile_text = digi_soup.find_all("li")[4].text    # プロフィール
    url = "http://www.b-boys.jp/series/digimon/reference/" + get_href
    # データフレームに保存
    with codecs.open(root_dir + "digimon_profiles.csv", "r", encoding="utf-8") as f:
        df = pd.read_csv(f, index_col=0)
    s = pd.Series([ja_name, rome_name, digimon_name, gene_class, type_name, attribute_name, tech_name, url],
                   index=data_col)
    df = df.append(s, ignore_index=True)
    df.to_csv(root_dir + "digimon_profiles.csv")

    # 各項目の保存先
    img_name = digimon_profile_dir + "/" + digimon_name + ".jpg"
    profile = digimon_profile_dir + "/" + digimon_name + "_profile.txt"
    attr_words = digimon_profile_dir + "/" + digimon_name + "_attribute.txt"

    print("downloading " + img_name)
    with open(img_name, 'wb') as f:
        for chunk in res.iter_content(int(1e+5)):
            f.write(chunk)
    with open(profile, 'w', encoding="utf-8") as f:
        f.write(digi_profile_text)
    with open(attr_words, 'w', encoding="utf-8") as f:
        f.write(ja_name + "," + 
                rome_name + "," +
                gene_class + "," +
                type_name + "," +
                attribute_name + "," +
                tech_name)
    
    time.sleep(5)
	