#!/usr/bin/gnuplot

infile="$0"
outfile="$1"

# maybe save image file
if (outfile ne '') \
  set term png size 1000,400; \
  set output "./out/sync-stats.png"

# make the graph beautiful
set title 'Soledad Sync Phases'
set xtics 10
set ytics 50
set grid
set key outside

# plot!
plot for [col=2:6] infile using 1:col with linespoints title columnheader

# pause when not saving image file
if (outfile eq '') \
  pause -1
