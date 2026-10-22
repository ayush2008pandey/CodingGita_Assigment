// question 01 

let num = 34
if(num>10){
    if(num%3==0){
        console.log("no is devisible by 3")
    }
}else{
    console.log("nothing")
}


// question 02

let personAge = 19
let voter_Id = true

if(personAge>=18){
    if(voter_Id){
        console.log("Can Vote")
    }
}


// question 03

let marks  = 90 
if(marks>=40){
    if(marks>=80){
        console.log("Passed with Distinction")
    }
}


// question 04

let Pin = true 
let amountbalance =500
let amountEnter = 45
if(Pin){if(amountbalance>=amountEnter){
    console.log("withdrawal amount")
}

}


// question 05

let year = 2026
if(year%4==0){
    if(year%100){
        if(year%400){
           console.log("leap year")
        }
    }
}


// question 06


const email = "user@example.com".trim();


if (email.includes("@")) {

  if (email.endsWith(".com")) {
    
    if (email.length > 10) {
      console.log("Valid Email");
    }
  }
}


// question 07

let cartValue = 5000
let premiuMember =true
let cartTotal = 1000
if(cartValue>=cartTotal){
    if(premiuMember){
        console.log("20% discount")
    }
    else {
        console.log("10% discount")
    }
}


// question 08

let num_1 = 22
if(num_1>=0){
    if(num_1%2==0){
        if(num_1%4==0){
            console.log("Positive Even and Divisble by 4")
        }
    }
}



// question 09

let age  = 23
let graduationDedree = true
let experience = 3
if(age>21 && age<=30){
    {
        if(graduationDedree){
            if(experience>=2){
                console.log("Eligible for Interveiw")
            }
        }
    }
}


// question 10

let studenPresent = true
let InternalMarks = 31
let externalMarks = 36
if(studenPresent){
    if(InternalMarks>=30){
        if(externalMarks>=35){
            console.log("eligible for final exam")
        }
    }
}

