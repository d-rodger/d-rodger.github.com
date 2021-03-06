Title: Introducing Cassandra
Date: 2012-06-08 22:25
Category: Programming
Tags: cassandra, datastax, nosql, opscenter, Tim Berglund

<p><img align="top" alt="Cassandra Logo" height="131" src="images/cassandra_logo.png" width="200"/></p>

<p>Lately I&#8217;ve been trying out <a href="http://cassandra.apache.org/" 
title="Cassandra" target="_blank">Cassandra</a> @ work. Just recently I took a 
webinar that <a href="http://www.datastax.com/" title="DataStax" 
target="_blank">DataStax</a> hosted (the commercial company behind Cassandra), 
and conducted by Tim Berglund (<a href="https://twitter.com/#!/tlberglund" 
title="twitter" target="_blank">@tlberglund</a>). The webinars introduce 
Cassandra for developers and operations. A great way to get started 
understanding what Cassandra does, and doesn&#8217;t do. (Tim&#8217;s 
training videos on O&#8217;Reilly are excellent by the way).</p> 

<p>Cassandra is a schema-less, scalable, distributed database. There&#8217;s
actually more to it than that, but the list of it&#8217;s capabilities is rather
long :-). Surprisingly, it&#8217;s also relatively easy to setup. I found the
setup process simpler than earilier versions of MySQL, yet you get far more from
a brief configuration.</p>

<p><strong>Single node setup</strong></p>

<p>Setting up a single node of Cassandra is straight forward, but it is handy to
have some notes in one place, since there may be some additional files you need
to download if you want some of the features provided by the <a
href="http://www.datastax.com/products/opscenter" title="OpsCenter"
target="_blank">OpsCenter</a> package that DataStax makes available for
monitoring your Cassandra cluster. More about that later.</p>

<p>First, decide if you want the Apache version (no OpsCenter available with
this version) or the DataStax Community version. </p>

<p>Cassandra runs on the JVM, so make sure you have a version of the Java
runtime environment. I&#8217;ve tested with both Oracle Java 6 &amp; 7. The
OpenJDK is <strong>not</strong> recommended. One caveat about Java 7 below.</p>

<p>I&#8217;ll be using the DataStax Community edition, which at this time is
v1.1.0.</p>

<p>Once you&#8217;ve downloaded the version for your OS, go ahead and install
it. I&#8217;m using the tarball: dsc-cassandra-1.1.0-bin.tar.gz </p>

<p><span>Configuration</span><br/>Edit your <strong>conf/cassandra.yaml</strong>
file.<br/><br/><strong>initial_token</strong><br/>You can set this to 0 for a
single node, but read the notes below if you setup a cluster. </p>

<p><strong>directories</strong><br/>Decide where you want your data files,
commit log, and cache to be saved to. Needs to be a path you have permissions to
read/write. </p>

<p><strong>seeds, listen_address, rpc_address</strong><br/>You can leave these
as the defaults, but you&#8217;ll want to change these for cluster
configurations.</p>

<p><strong>Java 7</strong><br/>Depending on the version of Cassandra you are
running with Java 7, the initial amount of memory set for the stack space
appears to be too small. (it works fine with v1.1.0). However, if you run into
an error from the JVM about memory, change the following line in
<strong>conf/cassandra-env.sh</strong> (near line
153):<br/><em>JVM_OPTS=&#8221;$JVM_OPTS -Xss128k&#8221;</em> <br/>and change it
to<br/><em>JVM_OPTS=&#8221;$JVM_OPTS -Xss160k&#8221; <br/></em><br/>At this
point, you can go ahead and try running Cassandra:<br/><strong>bin/cassandra
-f</strong> <br/><br/>This will run it in the foreground, allowing you to see
any errors. <br/>If you scroll through the output, you will see two items not
available:<br/>&#8230;<br/>JNA not found. Native methods will be
disabled.<br/>&#8230;<br/>Will not load MX4J, mx4j-tools.jar is not in the
classpath </p>

<p>These features (JNA and mx4j) can be downloaded and installed to the
cassandra/lib path by getting them from:<br/><a
href="http://sourceforge.net/projects/mx4j/files/" target="_blank"><a
href="http://sourceforge.net/projects/mx4j/files/"
target="_blank">http://sourceforge.net/projects/mx4j/files/</a><br/></a><a
href="https://github.com/twall/jna" target="_blank"><a
href="https://github.com/twall/jna"
target="_blank">https://github.com/twall/jna</a></a> </p>

<p>You need the mx4j-tools.jar from the mx4j project.<br/>You need the jna.jar
and platform.jar for JNA support.<br/>Once you have the jar files copied, stop
and then restart Cassandra.</p>

<p>Assuming no errors, at this point you have a working Cassandra node. You can
go ahead and create a keyspace (database), and column families (tables).</p>

<p><strong>Cluster setup</strong></p>

<p>This is mostly a repeat of the single node setup. Install and configure
Cassandra on your other nodes, but this time you will be filling in the config
section for &#8216;seeds&#8217; by adding a few of the IPs from the other nodes.
This allows the nodes to start talking to each other, and learn the topology of
the network. You don&#8217;t need to include all the other nodes, just enough
for the cluster to start talking to itself.</p>

<p><strong>initial_token</strong><br/>You really want to set the inital_token
for <em>each</em> node you are installing to. As noted in the conf file, poorly
chosen tokens will lead to hotspots for your data. There is a site available for
generating tokens depending on the number of nodes you have <a
href="http://rickbranson.com/tokenguy.html" title="Token Guy"
target="_blank">here</a>.</p>

<p><strong>seeds</strong><br/>As mentioned above, you will want to add some of
the IP addresses of the other nodes (even if those nodes are simply running in a
virtual machine). Modify this line, and make sure the list of IPs is within the
quotes:<br/>seeds: &#8220;192.168.10.100, 192.168.10.101,
192.168.10.103&#8221;</p>

<p><strong>listen_address:</strong><br/>Set this to the local host IP address
(the address that you will be configuring some of the other nodes to talk
to).</p>

<p><strong>rpc_address:</strong><br/>I set this to the same IP as I&#8217;m
using for the listen_address - the local host IP. </p>

<p><br/><strong>Ready</strong><br/>At this point, the node is ready to become
part of a cluster. You will need to perform all of the single node and cluster
setup as described above on each node that you want as part of the cluster. Go
ahead and start up your Cassandra instances.</p>
<p><strong>OpsCenter</strong></p>
<p>Take a look at this:<img alt="opscenter" height="468"
src="images/opsc-multi-cluster.jpg"
width="900"/></p>
<p>Download the <a href="http://www.datastax.com/products/opscenter"
title="OpsCenter" target="_blank">OpsCenter</a>. This is pretty cool. The
OpsCenter is your dashboard, allowing you to setup, modify, observe and maintain
your Cassandra cluster.</p>

<p><strong>OpsCenter setup</strong></p>

<p>There are two parts to the OpsCenter, as far as configuration goes:<br/>The
OpsCenter itself<br/>The agent that sends data to the OpsCenter<br/><br/>You
only need the OpsCenter running on one server, but you need the agent running on
each node, so that it can feed information to the OpsCenter.</p>

<p><strong>conf/opscenterd.conf</strong><br/>Set the <em>interface</em> value to
your local host IP</p>

<p>I also turned off ssl, since I&#8217;m just setting this up as a test cluster
using several virtual machines, by adding this under [agents]:</p>

<p>[agents]<br/>use_ssl = false </p>
<p><strong>agent/conf/address.yaml</strong><br/>You can create this by running
the bin/setup program, but for a simple entry, you can just create it yourself.
One difference here, will be the &#8216;stomp_interface&#8217; - this is the IP
address of the server where you want to run the OpsCenter. The agents on all
nodes should be using the same OpsCenter IP address to talk to. Also note that
here also, I&#8217;ve turned off ssl.</p>

<p>stomp_interface: &#8220;192.168.10.100&#8221;<br/>use_ssl: 0</p>

<p>You will need to setup the agent configuration on each node.</p>

<p>Then run the agent:<br/><strong>agent/bin/opscenter-agent -f</strong></p>

<p>To turn on the OpsCenter:<br/><strong>bin/opscenter -f</strong></p>

<p>Then use your browser to connect to the IP address that you configured
OpsCenter to use, via port 8888.</p>

<p><br/>If all has gone well, at this point you have Cassandra and OpsCenter up
and running, and you can see your cluster. Time to start creating keyspaces
(databases) and column families (tables). Then look into CQL :-).</p>

<p>I also recommend the #cassandra channel on freenode for questions, and the
documentation on the DataStax site is extensive.</p>

<p>Hope this helps.</p>

