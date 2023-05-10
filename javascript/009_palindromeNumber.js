function isPalindrome(x) {
  var strX = x.toString();
  var end = strX.length - 1;
  for (var z = 0; z < strX.length; z++) {
    if (strX[z] !== strX[end - z]) {
      return false;
    }
  }
  return true;
}
console.log(isPalindrome(121));
console.log(isPalindrome(-121));
console.log(isPalindrome(10));
