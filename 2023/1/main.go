package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
	"unicode"
)

func ReadInput() (inputs []string) {
	file, err := os.Open("input.txt")
	// file, err := os.Open("testinput.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		inputs = append(inputs, scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		panic(err)
	}

	return
}

func DecodeCalibrationP1(encodedCalibration string) (calibration int64) {
	var firstNum string
	var lastNum string
	digitRegex := regexp.MustCompile(`(\d)`)

	matches := digitRegex.FindAllString(encodedCalibration, -1)
	if len(matches) > 0 {
		firstNum = matches[0]
		lastNum = matches[len(matches)-1]
	}

	calibration, _ = strconv.ParseInt(firstNum+lastNum, 10, 32)
	return
}

func DecodeCalibrationP2(encodedCalibration string) (calibration int64) {
	var firstNum string
	var lastNum string

	toSkip := 0
	for idx := range encodedCalibration {
		if toSkip != 0 {
			toSkip--
			continue
		}
		var digit string
		digit, toSkip = GetDigit(encodedCalibration[idx:])
		if digit != "" {
			if firstNum == "" {
				firstNum = digit
			}
			lastNum = digit
		}
	}

	calibration, _ = strconv.ParseInt(firstNum+lastNum, 10, 32)
	return
}

func GetDigit(inputString string) (digit string, toSkip int) {
	if unicode.IsDigit(rune(inputString[0])) {
		digit = string(inputString[0])
		toSkip = 0
		return
	}
	lookupTable := map[string]string{
		"one":   "1",
		"two":   "2",
		"three": "3",
		"four":  "4",
		"five":  "5",
		"six":   "6",
		"seven": "7",
		"eight": "8",
		"nine":  "9",
	}

	for key, value := range lookupTable {
		if strings.HasPrefix(inputString, key) {
			digit = value
			toSkip = len(key) - 2
			return
		}
	}
	return
}

func main() {
	inputs := ReadInput()
	decodedCalibrations := make([]int64, 0)
	sum := 0

	// P1
	// for _, encodedCalibration := range inputs {
	// 	decodedCalibrations = append(decodedCalibrations, decodeCalibrationP1(encodedCalibration))
	// }

	// P2
	for _, encodedCalibration := range inputs {
		decodedCalibrations = append(decodedCalibrations, DecodeCalibrationP2(encodedCalibration))
	}

	for _, calibration := range decodedCalibrations {
		sum = sum + int(calibration)
	}
	fmt.Println(sum)
}
