NOW=`date +'%Y-%m-%d %H:%M:%S'`

deploy:
	@git add .
	@git commit -m "update at $(NOW)"
	@git push origin gh-pages
	open https://henyihanwobushi.github.io/

start:
	jekyll s -Bo

stop:
	pkill -f jekyll
