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

[2749](https://www.acmicpc.net/problem/2749) : 2018.09.17.

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

[11050](https://www.acmicpc.net/problem/11050), [11051](https://www.acmicpc.net/problem/11051) : 2018.09.18.

- 이항계수 문제.
- 11050은 N이 별로안커서 재귀돌림
- 11051은 N이 조금 커서 파이썬으로 재귀하면 터진다 + 오래걸린다
- 메모이제이션을 하려고 했는데, 재귀가 터져서 dp로 함
- 10051에서 mod 괄호안쳐서 한번 틀림..
- 다른사람 코드를 보니 11051에서 곱하고 나누고 하며 직접 계산하던데, 이런 수학적인 공식이 있는건 공식쓰는것도 좋을 듯.

[2309](https://www.acmicpc.net/problem/2309) : 2018.09.20.

- 간단한 브루트포스 문제
- 그런데, 브루트포스를 해야하는 상황이 오면 어떻게 해야할지 감이 하나도 안잡힌다
- 이런것도 많이 풀어봐야할듯

[1149](https://www.acmicpc.net/problem/1149) : 2018.09.20.

- DP문제
- 옛날에 풀어보려다 도저히 어떻게 해야할지 몰라서 포기했던 기억이 난다
- 빠르게 푼 사람들이랑 푼 방식은 같은 것 같은데, 시간은 내꺼가 길다.
- 세세하게 구현에서 느려지는 부분이 있는듯

[9461](https://www.acmicpc.net/problem/9461) : 2018.09.23.

- DP
- 그림을 보면 안다
- 그냥 커밋 하려고 후딱 찾아 푼 쉬운 문제

[2174](https://www.acmicpc.net/problem/2174) : 2018.09.24.

- 시뮬레이션 문제?
- 그냥 시키는대로 하면 되긴 한다.
- 근데 귀찮아서 사람들이 많이 안푸는듯!
- 사실 나도 어제 풀다가 오늘 이어서 풀었다..
- 좌표로 어떻게 하는건 x, y가 직관적으로 안되서 항상 헷갈리는듯.(출력할 때 헷갈림)
- row, col로 바꿔서 하는게 지금은 제일 편한 것 같다.
- 다음에 비슷한거 풀어보면서 x,y로 그대로 하는게 나은지 row, col로 하는게 나은지 해보자.

[2805](https://www.acmicpc.net/problem/2805) : 2018.09.25.

- 이분탐색 문제 인데 좀 이상하게 함
- 프리소트로 정렬해두면 빠르게 찾을 수 있지 않을까 해서 정렬을 했다.
- 그리고 답이 있는 높이 범위를 찾았다.(높은것부터 다음꺼는 안잘리는만큼 합해보면서? 설명이 어렵네)
- 범위를 찾으면 그 범위에서 밑에서 찾아 올라오며 정답을 찾는다.
- 그냥 1씩 올리니까 시간 초과.. -> 이분탐색으로 찾자!
- 제출해보니 파이썬중에 속도 1등! 별일아니지만 기분좋당
- 다른사람 코드 보니, 나처럼 범위를 찾고 이런거 없이 바로 이분탐색을 했다.
- 내가 약간 빠르긴 하지만, 바로 짜야할 때 이런거 하나하나 하고있으면 느릴듯..
- 이번 문제 풀고나서
  - 이분탐색같은 기본기를 익히자
  - 어느정도 속도가 나올지 추측하는 능력을 기르자

[5532](https://www.acmicpc.net/problem/5532) : 2018.09.27.

- 간단한 구현문제
- 반복문을 돌렸는데, 나눗셈으로 바로 한 사람도 있었다

[5054](https://www.acmicpc.net/problem/5054) : 2018.10.08.

- 간단한 구현문제
- 괜히 꼬아서 생각하지 말도록 하자

[12758](https://www.acmicpc.net/problem/12758) : 2018.10.12.

- dp인듯
- 약수 찾아두고 계속계속 더하고 하는 문제
- 순서가 왔다갔다하고 해서 헷갈린다

[2485](https://www.acmicpc.net/problem/2485) : 2018.10.14.

- gcd 문제
- 그냥 주룩주룩 이어서 gcd 하면 된다

[2169](https://www.acmicpc.net/problem/2169) : 2018.10.19.

- 길찾기 DP 문제
- 처음엔 NM^2으로 했는데 계속 시간초과.
- 제약을 가만히 보고있으니 어떻게 할지 생각나서 NM으로 했다.
- 비슷한 DP 나오면 풀 수 있을것만 같은 기분... 재미있는 문제였당

[16236](https://www.acmicpc.net/problem/16236) : 2018.10.21.

- 기묘한 BFS
- 친구들이 풀었던 삼성 문제. 궁금해서 들어가서 하나 풀었다
- 그냥 부담없이 푸니까 풀긴 풀었는데 잘 모르겠다.
  - 오래걸릴까봐 걱정했는데 생각보다 빠릿하게 잘돌아감..
  - 시험장에서 만나면 긴장해서 못풀었을지도 모르겠다
- 좀 새로운 느낌 문제라서 재미있었다

[2456](https://www.acmicpc.net/problem/2456) : 2019.01.02.

- if문을 열심히 쓰는 문제..
- 반복문을 돌다가 반목문 속에서 list를 수정해서 틀렸다
  - 그냥 테스트케이스 바꿔가면서는 안잡히는, 운에 따르는 오류..
- 조심히 코딩하도록 하자

[2616](https://www.acmicpc.net/problem/2616) : 2019.01.02.

- dp문제인데, 여러번 돌리는 문제
- 대충대충 짰는데, 뒷쪽에서 필요없는거 미리 빼버리면 아주조금 더 빠를듯.
- 바로바로 돌아가서 기분이 좋다.

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

[add-two-numbers](https://leetcode.com/problems/add-two-numbers/description/) : 2018.11.09.

- 두 숫자를 더하는 문제
- 그런데, 그냥 더하는게 아니라 전가산기를 만들어서 뒤에서 한자리씩 더한다.
- 스칼라로 풀어보고싶었는데, 잘 몰라서 아쉽다.
- 그냥 자바스크립트로 풀었음
- 재귀로 앞에서부터 하나씩 더해버렸다~

[integer-to-roman](https://leetcode.com/problems/integer-to-roman/description/) : 2018.11.22.

- 정수를 입력받으면 로마 숫자 문자열로 바꾸는 문제
- 4, 9 단위일때 조심해야했다
- 근데 그냥 쭉 나열시켜놓고 큰거에서 쭉 빼면 됨

[3sum](https://leetcode.com/problems/3sum) : 2019.01.06.

- 주어진 리스트에서 세 숫자의 합이 0이 되는 조합을 찾기
- 계속 시간초과로 틀림.. 처음엔 N^3으로 했는데, 이건 틀렸던 것
- 고민해서 N^2으로 했는데, 이것도 계속 시간초과가 났다.. 아마 파이썬이라서 그런듯!
- 다른분 코드도 보고, 중복검사 하는 부분 빠르게 건너가고 하니 통과했다.
- 리트코드는 틀린 TC 보여주는데, 이걸 바로 보고하니까 실력이 안느는 느낌이다
  - 혼자서 좀더 고민해볼 것.
  - 그리고 보이는 TC만 집중해서 고치니 코드도 더러워지더라..

[shortest-distance-to-a-character](https://leetcode.com/problems/shortest-distance-to-a-character/) : 2019.01.07.

- 주어진 문자열에서 주어진 문자와의 거리가 얼마나 되는지 확인하는 문제
- 나는 앞에서부터 쭉 돌다가, 찾는 문자가 나오면 앞으로 쭉 돌려본다.
- 그런데, 앞으로 한번 뒤로 한번 훑어보는것도 괜찮을듯.
  - 그래서 고친게 solve2
- 찾을때마다 돌아가며 확인하는건 112ms, 앞으로 한번 뒤로 한번은 76ms 걸렸다.
  - 검사하는것 자체는 이정도로 차이 안날 것 같은데, localty때문?

[delete-node-in-a-bst](https://leetcode.com/problems/delete-node-in-a-bst/) : 2019.01.08.

- BST에서 주어진 값 찾아 지우기
- 얼마전에 JS 자료구조 라이브러리 만들면서 해봤는데도 생각보다 신경쓸게 많다.
- 루트를 지우면? 한쪽 child만 있으면? 양쪽 child 다있으면? 기타등등
- 그래서 꽤 오래걸렸다. 그냥 찾기는 쉬운데 트리 유지하면서 하는건 은근 귀찮..
- 재귀로 하는것도 생각해보자. 난 그냥 반복으로 찾아서 옮기고 지우고 했는데, 재귀로 짠거 한번 보니 멋있다

[reverse-only-letters](https://leetcode.com/problems/reverse-only-letters/) : 2019.01.08.

- 문자열에서 영어글자는 앞뒤로 바꾸고, 다른 글자들은 그대로 놔두는 문제
- js에서 문자(char)를 직접 다루는게 없고, string에다가 map이나 forEach같은 array 함수들이 동작안해서 귀찮..
- 그래서 그냥 Array로 바꿔서 썼다
- 영어문자들만 stack에 넣어두고, 영어문자가 나오면 pop해서 대신 넣어줬다.
  - Map이 병렬적이지 않을꺼라고 생각하고 한것!!
  - 병렬적으로 돌아가면 forEach로 result에다가 하나씩 넣어주면 될것같다.

[longest-substring-without-repeating-characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) : 2019.02.16.

- 마지막 인덱스를 뒤로 밀다가 이미 존재하는게 나오면 시작하는 인덱스를 뒤로 밀어서 풀었다.
- 처음에는 입력 범위를 내맘대로 생각함..
  - 무조건 길이 1 넘을꺼라고 맘대로 생각, 영어 소문자만 오겠거니 생각해버림.
  - 입력에 대해 마음대로 생각하지 말자..
- 느려서 쓸데없는 부분들을 좀 지우니까 조금 빨라졌다.
- IDE 없이 그냥 코딩하니 역시 난 잘 모른다. 도움 없이 코딩하는 능력 키우자.

[linked-list-cycle](https://leetcode.com/problems/linked-list-cycle/) : 2019.02.17.

- 주어진 링크드리스트에서 사이클이 있는지 확인하는 문제
- 예전에 Elements of programming 이란 책에서 읽었다.
  - 근데 번역이 너무 별로라서 맨앞에 쪼금만 읽고 포기했다.
  - 언젠가 원서로 다시 읽어봐야지..
- 빠른것(두칸씩 가는것)과 느린것(한칸씩 가는것)이 만나면 사이클이 존재한다~~

[maximum-swap](https://leetcode.com/problems/maximum-swap/) : 2019.02.17.

- 주어진 숫자에서 최대 한번 자리를 바꿔서 가장 큰 숫자를 만들기.(안바꿔도됨)
- 숫자 범위가 10^8까지라서 그냥 브루트포스했다.
- 문자열로 바꿔서 자리바꿔버리기!
- 범위가 작아서 쉬운듯. 숫자 커지면 어떻게 할지 약간 고민해보는게 좋을것같다.
  - 근데 숫자 커지면 그것도 어차피 문자열로 처리하는게 낫지 않을까?

[ambiguous-coordinates](https://leetcode.com/problems/ambiguous-coordinates/) : 2019.02.25.

- 숫자를 잘라서 적당한 숫자가 두개 나오게 하는것.
  - 정수부분은 맨 앞에 0, 실수부분은 끝에 0이 오면 안된다.
- 네조각으로 잘라서 각각 맞는지 확인했다.
- 입력을 준대로 억지로 쓰려고 하다보니 꼬임
  - 쓰기 편하게 가공한 뒤에 문제 풀자
- 바운더리가 역시 귀찮다. 더 깊이 생각하고 짜자.

[container-with-most-water](https://leetcode.com/problems/container-with-most-water/) : 2019.02.27.

- 풀어봤던 문제라 금방 풀었다.
- 그런데, 대충대충 생각하고 풀었다고 생각했는데, 중요부분 처리하고나서 해야할걸 안함..
  - 꼼꼼하게 수도코드 적으면서 하는 습관을 좀 들여야할듯.
  - 특히 ide 없이 코딩할때!!!

[trapping-rain-water](https://leetcode.com/problems/trapping-rain-water/) : 2019.02.28.

- container-with-most-water를 푸니까 추천에 뜬 문제.
- 비슷한 느낌인데 좀 다르다!!
- 위에서 물이 떨어졌을때 받기는 물 다 모으면 얼마나 될까 하는것.
- 왼쪽에서 올라오고 오른쪽에서 올라와서 제일 높은 것 기준으로 생각.
- 올라가면서는 낮은 쪽만 생각하면 된다.
- 혼자 테스트케이스 만들면서 해봤는데, 틀린거 나왔다
  - 왼쪽, 오른쪽에서 올라올때 양쪽 높이 같은경우를 포함안함!!
  - 한쪽은 열리고 한쪽은 닫아두는게 여기서도 적영되었다.
  - 코드 돌리면서 디버깅하는걸 줄이도록 더 꼼꼼히 코드 보도록 하자.

[product-of-array-except-self](https://leetcode.com/problems/product-of-array-except-self/) : 2019.03.01.

- 주어진 배열에서 원래 인덱스에 있는 숫자 빼고 다 곱한 배열을 만드는 문제.
- 처음엔 문제를 이상하게 이해함.. 천천히 읽자
- 시간은 O(n)으로 풀고, 공간은 O(1)로 풀라고 했다.
  - 첨엔 공간도 O(n)으로 풀었는데, 누워있다보니 생각나서 O(1)로 바꿈
  - 일단 빠르게 구현하고 더 좋게 만드는게 좋을듯하다.
- 확실히 적고 하니까 더 편하다!! 습관 들이자

[string-to-integer-atoi](https://leetcode.com/problems/string-to-integer-atoi/) : 2019.03.02.

- 문자열을 숫자로 바꾸는 문제
- 빈 문자열이 입력으로 오는거 빼먹어서 틀렸다
  - 필요한 부분 뒤에 더이상 안들어오는 경우도..
- 입력에 대해서 좀 더 넓게 생각해야할듯.

[symmetric-tree](https://leetcode.com/problems/symmetric-tree/) : 2019.03.04.

- 트리가 좌우대칭인지 확인하는 문제
- 처음 생각난건 재귀로 왼쪽 오른쪽 확인하는거
  - 호다닥 만들었다
- 그런데 Recursive, Iterative 둘다 구현해보래서 만들었다
  - Iterative는 스택 써서!
- 빈 입력일때 처리 안해서 한번 틀림.. 빈 입력 항상 고려하도록 하자

[balanced-binary-tree](https://leetcode.com/problems/balanced-binary-tree/) : 2019.03.05.

- 주어진 바이너리 트리가 balanced인지 판별하는 문제
- and 빼먹어서 이상하게 실행이 안됨..
  - 보기 편하게 개행하려다 잘못 고친 것
  - 중요한걸 먼저 생각합시다
- height랑 balanced를 따로 계산하니까 재귀를 따로 돌아서 중복계산 계속 하고있었다
  - 다른사람 코드 보고 나도 합치니까 코드도 짧아지고 시간도 절반이 됨!

[merge-two-sorted-lists](https://leetcode.com/problems/merge-two-sorted-lists/) : 2019.03.06.

- 두 정렬된 리스트를 하나로 합치는 문제
- 이건 이상한짓 안하고 잘 풀었다!

[trim-a-binary-search-tree](https://leetcode.com/problems/trim-a-binary-search-tree/) : 2019.03.06.

- 처음엔 잘 풀었다고 생각했는데, 풀고나니 훨씬 깔끔한 코드가 있어서 고쳤다
- 그래도 생각은 처음부터 잘 하긴 한듯!

[zigzag-conversion](https://leetcode.com/problems/zigzag-conversion/) : 2019.03.06.

- 예전에 보고 풀기 싫어서 안풀었던 문제인데.. 풀었다!
- 그래도 역시 깔끔하진 않은듯.. 억지로 끼워맞춘 느낌

[two-sum](https://leetcode.com/problems/two-sum/) : 2019.03.07.

- 두 숫자의 합이 주어진 target이 되는 두 인덱스를 찾는 문제
- 그냥 생각나는대로 2중 for문 돌렸더니 엄청 느렸다
- 풀고나니 dictionary 쓰는 코드가 있길래 보고 따라씀..
- 깊이 생각하도록 합시다

[maximum-binary-tree](https://leetcode.com/problems/maximum-binary-tree/) : 2019.03.08.

- 주어진 리스트를 큰 값이 위에 있는 트리로 바꾸는 문제
- 나는 앞에서부터 처리하면 오른쪽에만 붙는구나 하면서 풀었다
- 그런데 짧고 빠른 코드들 많으니까 보고 더 생각해봐야할듯

[jump-game](https://leetcode.com/problems/jump-game/) : 2019.03.10.

- 처음 위치에서 마지막까지 갈 수 있는지 판별하는 문제
- 카운트 바꿔가면서 하니까 금방 풀었다
- 그런데, 처음에 대충 짜다보니 코드 지저분해짐..
  - 천천히 생각하면서 짜자

[jump-game-ii](https://leetcode.com/problems/jump-game-ii/) : 2019.03.11.

- jump-game이랑 비슷한데 마지막까지 갈 수 있을 때 최소 점프 수를 구하는 문제
- 처음엔 쌩으로 탐색했는데, 시간초과 났다
  - 그래서 뒷쪽부터 탐색해서 계산할필요 없는 곳 나오면 넘어가게 했더니 통과
  - 이건 num길이만한 배열 필요함
  - 한 위치에 여러번 계산도 한다
- 풀고나서 다른코드 보는데, 뒤로 쭉 밀면서 계산하는 코드가 너무 좋아서 나도 고침
  - 그런데 계속 틀렸던게, 마지막 인덱스에서 점프하는건 계산할 필요가 없었음
  - 바운더리는 항상 어렵다

[gray-code](https://leetcode.com/problems/gray-code/) : 2019.03.13.

- Gray code를 주어진 숫자에 따라 쭉 만드는 문제
- 재귀로 전에 어디선가 읽었던건지 들었던건지 생각나서 쉽게 풀었다

[merge-sorted-array](https://leetcode.com/problems/merge-sorted-array/) : 2019.03.18.

- 두 정렬된 배열을 주고, 첫 번째 배열로 merge하는 문제
- easy인데 너무 어려워서 내가 멍청한건가 엄청 고민함..
- 다른사람 글 보니까, 뒤에서 접근하길래 뒤에서부터 해보니까 너무너무너무 쉬운문제였다
- 이상하게 어려울땐 시작하는 방향을 다르게 해보자

[shortest-unsorted-continuous-subarray](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/) : 2019.03.19.

- 주어진 배열에서 어느정도 길이의 subarray를 정렬해야 완전히 정렬되는지 찾는 문제
- 처음에 복잡하게 생각하다가, 그냥 정렬해버리고 비교해버렸음
- 그래도 더 빠른 해법이 있겠지. O(n)으로 될것같으니 내일 다시 생각해보자

[find-peak-element](https://leetcode.com/problems/find-peak-element/) : 2019.03.20.

- 배열에서 피크값을 찾는 문제
- 어떤 피크든 상관없다!!
- 처음엔 O(n)으로 풀었는데, 생각해보니 하나만 걸려라 식으로 이진탐색으로 큰 값 찾으면 됨
- 그래서 짜고나서 다른사람 코드 보니까 더 깔끔하게 짠 사람이 있어서 내껏도 고쳤다
- 간만에 이진탐색 연습했다
- 천천히 생각하면서 코드 짤 것

[regular-expression-matching](https://leetcode.com/problems/regular-expression-matching/) : 2019.03.20.

- 재귀로 대충 짜면 그래도 돌아는 갈줄 알았는데, 생각처럼 잘 풀리진 않은 문제
- 케이스를 신경쓸게 많다..
- 그래도 재귀로 어찌저찌 짜서 구현했더니, 아주 느림
- 메모이제이션 넣어서 빨라졌다!
- 끝에 남아있는 경계 체크하는거 헷갈려서 한참 찾았다. 이항하며 잘 생각해보자

[word-search](https://leetcode.com/problems/word-search/) : 2019.03.23.

- 주어진 2차원 배열에서 쭉 이어진 주어진 문자열이 있는지 찾는 문제(중복 방문 X)
- 재귀로 dfs 하니까 풀리는 문제
- 내껀 쫌 느린데, 인자로 리스트를 계속 새로 만들어주고, 그 안에서 또 계속 검색하고 해서 그런듯
- 문자열이 길어지면 메모리 터지고 엄청느려질듯!!
- 따로 visited 기록하는걸 놔두던지, 해시맵같은걸로 저장하든지 하고, route를 계속 새로 안만드는게 나을듯

[unique-binary-search-trees-ii](https://leetcode.com/problems/unique-binary-search-trees-ii/) : 2019.03.27.

- 만들 수 있는 바이너리 서치 트리를 모두 만들어서 리턴하는 것
- 재귀로 적당히 하면 잘 됨
- 근데 10 넘으면 너무느려서 터지는듯

[unique-binary-search-trees](https://leetcode.com/problems/unique-binary-search-trees/) : 2019.03.27.

- 만들 수 있는 바이너리 서치 트리 갯수를 구하는 것
- 이건 쫌더 쉽다
- 숫자가 커지면 메모이제이션 해서 좀 빠르게 만들 수 있을듯

[interleaving-string](https://leetcode.com/problems/interleaving-string/) : 2019.03.27.

- 문자열 두개를 적당히 머지해서 주어진 문자열이 되는가?
- 그냥 재귀로 대충 했더니 느리다
- Discuss에 dp가 있길래 어떻게 할까 그냥 짜봤더니 돌아감
- 기본적인 수법들이 생각이 안나네ㅠㅠ
- Solution 보면 이런저런것들이 있느니까 한번 해봐야겠다

[validate-binary-search-tree](https://leetcode.com/problems/validate-binary-search-tree/) : 2019.03.27.

- BST에 요소 잘 들어가있는지 확인하는 것
- 그냥 바로 챡 될줄 알았는데 생각처럼은 안됐다
- 요즘에 깊게 생각하는걸 또 잘 안하는듯.. 천천히 생각하자

[different-ways-to-add-parentheses](https://leetcode.com/problems/different-ways-to-add-parentheses/) : 2019.03.29.

- 전에 비슷한거 풀어봤던것같아서 금방 했다
- 대충 해도 풀렸는데, 메모이제이션 쓰니까 더 빨리됨

[construct-the-rectangle](https://leetcode.com/problems/construct-the-rectangle/) : 2019.04.03.

- 주어진 넓이의 사각형을 만드는 가로세로 길이 찾기
- 그냥 약수 찾기인데, 제일 루트에 가까운 약수 찾기다
- 목록을 쭉쭉 만들다가 제일 가까운거랑 몫 리턴하면 됨
- 나는 리스트에 넣었는데, 하나만 가지고 있으면 되는듯

[same-tree](https://leetcode.com/problems/same-tree/) : 2019.04.06.

- 주어진 두 트리가 같은것인지 확인하는 문제
- 양쪽 확인하다가 not 안붙여서 한참 왜안될까 고민했다
- 급하게 안짜고 미리 적기 연습해볼까 생각했었는데, 잘 안되네..

[merge-two-binary-trees](https://leetcode.com/problems/merge-two-binary-trees/) : 2019.04.20.

- 주어진 두 바이너리 트리를 합치는 것
- 재귀로 짜면 쉽다

[binary-tree-pruning](https://leetcode.com/problems/binary-tree-pruning/) : 2019.04.20.

- 바이너리 트리 중에서 조건 만족하는것만 남기기
- 조건 쓸데없는거 안하도록 잘 생각하니까 잘됨!

[groups-of-special-equivalent-strings](https://leetcode.com/problems/groups-of-special-equivalent-strings/) : 2019.04.20.

- 다 검사할 필요 없이, 동치인것들 다 합치면 되니까 normalize하면 된다
- 근데, 다른사람 코드 보니까 더 잘짰다...

[print-in-order](https://leetcode.com/problems/print-in-order/) : 2019.12.15.

- 호출 순서에 상관없이, 정해진 순서대로 실행되도록 하기
- 처음엔 `while`문으로 spin lock처럼 함
  - 2초 걸림. 아주 느리다(당연)
- 다음은 `sleep`을 아주 조금 줘서 돌림
  - 꽤 빨리 되지만 이상함
- 다른사람꺼 보고 `Lock` 사용
  - 깔끔하고 좋다
  - 파이썬에서 그냥 쓸수있는 `Lock`이 있는걸 알게됨

[duplicate-emails](https://leetcode.com/problems/duplicate-emails/) : 2020.04.09.

- 간단한 SQL 문제
- Inner Query 안쓰고도 하는사람 있는데, 다른사람 코드 확인해볼것

[valid-phone-numbers](https://leetcode.com/problems/valid-phone-numbers/) : 2020.04.10.

- Bash 문제
- 그냥 정규표현식 쓰면 되는데, grep 대충만 쓰다보니, 옵션이 잘 생각이 안난다
- 정규표현식 필요한 만큼은 알아두도록 하자

[number-of-islands](https://leetcode.com/problems/number-of-islands/) : 2020.04.12.

- BFS/DFS 기본 문제
- 오랜만에 풀었는데, 푸는 방식은 맞았는데 느리다
- 다시 꾸준하게 풀면서 기술같은걸 손에 익혀야 할듯

---

## programmers.co.kr

[짝지어 제거하기](https://programmers.co.kr/learn/courses/30/lessons/12973) : 2018.09.19.

- 나는 스택을 써서 풀었다.
- 옛날에는 이런게 안보였는데 예전보단 조금 나아진것같다.

[쇠막대기](https://programmers.co.kr/learn/courses/30/lessons/42585) : 2018.09.19.

- 스택.
- 별로 안어렵다.

[섬 연결하기](https://programmers.co.kr/learn/courses/30/lessons/42861) : 2018.09.21.

- 최소 신장 트리 만들기.
- 쉬운건데, 이번에도 쓸데없는 생각 해서 몇번 틀림.
- 성급한 최적화를 할 필요가 없다. 돌려보고 느리면 하자!

[셔틀버스](https://programmers.co.kr/learn/courses/30/lessons/17678) : 2018.09.29.

- 작년 카카오 블라인드 문제
- 다풀어놓고 바보같은 실수 두개때문에 헤맸다.
  - 1을 적여아 할 곳에 i를 적은 것
    - 다른 언어였으면 컴파일타임에나 런타임에나 에러가 났을 듯.
      - 반복문 밖이라 i가 없어야 했는데, 앞에서 돌던 반복문때문에 남아있었음..
      - 정적 언어였으면 컴파일타임 에러 났겠지
      - js에서 let 썼으면 아마 스코프 밖이라고 에러 났을듯
      - 파이썬 쓰면 더 조심하자
  - 정렬 순서
    - 시간 정렬할 때, 시간순 정렬과 분별 정렬을 다 해야 할 때가 있다
    - 분 먼저 하고 시간을 정렬해야 우리가 생각하는 정렬이 됨.
    - 그런데 아무생각 없이 시간 먼저하고 분을 했음...
    - 테스트케이스를 좀 제대로 짜두고 해야할듯?
- 실수 줄이도록 연습하자..

[자동완성](https://programmers.co.kr/learn/courses/30/lessons/17685): 2018.09.29.

- 작년 카카오 블라인드 문제
- 이상하게 했는데 생각보다 잘돌아간다(그리고 짧다)
- 운이 약간 작용해서 바로 풀린 문제
  - 파이썬 인덱싱에서 끝나는 부분 인덱스가 크면 그냥 끝까지 됨.
  - "go"[:3] 같은것도 그냥 "go"가 된다
  - 덕분에 일치할 때 케이스를 처리를 따로 안했는데 맞았다
- key를 점점 늘려가며 검색되는 원소가 하나면 key의 길이를 result에 추가
  - 처음에는 문자열들의 첫글자만 가지고 dict를 만든다
  - 그리고 윈소가 다 빠질때까지 계속 키를 늘려가며 다시 dict에 넣음

[정수 삼각형](https://programmers.co.kr/learn/courses/30/lessons/43105): 2018.10.04.

- 간단한 dp문제
- 근데 바운더리 체크 이상하게 해서 틀렸다..
- 자바로 했는데, 자바는 ide 없으면 실행해보기가 너무 불편하다.
- 스켈레톤 코드 주는 것들도 애매하다.
- 여튼 자바는 불편하다..

[도둑질](https://programmers.co.kr/learn/courses/30/lessons/42897): 2018.10.04.

- dp문제
- 조금 기묘한데, 나는 그냥 맨앞에꺼 포함/안포함 해서 2개짜리로 만들어서 했다.
- 그런데, 마지막에 답찾을 때, 비교대상 하나를 안넣어서 틀림..
- 한번만에 맞추는 문제가 없냐 허허

[3xN 타일링](https://programmers.co.kr/learn/courses/30/lessons/12902): 2018.10.05.

- dp 문제.. 인데 n짜리는 아님.
- 2xN은 쉬웠는데, 이건 생각 한참 했다..
- n^2가 나와서 될까 했는데 됨!
- dp는 다 n으로 생각하고 시작했는데, 이래저래 다양하게 생각해보도록 하자.

[사칙연산](https://programmers.co.kr/learn/courses/30/lessons/1843): 2019.03.11.

- 괄호를 여기저기 두면서 덧셈, 뺄셈 결과가 가장 커지는 값 찾기
- 양쪽으로 나누면서 무작정 하니까 맞긴 하는데, 느리다
- 오랜만에 메모이제이션 쓰니까 잘 돌아감!
- 막막해보이는 것도 작은것부터 하면 될지도!

## algospot.com

[FESTIVAL](https://algospot.com/judge/problem/read/FESTIVAL) : 2018.09.26.

- 알고리즘 문제 해결 전략에서 맨 처음에 나오는 문제
- 선형으로 풀 수도 있다고 하지만 지금은 잘 모르겠다..
- 이제 슬슬 책 보고 공부해야지

[PICNIC](https://algospot.com/judge/problem/read/FESTIVAL) : 2019.03.30.

- 완전탐색 하는 문제(수가 작다)
- 그런데, 생각보다 엄청 어려움..
- 쉬움이라고 적혀있는데, 기초가 많이 부족한것같다

[QUADTREE](https://algospot.com/judge/problem/read/QUADTREE) : 2019.03.31.

- 재귀로 슥슥 풀리는 문제였다
- 나는 귀찮아서 대충 문자열 잘라서 했는데, 인덱스로 했으면 좀더 편하게 됐을듯
- 또, 4개밖에 안되는건데 반복문 썼다
  - 그냥 나열하는게 더 보기 좋을수도
  - 숫자 고정되어있는건 그러는게 좋겠다!

## swexpertacademy.com

[1244. 최대 상금](https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15Khn6AN0CFAYD) : 2019.01.01.

- 자릿수를 주어진 횟수만큼 바꾸며 나오는 최대 숫자를 찾는 것
- 친구가 풀어보래서 간단하게 풀어봤다
- set으로 문자열 그냥 전부다 넣어보면서 해봄..
- 숫자가 조금만 더 길어지면 안될 것 같다.

## [Google Kickstart](https://codingcompetitions.withgoogle.com/kickstart)

[Big Buttons](https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ee2/0000000000051136) : 2019.02.26.

- 주어진 prefix 없이 만들 수 있는 문자열의 갯수를 구하는 문제
- 천천히 생각부터 하고 코딩했으면 빨리 풀었을텐데, 그냥 무작정 손대서 오래걸렸다..
- 종이 가지고다니면서 적으면서 생각해보자
- 또, 출력 형식 틀려서 틀림..
  - 조심합시다

[2019 Round A](https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050e01)

- Training
  - 정렬하고 슬라이딩윈도우처럼 쭉쭉 계산했다
  - 그런데, 테스트 출력 안지우고 풀어서 한번 틀림..
- Parcels
  - 잘 하다보니까 작은건 풀렸는데, 큰건 도저히 안되는듯
  - 공부 열심히하자
- Contention
  - 손도 못댔다. 공부가 더 필요합니다..
  - 전체에서 10명이 스몰 풀었고, 2명이 라지까지 다 풀었다

## [Google Codejam](https://codingcompetitions.withgoogle.com/codejam)

[Qualification Round 2019](https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705)

- 1번 2번 문제는 hidden까지 다 맞았고, 3번 4번은 다 틀렸다
  - 결과는 41점. 그래도 예전 생각하면 나쁘지 않다!
  - 3번 조금만 더 생각했으면 훨씬 잘나왔을텐데 아깝다..
- Foregone Solution
  - 주어진 숫자를 둘로 나누는데, 결과에 4가 없게 만드는 문제
  - 그냥 뒷자리부터 하나씩 올리면서 보다가 4 있으면 반으로 나눴다
  - 쉬운데, 정해진 답이 하나가 있는게 아니라서 조금 당황
- You Can Go Your Own Way
  - 다른 사람이 간 길을 따라서 가지 않는 문제
  - 이것도 정답이 딱 정해진게 아니라, 적당히 되는거 만드는거라 당황함
  - 그래도 그냥 케이스 나누니까 생각보다 엄청 쉬웠다
- Cryptopangrams
  - 쉬운 문제였는데, 런타임 에러가 난 부분을 못찾아서 결국 못풀었다
  - 첫부분에 똑같은 숫자가 나와버릴수도 있다는걸 못찾았음..
  - 맨 뒤에 똑같은 숫자 여러개 붙여보긴 했는데, 왜 생각을 못했을까....
  - 문제 자체는 재미있게 풀었다
  - 끝나고 제출하니까 깔끔하게 맞았다
  - 예외 케이스 더 생각하자..
- Dat Bae
  - 아예 건드리지도 못했다. 그런데, 그냥 알고리즘 문제가 아니라 무슨 인터페이스가 있는 문제인듯

[Round 1A 2019](https://codingcompetitions.withgoogle.com/codejam/round/0000000000051635)

- Pylons는 작은거, AlienRhyme은 작은거 큰거 다 맞았다.
  - 등수 별로 안될줄 알았는데, 그래도 꽤 높게 나옴!
- Pylons
  - 백트래킹으로 대충 해봤는데 숫자가 7~8이 되니까 너무 느려졌다
  - 아쉽지만 그래도 작은거라도 풀어서 다행
- Golf Gophers
  - 인터랙션 하는건 솔직히 금방 하겠는데, 어떻게 풀지 아예 모르겠어서 놔뒀다
  - 랜덤하게 돌린다니까 작은 케이스도 생각이 안남..
- Alien Rhyme
  - 트라이 생각나서 뒤집고 트라이 만드니까 금방 풀렸다

[Qualification Round 2020](https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27)

- f스트링 쓰다가 파이썬 버전안맞아서 RE나왔다. 버전 확인하기
- 이번에 `break`때문에 시간을 너무많이썼다
  - 코드 다시볼때 우선 볼 것
- Vestigium
  - 그냥 시키는대로 하면 풀리는 것
- Nesting Depth
  - 그냥 앞에서 쭉 훑으면서 하면 됨
- Parenting Partnering Returns
  - `break` 안써서 한참 못찾았다
    - 테스트케이스가 돌아가서 더 한참찾았다
  - 3개짜리에서는 어려울것같음
  - 이런 시간같은거 나오면 시작/끝 시간으로 뭐 할수없나 먼저 생각해보자
- ESAb ATAd
  - 한참걸렸는데, 규칙찾는게 나한테는 어려웠다
  - inverse시키는거랑 reverse시키는거 찾는건 다음에 보면 못볼것같다
  - 맨앞 맨뒤 맞춰놓고 점점 늘려나가는법 찾는거 잘한것같다
  - interactive 처음풀어봤는데, 재미있다
  - `break` 위치 틀려서 한참삽질했다
    - interactive라서 디버깅이 좀 어려웠음
    - stderr 잘 써서 디버깅하기
- Indicium
  - Vestigium 반대로 하는것?
  - 천천히 풀면 할수도 있을것같은데, 이런식으로 푸는건 내가 잘 못함
  - 시간날때 풀어봐야겠다

## [codeforeces](https://codeforces.com)

[Round#552](https://codeforces.com/contest/1154)

- 처음 해본 codeforce였는데, 재미있었다.
  - 시간이 늦어서 절반쯤 풀다 잠.
  - 근데 더 했어도 아마 비슷했을듯. 쉬운것만 풀었다.
  - ABCD 풀고 E 시간초과, FG는 안건드렸다.
- 여러 자료구조 생각해보게 돼서 좋은것같다.
- 꾸준히 연습해볼 것.
