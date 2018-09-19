# 알고리즘 공부를 합시당

## acmicpc.net

[1697](https://www.acmicpc.net/problem/1697) : 2018.09.06.

- BFS로 탐색하고 DP로 풀었다. 옛날엔 못풀었는데 기분이 좋다.  

[7576](https://www.acmicpc.net/problem/7576) : 2018.09.06.

- 처음에는 무작정 다 돌면서 바뀐거 있으면 한번더 도는 식으로 반복했다. -> 시간초과  
- 다음에는 바뀐 것만 큐에 넣으며 한바퀴 돌리면서 반복했다. -> 메모리 초과  
- 파이썬 문제인가 싶어 C++로 만들어봤다 -> 메모리 초과  
- 번뜩 큐에 똑같은 점들도 쌓이겠다 싶어서, 큐에 넣지 말고 set에 넣어서 파이썬으로 만들어봤다. -> 느리지만 통과..  
- C++을 잘 못쓰다보니 Tuple같은거 stl에 집어넣고 하는게 귀찮아서 그냥 파이썬으로 했다. 파이썬만 쓰지 말고 다른것도 써보면서 해야겠다.  

[2504](https://www.acmicpc.net/problem/2504) : 2018.09.10.

- 스택을 이용하는 문제인데, 익숙하지 않아서 도대체 어떻게 해야할지 모르겠다.
- 그래서 재귀를 썼다. 아주 지저분하게.. 주어진 길이가 짧아서 그냥 통과된듯.
- 스택을 두개 쓰면 됐을 것 같기도 함.
- 더 풀다보면 나아지겠지 ㅠㅠ

[10845](https://www.acmicpc.net/problem/10845) : 2018.09.10.

- 큐를 구현해보는 것.
- C++ 잘 못쓰는데 그냥 썼다.
- 느린데, 아마 입출력 속도때문인듯. C++로 입출력 많은 문제 푸는 사람들은 stdio 쓰는듯하다.

[1966](https://www.acmicpc.net/problem/1966) : 2018.09.11.

- 정직하게 풀면 되는걸 삽질했다.
- 내맘대로 추측했다가 틀림!
  - 확실한거 아니면 맘대로 생각하는건 자제하도록..
- 큐 두개를 써서, 하나는 계속 돌리고, 하나는 정렬해뒀다.
- 하나씩 돌리면서 센다. 원하는 값이 맨 앞으로 오고, 남은 것중 가장 크다면 출력!

[1966](https://www.acmicpc.net/problem/1966), [11866](https://www.acmicpc.net/problem/11866) : 2018.09.12.

- 큐로 돌리면 되는 문제.
- 근데 빠르게 하려면 큐에 계속 넣고 빼고 하는건 낭비인듯!
- 하지만 둘다 빼고 넣고 해서 (느리지만) 풀렸다.

[10866](https://www.acmicpc.net/problem/10866) : 2018.09.12.

- 덱을 짜보는 문제.
- 느릿느릿하다. 입출력이 느리고, 커다란 배열을 직접 만들어서 써서 그런가?
- 파이썬 slice를 쓰는 코드들이 있다.
  - 느린것같은데 만들어지는 덱이 생각보다 짧아서 빠른걸까.
- list의 pop(0)을 쓰는 코드도 있다. 이렇게 하는게 좋았겠다.
- 라이브러리 쓸땐 시간복잡도도 고려하면서 쓸만한거 있으면 쓰자.

[11727](https://www.acmicpc.net/problem/11727) : 2018.09.12.

- 간단한 DP?
- 근데 굳이 앞에있는걸 다 저장할필요는 없고, 앞에서부터 반복돌렸다.
- 1년전에 짠 코드는 재귀돌려서 메모이제이션을 했는데, 더 빨리 됨..
- 그래도 재귀 깊이가 너무 깊었던거라 반복문으로 바꾸는게 맞았을듯.

[1021](https://www.acmicpc.net/problem/1021) : 2018.09.13.

- Dqeue을 쓰는 문제
- 인데 그냥 계산을 해봤다.
- 이번에도 깊게 생각안하고 한 추측때문에 삽질했다.
- 섣부른 최적화를 하려고 한다. 일단 하고나서 최적화를 하자.

[10844](https://www.acmicpc.net/problem/10844) : 2018.09.13.

- 간단한 DP
- 근데 mod 빼먹어서 한번 틀렸다.

[10057](https://www.acmicpc.net/problem/10057) : 2018.09.13.

- 10844랑 거의 똑같음.
- 근데 N이 1000까지라서, 전부다 저장 안하고 배열 두개로 바꿔가면서 썼다.

[9465](https://www.acmicpc.net/problem/9465) : 2018.09.14.

- DP로 슥삭 푸는 문제.
- 오타때문에 한참 헤맸다.
- 오타는 정말 기묘하다.
  - 찾기 전) 아.. 이게 안될리가 없는데...
  - 찾은 후) 와.. 이게 어떻게 돌아가고 있었지...

[5430](https://www.acmicpc.net/problem/5430) : 2018.09.15.

- dqeue를 써서 왼쪽 오른쪽을 빼낸다.
- 두번이나 틀렸는데,
  - 첫 번째는 comprehension 문에서 input()을 썼던 실수.
    - if 조건이 맞으면 input()을 받지만, else이면 input() 자체를 실행하지 않아서 에러가 났다.
  - 두 번째는 문제 조건을 까먹은 것..
    - 빼는것만 뒤집어서 뺴는게 아니라 출력할 때도 뒤집어야 하는데 까먹음..
- 실수를 줄이자.

[2747](https://www.acmicpc.net/problem/2747), [2748](https://www.acmicpc.net/problem/2748) : 2018.09.15.

- 간단한 피보나치 문제.

[2479](https://www.acmicpc.net/problem/2479) : 2018.09.17.

- 큰 수의 피보나치 문제.
- 행렬을 제곱해가면서 찾아서 풀었다.
- 한번 틀렸는데, 왜인지 모르겠다.. 이상한 코드가 붙어있었나보다.
- 틀려서 코드 보면서 가만히 찾아봤는데, 도저히 못찾겠어서 그냥 냈더니 맞음.

[1003](https://www.acmicpc.net/problem/1003) : 2018.09.17.

- 그냥 피보나치로 계산해서 풀면 되는 문제.
- 옛날에 스킴으로 풀었던 문제. 마법사책 봐야하는데 잔뜩 미뤄뒀다.
- 여튼 그땐 재귀로 풀었는데, 이번엔 dp로 풀었다.
- 여튼 0은 1, 0으로 시작하는 피보나치, 1은 0, 1로 시작하는 피보나치.
- 그런데 그냥 튜플로 dp해서 풀었다. 범위가 좁다.

[11050](https://www.acmicpc.net/problem/11050), [11051](https://www.acmicpc.net/problem/11051)  : 2018.09.18.

- 이항계수 문제.
- 11050은 N이 별로안커서 재귀돌림
- 11051은 N이 조금 커서 파이썬으로 재귀하면 터진다 + 오래걸린다
- 메모이제이션을 하려고 했는데, 재귀가 터져서 dp로 함
- 10051에서 mod 괄호안쳐서 한번 틀림..
- 다른사람 코드를 보니 11051에서 곱하고 나누고 하며 직접 계산하던데, 이런 수학적인 공식이 있는건 공식쓰는것도 좋을 듯.

---

## leetcode.com

[find-and-replace-pattern](https://leetcode.com/problems/find-and-replace-pattern/description/) : 2018.09.06.

- 친구가 풀어보래서 풀었다.
- 입력받은 단어를 패턴이랑 한글자씩 매핑시켜서 저장한다.
- 만약 단어에서 매핑하려는 문자가 이미 매핑되었다면!
  - 매핑된 문자가 패턴의 문자와 일치하는지 확인한다.
  - 일치하면 다음 글자로
  - 다르면 return False
- 단어에서 처리중인 문자는 처음 보는건데 매핑할 패턴 문자는 이미 사용했다면!
  - return False
- 두쪽 다 클린하다면 새로운 매핑을 만들고 다음 글자로.

---

## programmers.co.kr

[짝지어 제거하기](https://programmers.co.kr/learn/courses/30/lessons/12973) : 2018.09.19.

- 나는 스택을 써서 풀었다.
- 옛날에는 이런게 안보였는데 예전보단 조금 나아진것같다.
