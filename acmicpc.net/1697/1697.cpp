#include <iostream>
#include <vector>
#include <deque>

#define MAX 100000
#define MIN 0

int main() {
    int N, K;
    
    std::cin >> N >> K;

    std::vector<int> time(MAX + 1, MAX + 1);
    std::deque<int> processed;

    processed.push_back(N);
    time[N] = 0;
    while (processed.size() > 0) {
        int nowPos = processed.front();
        int nowTime = time[nowPos];
        processed.pop_front();

        // If out of position range, process next position
        if (nowPos < MIN || nowPos > MAX) {
            continue;
        }
        
        // Twice
        if (nowPos * 2 <= MAX && time[nowPos * 2] > nowTime + 1) {
            time[nowPos * 2] = nowTime + 1;
            processed.push_back(nowPos * 2);
        }

        // -1
        if (nowPos > MIN && time[nowPos - 1] > nowTime + 1) {
            time[nowPos - 1] = nowTime + 1;
            processed.push_back(nowPos - 1);
        }

        // +1
        if (nowPos < MAX && time[nowPos + 1] > nowTime + 1) {
            time[nowPos + 1] = nowTime + 1;
            processed.push_back(nowPos + 1);
        }
    }
    std::cout << time[K] << std::endl;

    return 0;
}
    
    
