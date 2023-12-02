package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Color string

const (
	Red   Color = "red"
	Green Color = "green"
	Blue  Color = "blue"
)

type Game struct {
	Id         int64
	GameRounds []GameRound
}

type GameRound struct {
	GameRoundPicks []GameRoundPick
}

type GameRoundPick struct {
	NumOfCubes int64
	Color      Color
}

func readInput() (input []string) {
	file, err := os.Open("input.txt")
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

func ParseGames(rawGames []string) (games []Game) {
	for _, rawGame := range rawGames {
		var tempGame Game
		gameIdRoundsSplit := strings.Split(rawGame, ":")
		tempGame.Id, _ = strconv.ParseInt(strings.Fields(gameIdRoundsSplit[0])[1], 10, 64)
		for _, gameRound := range strings.Split(gameIdRoundsSplit[1], ";") {
			var tempGameRound GameRound
			for _, gameRoundPick := range strings.Split(gameRound, ",") {
				var tempGameRoundPick GameRoundPick
				gameRoundPickSplit := strings.Fields(gameRoundPick)
				tempGameRoundPick.Color = Color(gameRoundPickSplit[1])
				tempGameRoundPick.NumOfCubes, _ = strconv.ParseInt(gameRoundPickSplit[0], 10, 64)
				tempGameRound.GameRoundPicks = append(tempGameRound.GameRoundPicks, tempGameRoundPick)
			}
			tempGame.GameRounds = append(tempGame.GameRounds, tempGameRound)
		}
		games = append(games, tempGame)
	}
	return
}

func GetValidGames(games []Game, constraint map[Color]int64) (validGames []Game) {
out:
	for _, game := range games {
		for _, gameRound := range game.GameRounds {
			for _, gameRoundPick := range gameRound.GameRoundPicks {
				if constraint[gameRoundPick.Color] < gameRoundPick.NumOfCubes {
					fmt.Println(gameRoundPick)
					continue out
				}
			}
		}
		validGames = append(validGames, game)
	}
	return
}

func SumValidGamesIds(games []Game) (sum int64) {
	for _, game := range games {
		sum = sum + game.Id
	}
	return
}

func GetPowersOfGames(games []Game) (powers []int64) {
	for _, game := range games {
		maxColorNumCubes := make(map[Color]int64, 0)
		maxColorNumCubes[Red] = 0
		maxColorNumCubes[Green] = 0
		maxColorNumCubes[Blue] = 0
		for _, gameRound := range game.GameRounds {
			for _, gameRoundPick := range gameRound.GameRoundPicks {
				if maxColorNumCubes[gameRoundPick.Color] < gameRoundPick.NumOfCubes {
					maxColorNumCubes[gameRoundPick.Color] = gameRoundPick.NumOfCubes
				}
			}
		}
		powers = append(powers, maxColorNumCubes[Red]*maxColorNumCubes[Green]*maxColorNumCubes[Blue])
	}
	return
}

func sum(nums []int64) (sum int64) {
	for _, num := range nums {
		sum += num
	}
	return
}

func main() {
	input := readInput()

	games := ParseGames(input)

	// P1
	// constraint := make(map[Color]int64, 0)
	// constraint[Red] = 12
	// constraint[Green] = 13
	// constraint[Blue] = 14
	// validGames := GetValidGames(games, constraint)
	// sum := SumValidGamesIds(validGames)
	// fmt.Println(sum)

	// P2
	powers := GetPowersOfGames(games)
	fmt.Println(sum(powers))

}
