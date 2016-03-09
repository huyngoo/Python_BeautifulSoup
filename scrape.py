from bs4 import BeautifulSoup
import requests
import re
import csv
for i in range(0,135,15): 
	url = "http://www.oldclassiccar.co.uk/forum/phpbb/phpBB2/viewtopic.php?t=12591&postdays=0&postorder=asc&start={}&sid=c94ca698661bdd01e674a5cf0d7be866".format(i)
	r = requests.get(url)
	encoded = r.text.encode('utf-8')
	soup = BeautifulSoup(encoded,"html.parser")
	offset = 0

	post_details = soup.find_all("span", {"class":"postdetails"})
	post_id = soup.find_all("span", {"class":"name"})
	post_bodies = soup.find_all("span",{"class":"postbody"})
	post_details = [x for x in post_details if "Posted" in x.contents[0]]
	post_bodies = [x for x in post_bodies if x.contents != []]
	for i in range(0,len(post_id)):
		curr_list = [[] for k in range (0,1)]
		curr_id = str(post_id[i].contents[0])
		curr_list[k].append(int(re.search(r'\d+', curr_id).group()))
		curr_list[k].append((str(post_id[i].contents[1])[3:-4]))
		curr_list[k].append(str(post_details[i].contents[0])[8:])
		j=0
		temp_post_body =""
		while j < len(post_bodies[i].contents):
			if not ("______")in post_bodies[i].contents[j]:
				try:
					if(post_bodies[i].contents[j].name == None):
						temp_post_body+= post_bodies[i].contents[j]
					elif(post_bodies[i].contents[j].name == "br"):
						temp_post_body+=(r"\n")
				except:
					pass
			else:
				break
			j+=1
		curr_list[k].append(temp_post_body)	
		with open('forum.csv','a') as csvfile:
			a = csv.writer(csvfile)
			a.writerow(curr_list);