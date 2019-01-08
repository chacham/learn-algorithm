/**
 * @param {string} S
 * @return {string}
 */
var reverseOnlyLetters = function(S) {
  const lowerMin = 'a'.charCodeAt(0);
  const lowerMax = 'z'.charCodeAt(0);
  const upperMin = 'A'.charCodeAt(0);
  const upperMax = 'Z'.charCodeAt(0);
  function isLetter(c) {
    return (c.charCodeAt(0) >= lowerMin && c.charCodeAt(0) <= lowerMax)
      || (c.charCodeAt(0) >= upperMin && c.charCodeAt(0) <= upperMax);
  }
  const chars = Array.from(S);
  const letters = chars.filter(isLetter);
  return chars.map(c => isLetter(c) ? letters.pop() : c).join('');
};

console.log(reverseOnlyLetters("a-bC-dEf-ghIj"));