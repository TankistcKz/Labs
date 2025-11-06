package main

import "fmt"

type Transport interface {
	Move()
	Stop()
}

type Car struct {
	Model string
}

func (c Car) Move() {
	fmt.Printf("Автомобиль %s начал движение\n", c.Model)
}

func (c Car) Stop() {
	fmt.Printf("Автомобиль %s остановился\n", c.Model)
}

type Bicycle struct {
	Type string
}

func (b Bicycle) Move() {
	fmt.Printf("Велосипед типа %s поехал\n", b.Type)
}

func (b Bicycle) Stop() {
	fmt.Printf("Велосипед типа %s остановился\n", b.Type)
}

type Train struct {
	Number int
}

func (t Train) Move() {
	fmt.Printf("Поезд №%d отправился\n", t.Number)
}

func (t Train) Stop() {
	fmt.Printf("Поезд №%d прибыл на станцию\n", t.Number)
}

func TestTransport(t Transport) {
	t.Move()
	t.Stop()
}

func main() {
	car := Car{Model: "Panzerkampfwagen V Panther"}
	bike := Bicycle{Type: "гравийный"}
	train := Train{Number: 52}

	TestTransport(car)
	TestTransport(bike)
	TestTransport(train)
}