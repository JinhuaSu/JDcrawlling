# JDcrawlling

**target**

- get the phone selling data in JD.com
	+ include basic info of phone
	+ include comment of the phone

**problem**

- find my request get no a valid html, maybe my header --done
	+ test my mechine can or not get real html --done 
	+ yes, it my request not valid for JD.com
		- find in the internet and make sure I can get a valid result
- learn the html extracting method
	+ tidy
	+ make a pandas excel which may be a little bit big
- info I need
	+ price
	+ number of comment
	+ score of the phone
	+ phone info(which day sell)
	+ record the sub url for further crawlling
- write a func for one item url crapy
- another difficulty: anti-crawl in price and comment score
	+ find the json to request
		- https://club.jd.com/comment/productCommentSummaries.action?referenceIds={0}
		- https://p.3.cn/prices/mgets?skuIds=J_{0}
- dirty data
	+ find out the result 
	+ fail record in /result/dirty_example.txt

**to-do-list**

- make one phone pd -> dict --done
- make a table and test for inserting one -> mysql --done
- have a raw
- code a class for the seperating
- change the name with the unit and make the new data base as a numerial variable

