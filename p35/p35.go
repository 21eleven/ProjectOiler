package main

import ( 
	"fmt"
	"strconv"
	"math"
	"strings"
)

func Factorial(n uint64)(result uint64) {
	if (n>0) {
		result = n* Factorial(n-1)
		return result
	}
	return 1
}

var zeroAsZ = strings.NewReplacer("0", "z")
var zAsZero = strings.NewReplacer("z", "0")

func rotate(n string)(rotation string){
	s := n
	s = zeroAsZ.Replace(s)
	r :=string(s[0])
	s =s+r
	s =s[1:]
	return s
}
func isPrime(n int)(bool){
	if n == 2 {
		return true 
	} else if n < 2 {
		return false
	} else if n % 2 == 0 {
		return false
	}
	sqr := math.Sqrt(float64(n))
	isqr := int(math.Ceil(sqr))
	for i := 3; i<= isqr; i+=2 {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func main() {
	count :=1
	for i:=3; i<1000000; i++{
		rotation := strconv.Itoa(i)
		check := true
		for j:=0; j<len(rotation); j++{
			if strings.Contains(rotation,"0") || strings.Contains(rotation,"2") || strings.Contains(rotation,"4") || strings.Contains(rotation,"6") || strings.Contains(rotation,"8") {
				check = false
				break
			}
			rotation = rotate(rotation)
			rotation = zAsZero.Replace(rotation)
			rInt, _ := strconv.Atoi(rotation)
			if isPrime(rInt) == false {
				check = false
				break
			}
		}
		if check == true {
			count++
		}

	}
	fmt.Println(count)
}
