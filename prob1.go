package main

import "fmt"

func main(){
   suma := 0
   for i := 0 ; i < 1000 ; i++{
      if i % 3 == 0 || i % 5 == 0 { suma += i}
   }
   fmt.Println(suma)
}

// solved by iterating over everynumber, 
// can be optimised by using the formulae
// for arithmetic sequences addition also 
// can be improved by using multiple threads
//  for the for loop

