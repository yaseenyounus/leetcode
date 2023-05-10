function isPalindrome(x: number): boolean {
  const strX: string = x.toString();
  let end: number = strX.length - 1;

  for (let z = 0; z < strX.length; z++) {
    if (strX[z] !== strX[end - z]) {
      return false;
    }
  }
  return true;
}

console.log(isPalindrome(121));
console.log(isPalindrome(-121));
console.log(isPalindrome(10));
