package main

import (
    "fmt"
    "sync"
    )

func main(){
    var wg sync.WaitGroup
    suma := 0
    for i := 0 ; i < 1000 ; i++{
        wg.Add(1)
        go func(index int){
            defer wg.Done()
             if index % 3 == 0 || index % 5 == 0 { suma += index }
        }(i)

         
    }

    wg.Wait()

    fmt.Println(suma)
}

// solved by iterating over everynumber, 
// can be optimised by using the formulae
// for arithmetic sequences addition also 
// can be improved by using multiple threads
//  for the for loop

