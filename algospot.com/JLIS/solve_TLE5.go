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

		// fmt.Scanln(&rawA)
		// fmt.Scanln(&rawB)
		// fmt.Println(N, M, A, B)
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
	// rec(&A, &B, N-1, M-1, &dpLis, &dpVal)
	// fmt.Println(dpLis)
	// fmt.Println(dpVal)
	lis, _ := rec(&A, &B, N-1, M-1, &dpLis, &dpVal)
	return lis
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func rec(Ap *[]int, Bp *[]int, lastA int, lastB int, dpLisp *map[p]int, dpValp *map[p]int) (int, int) {
	A := *Ap
	B := *Bp
	dpLis := *dpLisp
	dpVal := *dpValp
	cur := p{lastA, lastB}
	// println("START", lastA, lastB)

	if _, exist := dpLis[cur]; exist {
		return dpLis[cur], dpVal[cur]
	}

	maxLisBf := 0
	for i := -1; i < lastA; i++ {
		// if dpLis[p{i, lastB}] > maxLisBf && dpVal[p{i, lastB}] < A[lastA] {
		lisBf, maxBf := rec(Ap, Bp, i, lastB, dpLisp, dpValp)
		// println("A", lisBf, maxBf)
		if lisBf > maxLisBf && maxBf < A[lastA] {
			maxLisBf = lisBf
		}
	}
	for i := -1; i < lastB; i++ {
		lisBf, maxBf := rec(Ap, Bp, lastA, i, dpLisp, dpValp)
		// println("B", lisBf, maxBf)
		if lisBf > maxLisBf && maxBf < B[lastB] {
			maxLisBf = lisBf
		}
	}
	dpLis[cur] = maxLisBf + 1
	dpVal[cur] = max(A[lastA], B[lastB])
	// println("RES", lastA, lastB, "", dpLis[cur], dpVal[cur])
	return dpLis[cur], dpVal[cur]
}

type p struct {
	x, y int
}
