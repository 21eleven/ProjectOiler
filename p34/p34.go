package main

import ( 
	"fmt"
	"strconv"
)

func Factorial(n uint64)(result uint64) {
	if (n>0) {
		result = n* Factorial(n-1)
		return result
	}
	return 1
}

func main() {
	sum:=0
	x:=0
	var a = make([]int, 4, 100)
	for i:=3; i<1000000; i++{
		s := strconv.Itoa(i)
		sumFact:=0
		for c:=0; c<len(s); c++{
			digit, _ := strconv.Atoi(string(s[c]))
			sumFact+=int(Factorial(uint64(digit)))
		}
		if (sumFact==i) {
			a[x]=i
			x++
		}

	}
	for _, y := range(a) {
		sum+=y
	}
	fmt.Println(sum)
}
