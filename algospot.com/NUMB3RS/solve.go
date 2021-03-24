package main

import "fmt"

func main() {
	var C int
	fmt.Scanf("%d", &C)
	for c := 0; c < C; c++ {
		var N, D, P int
		var A = [][]int{}

		fmt.Scanf("%d %d %d", &N, &D, &P)

		for i := 0; i < N; i++ {
			row := make([]int, N)
			for j := 0; j < N; j++ {
				fmt.Scanf("%d", &row[j])
			}
			A = append(A, row)
		}

		var T int
		fmt.Scanf("%d", &T)

		Q := make([]int, T)
		for i := 0; i < T; i++ {
			fmt.Scanf("%d", &Q[i])
		}

		result := solve(N, D, P, A)
		for i := 0; i < T; i++ {
			if i != 0 {
				fmt.Print(" ")
			}
			fmt.Print(result[Q[i]])
		}
		fmt.Println()
	}
}

func solve(N int, D int, P int, A [][]int) []float64 {
	sumA := make([]float64, N)
	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			sumA[i] += float64(A[i][j])
		}
	}

	trans := make([][]float64, N)
	for i := 0; i < N; i++ {
		row := make([]float64, N)
		for j := 0; j < N; j++ {
			row[j] = float64(A[i][j]) / sumA[i]
		}
		trans[i] = row
	}

	p := make([]float64, N)
	p[P] = 1

	for D > 0 {
		if D%2 > 0 {
			p = multi(p, trans, N)
		}
		trans = square(trans, N)
		D >>= 1
	}
	return p
}

func multi(vec []float64, sqmat [][]float64, size int) []float64 {
	res := make([]float64, size)
	for i := 0; i < size; i++ {
		for c := 0; c < size; c++ {
			res[c] += vec[i] * sqmat[i][c]
		}
	}
	return res
}

func square(sqmat [][]float64, size int) [][]float64 {
	res := make([][]float64, size)
	for i := 0; i < size; i++ {
		res[i] = make([]float64, size)
	}
	for r := 0; r < size; r++ {
		for c := 0; c < size; c++ {
			for i := 0; i < size; i++ {
				res[r][c] += sqmat[r][i] * sqmat[i][c]
			}
		}
	}
	return res
}
