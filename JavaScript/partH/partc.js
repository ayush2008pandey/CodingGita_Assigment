// question 11

console.log("5" + 3 + 2);
// 57
console.log(5 + 3 + "2");
// 82
console.log("5" - 3 + 2);
// 4
console.log(5 - "3" + "2");
// 22


// question 12

console.log(true + true);//2
console.log(true + false);//1
console.log(true + "false");//truefalse
console.log(false + "true");//flasetrue


// question 13

console.log(null + 5);//5
console.log(undefined + 5);//NaN
console.log(null + "5");//null15
console.log(undefined + "5");//undefined15


// question 14

console.log([] + []);
//
console.log([] + {});
// [object Object]

console.log({} + []);
// [object Object]

console.log({} + {});

//[object Object][object Object]


// question 15

let a = "10";
let b = 5;
let c = a + b;
let d = a - b;
let e = +a + b;
console.log(c, typeof c);
console.log(d, typeof d);
console.log(e, typeof e);

// 105 string
// 5 number
// 15 number

// question 16

console.log(!!"Hello");
console.log(!!"");
console.log(!!0);
console.log(!!1);
console.log(!!null);
console.log(!!undefined);

// true
// false
// false
// true
// false
// false

// question 17 

console.log(Number(""));
console.log(Number(" "));
console.log(Number("0"));
console.log(Number("  25  "));
console.log(Number("25px"));

// 0
// 0
// 0
// 25
// NaN

// question 18 


let val1 = "5";
let val2 = 2;
console.log(val1 + val2);
console.log(+val1 + val2);
console.log(val1 - val2);
console.log(val1 * val2);
console.log(val1 / val2);

// 52
// 7
// 3
// 10
// 2.5

// Bonus Mixed Practice Questions:

// questions 19 

let count = 5;
console.log(typeof count++);
console.log(count);
console.log(typeof ++count);
console.log(count);

// number
// 6
// number
// 7

// question 20 

let x = "10";
let y = ++x;
console.log(x, y, typeof x, typeof y);

// 11 11 number number


// questions 21

let a = "5";
let b = a++;
console.log(a, b, typeof a, typeof b);


// 6 5 number number

// question 22

console.log(typeof (1 + "2"));
console.log(typeof (1 - "2"));
console.log(typeof (1 * "2"));
console.log(typeof (1 / "2"));

// string
// number
// number
// number

// questions 23

let val = null;
console.log(typeof val);
console.log(val + 1);
console.log(val - 1);
console.log(val * 1);
console.log(Boolean(val));


// object
// 1
// -1
// 0
// false

