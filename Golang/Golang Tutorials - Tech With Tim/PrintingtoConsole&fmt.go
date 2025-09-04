package main

import "fmt"

func main() {

	fmt.Printf("Type of 10: %T\n", 10) // sprint?
	fmt.Printf("Value of 10: %v\n", 10)
	fmt.Printf("Using %%T and %%v\n") // %% = %

	fmt.Printf("%t\n\n", true)

	// integer
	fmt.Println("Print 100: ")
	fmt.Printf("%b ", 100) // binaru
	fmt.Printf("%o ", 100) // octal
	fmt.Printf("%d ", 100) // dec
	fmt.Printf("%x ", 100) // hex

	// floating
	fmt.Println("Print 10,10: ")
	fmt.Printf("%e ", 10.10) // scientific
	fmt.Printf("%f ", 10.10) // decimal
	fmt.Printf("%g ", 10.10) // general

	// string
	fmt.Println("\nPrint string: ")
	fmt.Printf("%s ", "Hello") // string
	fmt.Printf("%q ", "Hello") //"string"

	// padding - %espaçamento.precisão
	fmt.Println("\nPadding: ")
	fmt.Printf("%6d\n", 12)
	fmt.Printf("%-6d", 12)
	fmt.Print("x\n")
	fmt.Printf("%6.2d\n", 12) // pad to width 6, precision 2
	fmt.Printf("%6.2f\n", 12.111111)

	fmt.Printf("%6.3s\n", "Hello") // only first 3 characters
	fmt.Printf("%08d\n", 12)

	var test string = fmt.Sprintf("The number is number %2.3f\n", 1333.3)
	fmt.Printf(test)

}
