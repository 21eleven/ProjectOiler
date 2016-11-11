package main

import ( "fmt" )


func main() {
	var sumN = 0
	count := 1
	for count <1000 {
		if count % 3 == 0  {
			sumN += count
		} else if count % 5 == 0 {
			sumN += count
		}
	
	count++
	}
	fmt.Println(sumN)
}
