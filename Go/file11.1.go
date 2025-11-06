package main

import "fmt"

type Engine struct {
    Type        string
    Power       int
    Volume      float64
    IsTurbo     bool
}

type Car struct {
    Make        string
    Model       string
    Year        int
    EngineInfo  Engine
}

func NewCar(make, model string, year int, engineType string, power int, volume float64, isTurbo bool) Car {
    return Car{
        Make:   make,
        Model:  model,
        Year:   year,
        EngineInfo: Engine{
            Type:    engineType,
            Power:   power,
            Volume:  volume,
            IsTurbo: isTurbo,
        },
    }
}

func (c Car) PrintInfo() {
    fmt.Printf("Автомобиль: %s %s (%d год)\n", c.Make, c.Model, c.Year)
    fmt.Printf("Двигатель: %s, %.1f л\n", c.EngineInfo.Type, c.EngineInfo.Volume)
    fmt.Printf("Мощность: %d л.с.\n", c.EngineInfo.Power)
    if c.EngineInfo.IsTurbo {
        fmt.Println("Турбонаддув: есть")
    } else {
        fmt.Println("Турбонаддув: нет")
    }
}

func (c *Car) UpgradeEngine(newPower int, newVolume float64, addTurbo bool) {
    c.EngineInfo.Power = newPower
    c.EngineInfo.Volume = newVolume
    c.EngineInfo.IsTurbo = addTurbo
    fmt.Printf("Двигатель %s %s модернизирован\n", c.Make, c.Model)
}

func main() {
    car := NewCar("Daimler-Benz", "Sonderkraftfahrzeug 142", 1940, "Бензиновый", 200, 11, false)
    car.PrintInfo()
    car.UpgradeEngine(330, 12, true)
    car.PrintInfo()
}