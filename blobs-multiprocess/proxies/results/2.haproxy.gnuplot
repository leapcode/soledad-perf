#!/usr/bin/gnuplot

# Let's output to a jpeg file
set terminal jpeg size 800,600
# This sets the aspect ratio of the graph
set size 1, 1
# The file we'll write to
set output "2.haproxy.jpg"
# The graph title
set title "Response time for \"ab -c 50 -n 10000\" doing GET /blobs/user/ with haproxy"
# Where to place the legend/key
set key left top
# Draw gridlines oriented on the y axis
set grid y
# Specify that the x-series data is time data
#set xdata time
# Specify the *input* format of the time data
#set timefmt "%s"
# Specify the *output* format for the x-axis tick labels
#set format x "%S"
# Label the x-axis
set xlabel 'number of requests'
# Label the y-axis
set ylabel "response time (ms)"
# Tell gnuplot to use tabs as the delimiter instead of spaces (default)
set datafile separator '\t'
# Plot the data
#set offsets 1, 1, 2, 2
#set xrange [1516827928:1516827960]
set yrange [0:800]
plot "2.haproxy-1.tsv" every ::2 using 5 title 'haproxy, 1 process' with lines, \
  "2.haproxy-2.tsv" every ::2 using 5 title 'haproxy, 2 processes' with lines, \
  "2.haproxy-3.tsv" every ::2 using 5 title 'haproxy, 3 processes' with lines, \
  "2.haproxy-4.tsv" every ::2 using 5 title 'haproxy, 4 processes' with lines
