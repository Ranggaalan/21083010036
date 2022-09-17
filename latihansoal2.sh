#!/bin/bash

echo "Kalkulator Sederhana dengan Linux Bash"

echo -n "x :"
read x
echo -n "y :"
read y

let jumlah=$x+$y
let kali=$x*$y
let pangkat=$x**$y
let mod=$x%$y
let kurang=$x-$y

echo -n "Masukkan operasi aritmatika  yang ingin kamu pilih: "
read pilih

if [ $pilih == jumlah ]
then
	echo "x+y=$jumlah"
elif [ $pilih  == kali ]
then
	echo "x*y=$kali"
elif [ $pilih == pangkat ]
then 
	echo "x**y=$pangkat"
elif [ $pilih == mod ]
then 
	echo "x%y=$mod"
elif [ $pilih == kurang ]
then 
	echo "x-y=$kurang"
else
	echo "Operasi anda tidak ada dalam kalkulator kami, silahkan pilih operasi lainnya"
fi
