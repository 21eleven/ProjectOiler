package main

import "fmt"

func main() {
	var fib [50]int
	var sum int
	fib[1]= 1
	fib[2]= 2
	for i:=3; i < 50; i++ {
		fib[i] = fib[i-2] + fib[i-1]
	}
	for i:=0; i <50; i++ {
		if (fib[i] % 2 == 0) && (fib[i] < 4000000){
			sum+=fib[i]
		}
	}
	fmt.Println(sum)
}

