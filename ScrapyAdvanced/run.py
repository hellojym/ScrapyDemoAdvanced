from scrapy import cmdline

name = 'lianjia'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())
