#!bin/bash
set term jpeg
unset key
set size square
set size 0.7,1.0
set title 'Rys. 1. u(x,t) dla sztywnych warunków brzegowych z wymuszeniem'
set ylabel 't[s]'
set xlabel 'x'
# set cbrange [-1:1];
set yrange [0:10];
set out '../plots/zad.jpg'
set view map
set datafile separator ","
set palette defined (-1'blue',0'white',1'red')
splot '../data/ex3.csv' u 1:2:3 w pm3d
