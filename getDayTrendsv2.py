#python3 getDayTrends.py 2019-01-10 2019-01-31
import datetime
from scrapy import Selector
import requests
from time import sleep
import random
import argparse

#Parsing Arguments using argparse Library
parser = argparse.ArgumentParser(description="Get Twitter Trending Hourly HashTags<Top50>")
parser.add_argument("start_date",action="store",help="Enter Your Starting Date In this position In YYYY-MM-DD Format")
parser.add_argument("end_date",action="store",help="Enter Your Ending Date In this Postion In YYYY-MM-DD Format")
parser.add_argument("--country","-c",action="store",help="Enter Your Country Name",default="india")
parser.add_argument("--sleep",action="store",type=int,help="Enter Your Desired Sleeping Time",default=0)
parser.add_argument('--version', action='version', version='%(prog)s 2.0')
args = parser.parse_args()
print(args.version)

#Function To Generate Dates And Times
def generate_dates_times(start,stop):
	today = datetime.datetime.today()
	start = int(getattr(today - (datetime.datetime.strptime(start,"%Y-%m-%d")),"days"))
	stop = int(getattr(today - (datetime.datetime.strptime(stop,"%Y-%m-%d")),"days"))
	dates,times = [],[]
	for i in range(start,stop+1):
		dates.append(str((today-datetime.timedelta(days=i)).strftime("%Y-%m-%d")))
	for i in range(0,24):
		times.append(str(i))
	return dates,times

#Function To Get Data
def get_data(response,i):
	hashtag = ""
	tweet_count = ""
	tmp = response.xpath('//*[@id="table-body"]/tr[' + str(i) + ']/td[2]/span/b/text()').extract()
	if len(tmp) == 0:
		tmp = response.xpath('//*[@id="table-body"]/tr[' + str(i) + ']/td[2]/span/text()').extract()
	hashtag = process_hashtag(tmp[0])
	tmp = response.xpath('//*[@id="table-body"]/tr[' + str(i) + ']/td[2]/i/text()').extract()
	tweet_count = process_tweet_count(tmp[0])
	return hashtag,tweet_count	

#Function To Process Tweet Count
def process_tweet_count(tweet_count):
	for i in tweet_count:
		if i.isdigit():
			index = tweet_count.index(i)
			break
	return tweet_count[index:]

#Function To Process HashTag
def process_hashtag(hashtag):
	if hashtag[0] != "#":
		hashtag = "#" + hashtag
	return hashtag

#Finally Using All The Functions
dates,times = generate_dates_times(args.end_date,args.start_date)
for date in dates:
	out = open(date + ".tsv","w")
	out.write("hashtag\ttweet_count\ttime\n")
	for time in times:	
		while True:
			try:
				url = "https://getdaytrends.com/" + args.country + "/" + date + "/" + time + "/"
				print(url)
				response = requests.get(url)
				sleep(args.sleep)
				response = Selector(response=response)
				for i in range(1,52):
					try:
						if i == 6:
							continue
						hashtag,tweet_count = get_data(response,i)
						out.write(hashtag + "\t" + tweet_count + "\t" + time + "\n")
					except IndexError:
						print("Index Error",i)
						continue
				break
			except requests.exceptions.SSLError:
				print("error",time)
				pass
	out.close()
