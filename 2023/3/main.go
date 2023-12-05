package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"unicode"
)

type Position struct {
	Row int
	Col int
}

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
				if num != "" {
					isValid = true
					parsedNum, _ := strconv.ParseInt(num, 10, 64)
					sum += parsedNum
					isValid = false
					num = ""
				}
			} else {
				if isValid {
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

func GetGears(engineSchematic []string) (gearPositions []Position) {
	for rowNum, row := range engineSchematic {
		for colNum, char := range row {
			if char == '*' {
				gearPositions = append(gearPositions, Position{Row: rowNum, Col: colNum})
			}
		}
	}
	return
}

func GetGearNumPositions(gearPosition Position, engineSchematic []string) (numPositions []Position) {
	tempIsValid := false
	isTop := false
	isBottom := false

	// LEFT
	if gearPosition.Col != 0 && unicode.IsDigit(rune(engineSchematic[gearPosition.Row][gearPosition.Col-1])) {
		tempIsValid = true
		numPositions = append(numPositions, Position{Row: gearPosition.Row, Col: gearPosition.Col - 1})
	}
	// RIGHT
	if gearPosition.Col != 0 && unicode.IsDigit(rune(engineSchematic[gearPosition.Row][gearPosition.Col+1])) {
		if tempIsValid {
			numPositions = append(numPositions, Position{Row: gearPosition.Row, Col: gearPosition.Col + 1})
			return
		} else {
			tempIsValid = true
			numPositions = append(numPositions, Position{Row: gearPosition.Row, Col: gearPosition.Col + 1})
		}
	}
	// TOP
	if gearPosition.Row != 0 && unicode.IsDigit(rune(engineSchematic[gearPosition.Row-1][gearPosition.Col])) {
		if tempIsValid {
			numPositions = append(numPositions, Position{Row: gearPosition.Row - 1, Col: gearPosition.Col})
			return
		} else {
			tempIsValid = true
			isTop = true
			numPositions = append(numPositions, Position{Row: gearPosition.Row - 1, Col: gearPosition.Col})
		}
	}
	// BOTTOM
	if gearPosition.Row < len(engineSchematic)-1 && unicode.IsDigit(rune(engineSchematic[gearPosition.Row+1][gearPosition.Col])) {
		if tempIsValid {
			numPositions = append(numPositions, Position{Row: gearPosition.Row + 1, Col: gearPosition.Col})
			return
		} else {
			tempIsValid = true
			isBottom = true
			numPositions = append(numPositions, Position{Row: gearPosition.Row + 1, Col: gearPosition.Col})
		}
	}
	// DIAGONAL TOP RIGHT
	if gearPosition.Row != 0 && gearPosition.Col < len(engineSchematic[gearPosition.Row])-1 && unicode.IsDigit(rune(engineSchematic[gearPosition.Row-1][gearPosition.Col+1])) {
		if tempIsValid && !isTop {
			numPositions = append(numPositions, Position{Row: gearPosition.Row - 1, Col: gearPosition.Col + 1})
			return
		} else if !tempIsValid {
			tempIsValid = true
			numPositions = append(numPositions, Position{Row: gearPosition.Row - 1, Col: gearPosition.Col + 1})
		}
	}
	// DIAGONAL TOP LEFT
	if gearPosition.Row != 0 && gearPosition.Col != 0 && unicode.IsDigit(rune(engineSchematic[gearPosition.Row-1][gearPosition.Col-1])) {
		if tempIsValid && !isTop {
			numPositions = append(numPositions, Position{Row: gearPosition.Row - 1, Col: gearPosition.Col - 1})
			return
		} else if !tempIsValid {
			tempIsValid = true
			numPositions = append(numPositions, Position{Row: gearPosition.Row - 1, Col: gearPosition.Col - 1})
		}
	}
	// DIAGONAL BOTTOM RIGHT
	if gearPosition.Row < len(engineSchematic)-1 && gearPosition.Col != 0 && unicode.IsDigit(rune(engineSchematic[gearPosition.Row+1][gearPosition.Col-1])) {
		if tempIsValid && !isBottom {
			numPositions = append(numPositions, Position{Row: gearPosition.Row + 1, Col: gearPosition.Col - 1})
			return
		} else if !tempIsValid {
			tempIsValid = true
			numPositions = append(numPositions, Position{Row: gearPosition.Row + 1, Col: gearPosition.Col - 1})
		}
	}
	// DIAGONAL BOTTOM LEFT
	if gearPosition.Row < len(engineSchematic)-1 && gearPosition.Col < len(engineSchematic[gearPosition.Row])-1 && unicode.IsDigit(rune(engineSchematic[gearPosition.Row+1][gearPosition.Col+1])) {
		if tempIsValid && !isBottom {
			numPositions = append(numPositions, Position{Row: gearPosition.Row + 1, Col: gearPosition.Col + 1})
			return
		}
	}
	return
}

func GetGearRatio(validGearNumPositions []Position, engineSchematic []string) (gearRatio int64) {
	gearRatio = 1
	for _, numPosition := range validGearNumPositions {
		numLeftLimit := numPosition.Col
		numRightLimit := numPosition.Col
		// Scan Left till no digit
		for {
			if numLeftLimit >= len(engineSchematic[numPosition.Row]) || !unicode.IsDigit(rune(engineSchematic[numPosition.Row][numLeftLimit])) {
				break
			}
			numLeftLimit = numLeftLimit + 1
		}

		// Scan Right till no digit
		for {
			if numRightLimit < 0 || !unicode.IsDigit(rune(engineSchematic[numPosition.Row][numRightLimit])) {
				break
			}
			numRightLimit = numRightLimit - 1
		}
		parsedNum, _ := strconv.ParseInt(string(engineSchematic[numPosition.Row][numRightLimit+1:numLeftLimit]), 10, 64)
		gearRatio = gearRatio * parsedNum
	}
	return
}

func ProcessEngineSchematicForGearRatioSum(engineSchematic []string) (sum int64) {
	gears := GetGears(engineSchematic)

	for _, gear := range gears {
		numPositions := GetGearNumPositions(gear, engineSchematic)
		if len(numPositions) == 2 {
			sum += GetGearRatio(numPositions, engineSchematic)
		}
	}
	return
}

func main() {
	input := readInput()

	// P1
	// sum := SumValidNum(input)
	// fmt.Println(sum)

	// P2
	sum := ProcessEngineSchematicForGearRatioSum(input)
	fmt.Println(sum)

}
