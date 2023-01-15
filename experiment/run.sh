#!/bin/bash

echo "**** intialize"

rm experiment/main.dat
rm experiment/test.dat

echo "**** compile code"

cc experiment/prototype.c -o experiment/prototype

echo "**** execute test - 5 to 10 minutes "

./experiment/prototype

echo "**** graph the data "

gnuplot experiment/plot1
gnuplot experiment/plot2
gnuplot experiment/plot3

echo "**** complete "
