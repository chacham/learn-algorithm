class Solution {
    public int solution(int[][] triangle) {
        int depth = triangle.length;

        for (int i = 1; i < depth; i++) {
            triangle[i][0] += triangle[i-1][0];
            for (int j = 1; j < i; j++) {
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j]);
            }
            triangle[i][i] += triangle[i-1][i-1];
        }
        int answer = 0;
        for (int i = 0; i < depth; i++) {
            answer = max(answer, triangle[depth - 1][i]);
        }
        return answer;
    }
    private int max(int x, int y) {
        return x > y ? x : y;
    }
}
