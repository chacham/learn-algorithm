/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
    const roman =   ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    const integer = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    let result = '';
    for (let i = 0; i < roman.length; i++) {
      while (num >= integer[i]) {
        result += roman[i];
        num -= integer[i];
      }
    }
    return result;
};