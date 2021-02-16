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
	dpLis := make([][]int, N+1)
	for i := 0; i < N+1; i++ {
		dpLis[i] = make([]int, M+1)
		for j := 0; j < M+1; j++ {
			dpLis[i][j] = -1
		}
	}
	dpVal := make([][]int, N+1)
	for i := 0; i < N+1; i++ {
		dpVal[i] = make([]int, M+1)
		for j := 0; j < M+1; j++ {
			dpVal[i][j] = -9876543210
		}
	}
	dpLis[0][0] = 0
	dpVal[0][0] = 0
	for i := 0; i < N; i++ {
		maxLisBf := 0
		for j := 0; j < i; j++ {
			if A[i] > A[j] && dpLis[j+1][0] > maxLisBf {
				maxLisBf = dpLis[j+1][0]
			}
		}
		dpLis[i+1][0] = maxLisBf + 1
		dpVal[i+1][0] = A[i]
	}
	for i := 0; i < M; i++ {
		maxLisBf := 0
		for j := 0; j < i; j++ {
			if B[i] > B[j] && dpLis[0][j+1] > maxLisBf {
				maxLisBf = dpLis[0][j+1]
			}
		}
		dpLis[0][i+1] = maxLisBf + 1
		dpVal[0][i+1] = B[i]
	}

	for R := 0; R < N; R++ {
		for C := 0; C < M; C++ {
			maxLisBf := 0
			maxValCur := max(A[R], B[C])
			for r := -1; r < R; r++ {
				if dpLis[r+1][C+1] > maxLisBf && dpVal[r+1][C+1] < maxValCur {
					maxLisBf = dpLis[r+1][C+1]
				}
			}
			for c := -1; c < C; c++ {
				if dpLis[R+1][c+1] > maxLisBf && dpVal[R+1][c+1] < maxValCur {
					maxLisBf = dpLis[R+1][c+1]
				}
			}
			dpLis[R+1][C+1] = maxLisBf + 1
			dpVal[R+1][C+1] = maxValCur
		}
	}

	lis := -1
	for r := -1; r < N; r++ {
		for c := -1; c < M; c++ {
			lis = max(lis, dpLis[r+1][c+1])
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
