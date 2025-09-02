package main

import "fmt"

func main() { // more than one main not allowerd (run, but not build)

	fmt.Println("Hello Word")

	// var name type
	var name string = "golang" // sem numero no começo, sem espaço. apenas letras caracteres e numeros. sem keywords (func, main, var, import)

	var name2 string
	name2 = name + " tutorial"
	fmt.Println(name2)

	name2 = "go tutorial"
	fmt.Println(name2)

	// types
	// signet integeger (can be negative) - uint8 = -128 p 127
	var test1 int = -128
	fmt.Println("Number:", test1)
	// unsignet integeger (can not be negative) 0 - uint8 = 0 p 255
	// int8, int16, int32, int64
	var test2 uint8 = 255
	fmt.Println("Number 2:", test2)

	// machine dependet types
	// uint int (32 or 64)

	// float32, float64
	var testFloat float32 = 1.5
	fmt.Println("Test float:", testFloat)

	// string
	var testString string = "this is a test string"
	fmt.Println("Test string:", testString)

	// bool - true or false
	var testBool bool = false
	fmt.Println("Test boolean:", testBool)

	// complex64, complex128
	var testComplex complex64 = 1 + 2i
	fmt.Println("Test complex:", testComplex)

}
