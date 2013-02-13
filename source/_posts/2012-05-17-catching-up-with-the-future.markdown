---
layout: post
title: "Catching up with the future"
date: 2012-05-17 16:26
comments: true
categories: [redis, mongodb, airG]
---
<p>One of the things that started happening @work in the last year is that more
developers within the company began looking to use a wider (and more recent)
selection of technology. @work has been running for years on a LAMP (Linux, 
Apache 1.3x, MySQL, Perl) stack.</p>

<p>With a move to JavaScript, HTML5, and CSS3 for front-end development, and
node.js for some of the back-end infrastructure, there have been opportunities
to try new languages, databases, caches, etc.</p>

<p>Like any group of people picking new technology, sometimes you pick wisely. 
Other times…</p>

<p><strong>When you don’t know what your choice means</strong></p>

<p><img alt="MongoDB" height="100" width="225" src="http://media.mongodb.org/logo-mongodb.png"/></p>

<p>About 8 months ago, one project team was facing a high volume of reads 
(and a fairly high volume of writes). They decided to try using MongoDB for 
storing their data. They went through some rough outages, but managed to 
persevere and got it working (and it still works). However, sometimes success 
makes everything look like it can be solved the same way.</p>

<p>There were some features that were meant only for paying users. This is where things quickly got painful.</p>

<p>They used MongoDB to also store whether or not the user had paid, and should therefore be granted access to additional content and features. There was already a billing system that stored this information, but they wanted to cache the billing access in MongoDB. Some of you will already be thinking of the ways this can go wrong, but for now I’m not going to focus on the risks of having data and responsibilities being duplicated across different platforms. Instead I’ll focus on the disadvantage of using MongoDB for this.</p>

<p>In this particular use case, with MongoDB’s eventual consistency, users could have successfully paid, but depending on which MongoDB node the requests came to immediately after purchasing, the node may or may not have the updated data.</p>

<p>MongoDB isn’t where you want to store this kind of information. You need your view of billing data to be consistent 100% of the time. Imagine if you 
occasionally lost access to your TV channels because the system storing your
billing state wasn’t consistent.</p>

<p>People don’t like it when you mess up the access they have paid for.</p>

<p><strong>Speed and consistency</strong></p>

<p><img alt="Redis" height="100" width="200" src="http://redis.io/images/redis.png"/></p>

<p>
Since it was now impacting users for something they had paid for, I became involved from the billing side of @work. Myself and another developer (from the Integrations team) volunteered to take care of it. We were faced with a few problems:
</p>

<ol>
	<li>The technical - data needed to be accessed frequently (about 4,000 - 5,000 queries per second with higher volumes expected), and had to be consistent each time.</li>

	<li>There was no documentation on what had been done or how the product was supposed to work. Argh.</li>
</ol>

<p>
Fortunately, the actual amount of data to store was small, and could easily fit into memory. This is where we could have used memcache. We already had memcache in use in other areas of the company infrastructure, so it would be easy to spin up another instance.
</p>

<p>
After a bit of research though, we decided to use Redis. Aside from being ridiculously fast (testing showed it capable of 100,000 queries per second on our servers), it supports storing data structures such as hashes, sets, sorted sets, and lists.
</p>

<p>
Additionally, Redis was easy to work with. Compared to the rest of the code we needed to change, suddenly the data store and it’s performance was no longer a concern. Redis just worked.
</p>

<p>
Since moving the data over to Redis and ensuring that the billing system was responsible for updating it, I can say that Redis has been completely solid for us. Billions and billions of hits, no downtime, reasonably easy to slave and support for fail-over with persistence to disk. Our customers now have a correct, and consistent experience when using the product.
</p>

<p>
Some technology can really help you across a range of problem domains (I’ll blog about Cassandra for that in the future). But you should always be thinking (and testing!) about your choices, lest you end up using a shiny new hammer to solve problems that need a powerdrill.
</p>