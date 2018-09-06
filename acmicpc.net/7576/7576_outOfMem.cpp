#include <iostream>
#include <vector>
#include <deque>

using namespace std;

int main(){
    int M, N, tmp;
    cin >> M >> N;

    vector< vector<int> > box(N);
    vector< vector<int> > nextBox(N);
    deque<int> points;
    deque<int> nextPoints;
    for (int row = 0; row < N; row++) {
        box[row] = vector<int>(M);
        nextBox[row] = vector<int>(M);
        for (int col = 0; col < M; col++) {
            cin >> tmp;
            box[row][col] = tmp;
            nextBox[row][col] = tmp;
            if (tmp == 1){
                points.push_back(row);
                points.push_back(col);
            }
        }
    }

    int result = -1;
    while (points.size() > 0) {
        cout << "test " << points.size() << endl;
        result++;
        while (points.size() > 0){
            int row = points.front();
            points.pop_front();
            int col = points.front();
            points.pop_front();

            nextBox[row][col] = 1;
            if (col > 0 && box[row][col - 1] == 0) {
                nextBox[row][col - 1] = 1;
                nextPoints.push_back(row);
                nextPoints.push_back(col - 1);
            }
            if (col < M - 1 && box[row][col + 1] == 0) {
                nextBox[row][col + 1] = 1;
                nextPoints.push_back(row);
                nextPoints.push_back(col + 1);
            }
            if (row > 0 && box[row - 1][col] == 0) {
                nextBox[row - 1][col] = 1;
                nextPoints.push_back(row - 1);
                nextPoints.push_back(col);
            }
            if (row < N - 1 && box[row + 1][col] == 0) {
                nextBox[row + 1][col] = 1;
                nextPoints.push_back(row + 1);
                nextPoints.push_back(col);
            }
        }
        swap(box, nextBox);
        swap(points, nextPoints);
    }

    for (int row = 0; row < N; row++) {
        for (int col = 0; col < M; col++) {
            if (box[row][col] == 0) {
                cout << -1 << endl;
                return 0;
            }
        }
    }
    cout << result << endl;
    return 0;
}
