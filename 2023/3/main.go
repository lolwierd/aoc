package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"unicode"
)

func readInput() (input []string) {
	file, err := os.Open("input.txt")
	// file, err := os.Open("testinput.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		input = append(input, scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		panic(err)
	}

	return
}

func SumValidNum(engineSchematic []string) (sum int64) {
	isValid := false
	num := ""
	for rowNum, row := range engineSchematic {
		for colNum, char := range row {
			if unicode.IsDigit(char) {
				num += string(char)
			} else if isSymbol(char) {
				fmt.Println(string(char))
				if num != "" {
					fmt.Println("IsValidAfterSym ", num)
					isValid = true
					parsedNum, _ := strconv.ParseInt(num, 10, 64)
					sum += parsedNum
					isValid = false
					num = ""
				}
			} else {
				if isValid {
					fmt.Println("IsValid ", num)
					parsedNum, _ := strconv.ParseInt(num, 10, 64)
					sum += parsedNum
					isValid = false
					num = ""
				} else {
					isValid = false
					num = ""
				}
			}
			if isValid || num == "" {
				continue
			}
			// LEFT
			if colNum != 0 && isSymbol(rune(engineSchematic[rowNum][colNum-1])) {
				isValid = true
				continue
			}
			// TOP
			if rowNum != 0 && isSymbol(rune(engineSchematic[rowNum-1][colNum])) {
				isValid = true
				continue
			}
			// BOTTOM
			if rowNum < len(engineSchematic)-1 && isSymbol(rune(engineSchematic[rowNum+1][colNum])) {
				isValid = true
				continue
			}

			// DIAGONAL TOP RIGHT
			if rowNum != 0 && colNum < len(row)-1 && isSymbol(rune(engineSchematic[rowNum-1][colNum+1])) {
				isValid = true
				continue
			}

			// DIAGONAL TOP LEFT
			if rowNum != 0 && colNum != 0 && isSymbol(rune(engineSchematic[rowNum-1][colNum-1])) {
				isValid = true
				continue
			}

			// DIAGONAL BOTTOM RIGHT
			if rowNum < len(engineSchematic)-1 && colNum != 0 && isSymbol(rune(engineSchematic[rowNum+1][colNum-1])) {
				isValid = true
				continue
			}

			// DIAGONAL BOTTOM LEFT
			if rowNum < len(engineSchematic)-1 && colNum < len(row)-1 && isSymbol(rune(engineSchematic[rowNum+1][colNum+1])) {
				isValid = true
			}
		}
	}
	return
}

func isSymbol(char rune) bool {
	return !(unicode.IsDigit(char)) && string(char) != "."
}

func main() {
	input := readInput()

	sum := SumValidNum(input)
	fmt.Println(sum)
}
