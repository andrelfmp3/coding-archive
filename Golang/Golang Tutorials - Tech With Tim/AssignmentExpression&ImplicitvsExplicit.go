package main // AssignmentExpression&ImplicitvsExplicit

import "fmt"

func main() {

	var x int // atribuição explícita / assignment expression. 
	fmt.Println(x) // zero
	x = 32 
	fmt.Println(x)

	y := 3 // atribuição implícita / implicit assignment. Declara e atribui.
	y = 4 // reatribui
	fmt.Println(y)

	// ======================================================================

	// atribuição multipla
	um, dois := 1, 2
	fmt.Println(um, dois)

	tres, quatro := 3, 4
	fmt.Println(tres, quatro)

	um, dois = tres, quatro // reatribui, explicito
		// um = tres
		// dois = quatro
	fmt.Println(um, dois)

	i, j := 1, 2
	j, k := 3, 4 // reatribui j e cria K
	fmt.Println(i, j, k)

	// ======================================================================
	var number uint = 261 // only positive numbers
	number = number + 1
	fmt.Println(number)

	var number2 = 2 // qual tipo?
	number2 = number2 + 1
	fmt.Println(number2)
	fmt.Printf("Type of number2 is %T\n", number2)

	var number3 = 1.3
	fmt.Println(number3)

	var number4 = 4  // implicit conversion
	fmt.Println(number4)

	var number5 string = "srtstr"
	number5 = "str" // implicit conversion
	fmt.Println(number5)

	var number6 bool
	number6 = false
	fmt.Println(number6)

	var number7 uint64
	fmt.Println(number7)

}
