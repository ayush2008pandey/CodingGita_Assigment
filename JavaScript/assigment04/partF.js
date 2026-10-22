// question 01

let num = 14
let divisible = num%7==0?"Devisible by 7 ":"not divisible by 7 "
console.log(divisible)

// question 2

let tem = 31 
let check = tem>=30?"hot day":"Pleasant day"
console.log(check)


// question 3

let string = ""
console.log(string===""?"empty string":"string has content")

// question 4 

let age  = 18
let result = age<13?"child":age>=13 && age<=19?"teenager":"adult"
console.log(result)


// question 5

let a =1 ,b =2 , c= 3
let greatest = a>b && a>c ?"a is greates":b>a && b>c ?"b is greatest":c>a && c>b ?"c is greatest":"all are equal"
console.log(greatest)


// question 6 

let mark = 88
let classifies = makrs>=75?"Distinction":makrs>=60 && makrs<=74?"First class":makrs>=50 && makrs<=59?"Second class":makrs>=35 && marks<=49?"pass":"fail"
console.log(classifies)


// question 07 

let no = 78
let no_return = no==0?"Zero":n0>0?(no%2===0?"Positive no ":"positive odd"):(no%2===0?"Negative Even":"negative odd")
console.log(no_return)

// question 08

let year = 2026
let leap_year = year%4==0?((leap_year%100==0 )?(( leap_year%400==0)?"lear year":"not a leap year"):"leap_year"):"not a leap_year"
console.log(leap_year)


// question 09 

// if (role === "admin") {
//   if (action === "delete") → "Admin Delete"
//   else if (action === "edit") → "Admin Edit"
//   else → "Admin Other"
// } else if (role === "user") {
//   if (action === "view") → "User View"
//   else → "User Restricted"
// } else {
//   → "Invalid Role"
// }


let role = "admin"
let role_check = role==="admin"?(action=="delete"?"Admin delete":action==="edit"?"Admin edit":"admin other"):role==="user"?(action==="view"?"user veiw":"user Restricted"):"invalid role"
console.log(role_check)


// question 10 

let cartTotal = 3500;

let discount = cartTotal >= 5000
  ? { discountPercent: 20, finalAmount: cartTotal * 0.8 }
  : cartTotal >= 2000
    ? { discountPercent: 10, finalAmount: cartTotal * 0.9 }
    : cartTotal >= 1000
      ? { discountPercent: 5, finalAmount: cartTotal * 0.95 }
      : { discountPercent: 0, finalAmount: cartTotal };

console.log(result); 
