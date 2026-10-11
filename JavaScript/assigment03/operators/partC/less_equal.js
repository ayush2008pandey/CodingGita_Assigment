// question 1
console.log(60 <= 60); // true

// quesstion 2 
console.log(39 < 40); // true (failed)


// question 3

console.log(15 <= 20); // true
console.log(20 <= 15); // false
console.log(15 <= 15); // true


// question 4

console.log("15" <= 20);  // true
console.log("30" <= "5"); // true
console.log(null <= 0);   // true

// question 5

// undefined <= 0 returns false because undefined converts to NaN, and comparisons involving NaN always return false.


// question 6

console.log(10 < 10); // false 


// question 7

console.log(false <= 0); // true
console.log("" <= 0);    // true
console.log(NaN <= 5);   // false
