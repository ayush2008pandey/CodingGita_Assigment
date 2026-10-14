// question 1
 
let passwordCorrect = true
let otpValid = false  
 

let loginAllowed = passwordCorrect || otpValid
console.log("if login is allowed",loginAllowed )



// question 2


let isMember  = false
let hasCoupon  = true

let discountApplies = isMember||hasCoupon
console.log("A discount applies",discountApplies)


// question 3

let age = 16  
let height = 155
if(age==18 || height==150){
    console.log("Entry is allowed")
}
else{
    console.log("Entry not allowed")
}



// question 4 


let emailGiven = true 
let phoneGiven = false 
let formValid  = emailGiven||phoneGiven
console.log("A form is valid",formValid)



// question 5 
let score = 900 
let  timeBonus = true 
if(score>1000 || timeBonus==true){
    console.log("A given Level open")
}
else{
    console.log("game level not open")
}


// Additional Questions (Logical OR ||)


// question 6 


// let a = 0;
// let b = false;
// let c = "";
// let d = null;
// let e = 42;
// let result = a || b || c || d || e;
// console.log(result);

// // 42

// // question 7


// let x = "Hello" || 0;
// let y = 0 || "Hi";
// console.log(x, y);

// // Hello Hi


// // question 8

// let a = 10;
// let b = 20;
// let result = (a < 5) || (b > 15);
// console.log(result);

// // true

// // question 9 

// let val = 5;
// let condition = val || (val = 0);
// console.log(condition);
// console.log(val);

// // 5
// // 5


// // question 10 

// let x = "" || 0 || false || null || undefined || "OK";
// console.log(x);

// // OK


