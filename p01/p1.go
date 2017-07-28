/*
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
*/

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
