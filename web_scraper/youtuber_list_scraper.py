import requests
from bs4 import BeautifulSoup
import time
import os
import pandas as pd
import codecs
from urllib.parse import urljoin

base_url = "https://ytranking.net"
dynamic_url = "https://ytranking.net"
save_csv = "youtuber_list.csv"

# max_page = 583

data_col = ["channel_name", "channel_url"]
if not os.path.exists(save_csv):
    df = pd.DataFrame(columns=data_col)
    df.to_csv(save_csv)

with codecs.open(save_csv, "r", encoding="utf-8") as f:
# with codecs.open(save_csv, "r") as f:
	df = pd.read_csv(f, index_col=0)

while True:

	res = requests.get(dynamic_url)
	res.raise_for_status()

	html = BeautifulSoup(res.text, 'lxml')
	next_page = html.find("li", class_="next")

	ranking_list_class = html.find("section", class_="ranking")
	youtuber_detail = ranking_list_class.find_all("p", class_="more")
	youtuber_name = ranking_list_class.find_all("h2")

	for i in range(len(youtuber_detail)):

		try:
			print(youtuber_name[i].string)
		except:
			print("Error encoding")
				
		if youtuber_name[i].string in list(df["channel_name"]):
			continue

		res = requests.get(urljoin(base_url, youtuber_detail[i].a.get("href")))
		res.raise_for_status()
		html = BeautifulSoup(res.text, 'lxml')
		profile = html.find("p", class_="thumbnail")
		# name = profile.img.get("alt")
		channel = profile.a.get("href")
		
		s = pd.Series([youtuber_name[i].string, channel],
					   index=data_col)
		df = df.append(s, ignore_index=True)
		df.to_csv(save_csv)
		time.sleep(5)
		
	if bool(next_page) == False:
		break
	dynamic_url = urljoin(base_url, next_page.a.get("href"))
	time.sleep(5)
