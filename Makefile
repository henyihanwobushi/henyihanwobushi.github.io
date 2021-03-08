NOW=`date +'%Y-%m-%d %H:%M:%S'`

deploy:
	@git add .
	@git commit -m "update at $(NOW)"
	@git push origin master

start:
	nohup bundle exec jekyll server > ./jekyll-server.log 2>&1 &
	open "http://localhost:4000"

stop:
	kill -9 `pgrep "jekyll"`
	rm ./jekyll-server.log

