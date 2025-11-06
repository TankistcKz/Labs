package main

import (
	"errors"
	"fmt"
)

type BankAccount struct {
    owner   string
    balance float64
}

func (acc *BankAccount) Deposit(amount float64) error {
    if amount <= 0 {
        return errors.New("сумма должна быть положительной")
    }
    acc.balance += amount
    return nil
}

func (acc *BankAccount) Withdraw(amount float64) error {
    if amount <= 0 {
        return errors.New("сумма должна быть положительной")
    }
    if amount > acc.balance {
        return errors.New("недостаточно средств")
    }
    acc.balance -= amount
    return nil
}

func (acc BankAccount) GetBalance() float64 {
    return acc.balance
}

func (acc BankAccount) PrintInfo() {
    fmt.Printf("Владелец счёта: %s\n", acc.owner)
    fmt.Printf("Текущий баланс: %.2f\n", acc.GetBalance())
}

func main() {
    account := BankAccount{
        owner:   "Саня Ишаков",
        balance: 1000.00,
    }

    account.PrintInfo()

    err := account.Deposit(500)
    if err != nil {
        fmt.Println("Ошибка пополнения:", err)
    } else {
        fmt.Println("Счёт успешно пополнен на 500")
    }

    err = account.Withdraw(200)
    if err != nil {
        fmt.Println("Ошибка снятия:", err)
    } else {
        fmt.Println("Со счёта снято 200")
    }

    err = account.Withdraw(3000)
    if err != nil {
        fmt.Println("Ошибка снятия:", err)
    }

    account.PrintInfo()
}