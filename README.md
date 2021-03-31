# Request Tracker
A program that tracks **_response times_ to the requests done**, and shows it with a live graph in the dashboard of the site.
![samplegraph](https://user-images.githubusercontent.com/80488910/112766093-f04b1780-9018-11eb-8ae7-3ff7c7c339c1.png)
## Installation
1. Install docker
2. "docker-compose up -d" in the console.

## Usage
Send appropriate requests to
- 127.0.0.1:8080/get
- 127.0.0.1:8080/post
- 127.0.0.1:8080/put
- 127.0.0.1:8080/delete

then you can see the data at
- 127.0.0.1:8080/data

later you can view the data as line graph at
- 127.0.0.1:8080/dashboard

## More in-depth explanation
- The decoder that is used to decode the assignment added as "decoder.py"
- The server checks for requests and write them to logfile.txt with corresponding **response time** and **timestamp**. Response times are randomly generated between 0-3 seconds.  
- Producer reads the logfile and sends them through **kafka** to the topic "LogTopic". Two things done to reduce the resources to read the logfile. First, **python-watchdog** was added so producer only reads logfile when the logfile is modified. Second, producer saves the last index it already read so it can start reading further from that index.
- Consumer takes logs from the "LogTopic" and after connecting to Mongodb, it uploads them to database.  
- Server reads the last one hours' requests from database and store them in /data endpoint.  
- Then server creates a live line graph that refreshes itself every 3 seconds in /dashboard endpoint.

gAAAAABgUn3T_2HCRP7s5RgDwWJNTzNY2tE83AR6YLZNcnACKIc_kXJlcfA52GrUJ2-zk1OSM-0RggncXtFQ2kNO6NfvQTvL6c6_CjUJELo5e65ey_5hYuMGG-GhEZ0QljSn7ppPHt_0VH7D7OTRBDNscgXSpwl9VXyW5g1F52I5BTkh84rsfa0bxDuTQXe8ni7Z_YLl4_GQ6M_-6EUmiAHa8L-NsSUOyA==
