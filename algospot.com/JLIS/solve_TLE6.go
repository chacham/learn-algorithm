package main

import "fmt"

func main() {
	var C int
	fmt.Scanf("%d", &C)
	for c := 0; c < C; c++ {
		var N, M int
		var A = []int{}
		var B = []int{}

		fmt.Scanf("%d %d", &N, &M)

		for i := 0; i < N; i++ {
			var tmp int
			fmt.Scanf("%d", &tmp)
			A = append(A, tmp)
		}
		for i := 0; i < M; i++ {
			var tmp int
			fmt.Scanf("%d", &tmp)
			B = append(B, tmp)
		}

		fmt.Println(jlis(N, M, &A, &B))
	}
}

func jlis(N int, M int, Ap *[]int, Bp *[]int) int {
	A := *Ap
	B := *Bp
	dpLis := make(map[p]int)
	dpVal := make(map[p]int)
	dpLis[p{-1, -1}] = 0
	dpVal[p{-1, -1}] = 0
	for i := 0; i < N; i++ {
		maxLisBf := 0
		for j := 0; j < i; j++ {
			if A[i] > A[j] && dpLis[p{j, -1}] > maxLisBf {
				maxLisBf = dpLis[p{j, -1}]
			}
		}
		dpLis[p{i, -1}] = maxLisBf + 1
		dpVal[p{i, -1}] = A[i]
	}
	for i := 0; i < M; i++ {
		maxLisBf := 0
		for j := 0; j < i; j++ {
			if B[i] > B[j] && dpLis[p{-1, j}] > maxLisBf {
				maxLisBf = dpLis[p{-1, j}]
			}
		}
		dpLis[p{-1, i}] = maxLisBf + 1
		dpVal[p{-1, i}] = B[i]
	}

	for R := 0; R < N; R++ {
		for C := 0; C < M; C++ {
			maxLisBf := 0
			maxValCur := max(A[R], B[C])
			current := p{R, C}
			for r := -1; r < R; r++ {
				before := p{r, C}
				if dpLis[before] > maxLisBf && dpVal[before] < maxValCur {
					maxLisBf = dpLis[before]
				}
			}
			for c := -1; c < C; c++ {
				before := p{R, c}
				if dpLis[before] > maxLisBf && dpVal[before] < maxValCur {
					maxLisBf = dpLis[before]
				}
			}
			dpLis[current] = maxLisBf + 1
			dpVal[current] = maxValCur
		}
	}

	lis := -1
	for r := -1; r < N; r++ {
		for c := -1; c < M; c++ {
			lis = max(lis, dpLis[p{r, c}])
		}
	}
	return lis
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

type p struct {
	x, y int
}
