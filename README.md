# twitter-hourly-trends
This is a command-line tool for getting hourly (Top 50) trending hashtags

## Usage:
This tool can be used by both Linux and Mac Users.

- **Command 1:**

`python3 getDayTrendsv2.py -h`

The above command gives output as below:

    usage: getDayTrendsv2.py [-h] [--country COUNTRY] [--sleep SLEEP] [--version]
                         start_date end_date

    Get Twitter Trending Hourly HashTags<Top50>

    positional arguments:

      start_date            Enter Your Starting Date In this position In YYYY-MM-
                        DD Format
                        
      end_date              Enter Your Ending Date In this Postion In YYYY-MM-DD
                        Format

    optional arguments:

      -h, --help            show this help message and exit
  
      --country COUNTRY, -c COUNTRY
                        Enter Your Country Name
                        
      --sleep SLEEP         Enter Your Desired Sleeping Time
  
      --version             show program's version number and exit

This program has 2 positional arguments and 4 optional arguments

- **Command 2:**

`python3 getDayTrendsv2.py 2019-10-15 2019-10-16`

The above command gives the top 50 trending hashtags per hour over the given period i.e., from 2019-10-15 to 2019-10-16

The output will be written directly to a file named "<date>.tsv" and the file contains output in the following format:
  
  header:"hashtag\<tab spaced\>tweet_count\<tab spaced\>time"
  
  *Example:*
  
        1. #BarçaCelta     35527   0
        
        2. #Ram Lalla      35041   1
        
        3. #ITAAwards2019  10000   19
        
   In the output the time is indicated as the following:
     
   *For suppose if time column contains "0" it means 12:00 AM, "1" implies 01:00 AM, similarly "23" implies 11:00 PM etc.,*
   
   - **Time is in 24-hour Format**
   - **If many dates are present in the given period then multiple output files will be automatically created such as \<date\>.tsv**
   - *Example:*
        - *If for suppose period is 2019-10-15 2019-10-16 then two files will be created with names 2019-10-15.tsv and 2019-10-16.tsv and these contains the hourly top 50 trends in the above mentioned format*
# Issue: 
* *It is not working for current date i.e., it'll work for all past days except current day*
