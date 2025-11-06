package main

import "fmt"

func main() {
    var i int = -42
    var i8 int8 = -128
    var i16 int16 = -32768
    var i32 int32 = -2147483648
    var r rune = 'Я'
    var i64 int64 = -9223372036854775808
    
    var ui uint = 42
    var ui8 uint8 = 255
    var ui16 uint16 = 65535
    var ui32 uint32 = 4294967295
    var ui64 uint64 = 18446744073709551615
    var uiptr uintptr = 0xc82000c290
    
    var f32 float32 = 3.14
    var f64 float64 = 3.141592653589793
    
    var c64 complex64 = 1 + 2i
    var c128 complex128 = 1 + 2i
    
    var b byte = 'A' 
    var s string = "Hello, world!"

    var boolean bool = true
    
    fmt.Println("Целые числа:", i, i8, i16, i32, r, i64)
    fmt.Println("Беззнаковые целые:", ui, ui8, ui16, ui32, ui64, uiptr)
    fmt.Println("Числа с плавающей точкой:", f32, f64)
    fmt.Println("Комплексные числа:", c64, c128)
    fmt.Println("Байт и строка:", b, s)
    fmt.Println("Логическое значение:", boolean)
}