NOW=`date +'%Y-%m-%d %H:%M:%S'`

deploy:
	@git add .
	@git commit -m "update at $(NOW)"
	@git push origin master

start:
	jekyll s -Bo

stop:
	pkill -f jekyll
