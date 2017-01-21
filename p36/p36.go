package main

import ( 
	"strconv"
)

func Palindrome(str string)(bool) {
	l := len(str)
	if l == 1 {
		return true
	} else {
		check := true
		if l % 2 == 0 {
			for i:=0; i<l/2; i++{
				if str[i] != str[l-1-i]{
					check = false
				}
			}
		} else {
			for i:=0; i<(l-1)/2; i++{
				if str[i] != str[l-1-i]{
					check = false
				}
			}
		}
		return check
	}
}

func main() {
	sum:=0
	x:=0
	var a = make([]int, 100, 100)
	for i:=1; i<1000001; i++{
		s := strconv.Itoa(i)
		b := strconv.FormatInt(int64(i), 2)
		if Palindrome(s) == true && Palindrome(b) == true {
			a[x] = i
			x++
		}
	}
	for _, y := range(a) {
		sum+=y
	}
	println(sum)
}
