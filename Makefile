NOW=`date +'%Y-%m-%d %H:%M:%S'`

deploy: save
	@git push origin gh-pages
	open https://henyihanwobushi.github.io/

save:
	@git add .
	@git commit -m "update at $(NOW)"

start:
	jekyll s -Bo

stop:
	pkill -f jekyll
