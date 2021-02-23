package main

import (
	"fmt"
)

func main() {
	var C int
	fmt.Scanf("%d", &C)
	for c := 0; c < C; c++ {
		var Ss string
		fmt.Scanf("%s", &Ss)

		S := make([]int, len(Ss))
		for i := 0; i < len(Ss); i++ {
			S[i] = int(Ss[i] - '0')
		}
		fmt.Println(solve(&S))
	}
}

func solve(Sp *[]int) int {
	S := *Sp
	dp := make([]int, len(S))
	dp[0] = 0
	dp[1] = 0
	dp[2] = d(Sp, 0, 3)
	dp[3] = d(Sp, 0, 4)
	dp[4] = d(Sp, 0, 5)
	for i := 5; i < len(S); i++ {
		res := 1234567890
		for j := max(2, i-5); j < i-2; j++ {
			res = min(res, dp[j]+d(Sp, j+1, i+1))
		}
		dp[i] = res
	}
	return dp[len(dp)-1]
}

func d(Sp *[]int, start int, end int) int {
	S := *Sp
	c1 := true
	c2 := true
	c3 := true
	c4 := true
	for i := start + 1; i < end; i++ {
		if S[i] != S[i-1] {
			c1 = false
		}
		if i > start+1 {
			if S[i-2]-S[i-1] != S[i-1]-S[i] {
				c2 = false
				c4 = false
			}
			if S[i-1]-S[i] != 1 && S[i-1]-S[i] != -1 {
				c2 = false
			}
			if S[i-2] != S[i] {
				c3 = false
			}
		}
	}
	if c1 {
		return 1
	}
	if c2 {
		return 2
	}
	if c3 {
		return 4
	}
	if c4 {
		return 5
	}
	return 10
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
