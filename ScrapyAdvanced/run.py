from scrapy import cmdline

name = 'meizi'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())
