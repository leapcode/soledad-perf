#!/usr/bin/gnuplot

# Let's output to a jpeg file
set terminal jpeg size 1024,768
# This sets the aspect ratio of the graph
set size 1, 1
# The file we'll write to
set output "all-freq.jpg"
# The graph title
set title "Response time for \"ab -c 50 -n 10000\" doing GET /blobs/user/ in different scenarios"
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
set xlabel 'response time'
# Label the y-axis
set ylabel "frequency"
# Tell gnuplot to use tabs as the delimiter instead of spaces (default)
set datafile separator '\t'
# Plot the data
#set offsets 1, 1, 2, 2
#set xrange [1516827928:1516827960]
#set yrange [0:800]

n=50 #number of intervals
max=752. #max value
min=2. #min value
width=(max-min)/n #interval width
#function used to map a value to the intervals
hist(x)=width*floor(x/width)+width/2.0
set xrange [min:200]
set yrange [0:]
set offset graph 0.05,0.05,0.05,0.0
set xtics min,(max-min)/5,max
#set boxwidth width*0.9
set style fill empty #0.5 #fillstyle
set tics out nomirror

plot "noproxy-1.tsv" every ::2 using (hist($5)):(1) title 'noproxy, 1 process' smooth frequency with linespoints, \
  "noproxy-2.tsv" every ::2 using (hist($5)):(1) title 'noproxy, 2 processes' smooth frequency with linespoints, \
  "noproxy-3.tsv" every ::2 using(hist($5)):(1) title 'noproxy, 3 processes' smooth frequency with linespoints, \
  "noproxy-4.tsv" every ::2 using(hist($5)):(1) title 'noproxy, 4 processes' smooth frequency with linespoints, \
  "haproxy-1.tsv" every ::2 using(hist($5)):(1) title 'haproxy, 1 process' smooth frequency with linespoints, \
  "haproxy-2.tsv" every ::2 using(hist($5)):(1) title 'haproxy, 2 processes' smooth frequency with linespoints, \
  "haproxy-3.tsv" every ::2 using(hist($5)):(1) title 'haproxy, 3 processes' smooth frequency with linespoints, \
  "haproxy-4.tsv" every ::2 using(hist($5)):(1) title 'haproxy, 4 processes' smooth frequency with linespoints, \
  "pyproxy-1.tsv" every ::2 using(hist($5)):(1) title 'pyproxy, 1 process' smooth frequency with linespoints, \
  "pyproxy-2.tsv" every ::2 using(hist($5)):(1) title 'pyproxy, 2 processes' smooth frequency with linespoints, \
  "pyproxy-3.tsv" every ::2 using(hist($5)):(1) title 'pyproxy, 3 processes' smooth frequency with linespoints, \
  "pyproxy-4.tsv" every ::2 using(hist($5)):(1) title 'pyproxy, 4 processes' smooth frequency with linespoints
