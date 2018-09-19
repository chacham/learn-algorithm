function solution(arrangement) {
    let answer = 0;
    let stack = [];
    let last = ''
    for (let i in arrangement) {
        if (arrangement[i] == '(') {
            stack.push('(');
        } else if (last == '(') {
            stack.pop();
            answer += stack.length;
        } else {
            stack.pop();
            answer += 1;
        }
        last = arrangement[i];
    }
    return answer;
}

s = "()(((()())(())()))(())";
console.log(solution(s));