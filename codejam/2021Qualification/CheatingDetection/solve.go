package main

import (
	"fmt"
	"math"
)

func main() {
	var T int
	fmt.Scanf("%d", &T)
	for t := 0; t < T; t++ {
		var P int
		fmt.Scanf("%d", &P)
		scores := make([][]int, 100)
		for i := 0; i < 100; i++ {
			scores[i] = make([]int, 10000)
			var score string
			fmt.Scanf("%s", &score)
			for j, c := range score {
				scores[i][j] = int(c - '0')
			}
		}
		// fmt.Println(scores)

		pQ := make([]float64, 10000)
		for i := 0; i < 100; i++ {
			sumScore := 0.0
			for j := 0; j < 10000; j++ {
				sumScore += float64(scores[i][j])
			}
			pQ[i] = sumScore / 100
		}

		pS := make([]float64, 100)
		for i := 0; i < 100; i++ {
			for j := 0; j < 10000; j++ {
				pS[i] += float64(scores[i][j])
			}
			pS[i] /= 10000
		}

		sus := make([]float64, 100)
		for i := 0; i < 100; i++ {
			for j := 0; j < 100; j++ {
				prob := pQ[j] * pS[i]
				sus[i] += math.Pow(10, math.Abs(float64(scores[i][j])-prob))
			}
		}

		maxSus := sus[0]
		res := 0
		for i := 1; i < 100; i++ {
			if maxSus < sus[i] {
				maxSus = sus[i]
				res = i
			}
		}

		fmt.Printf("Case #%d: %d\n", t+1, res+1)
	}
}
