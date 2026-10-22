// question 01 

let month=7
let season

if (month==12 ||month==1||month==2){
    season="winter"
}
else if(month==3 ||month==4||month==5){
    season="summer"
}
else if(month==6 ||month==7||month==8){
    season="Monsoon"
}
else{
    season="Autumn"
}

console.log(season)


// question 02

let income = 350000
let SimpleTax 
if(income<300000){
    SimpleTax=0
}
else if(income>300000 && income<700000){
    SimpleTax=5
}
else if(income>700000 && income<1000000){
    SimpleTax=10 
}
else{
    SimpleTax=15 
}

console.log(`${SimpleTax}% Tax`)
let tax = income%SimpleTax
console.log(`the tax amount is ${tax} `)


// question 03


let studentScore = 91

if(studentScore>=90){
    console.log("Outstanding")
}
else if (studentScore>70&&studentScore<89){
    console.log("Good")
}
else if(studentScore>40 && studentScore<69){
    console.log("Needs Improvement")
}
else{
    console.log("Needs improvement")
}


// question 04


let vehicleSpeed = 90
if(vehicleSpeed<40){
    console.log("Slow")
}else if(vehicleSpeed>=40 && vehicleSpeed<80){
    console.log("Normal")
}
else{
    console.log("fast")
}


// question 05 

let personHeight = 179
if(personHeight<150){
    console.log("Short")
}else if(personHeight>=150 && personHeight<170){
    console.log("Average")
}


// question 06 

let Daynum = 3
if (Daynum>=1 && Daynum<=5){
    console.log("Weekday")
}
else if(Daynum>=6 && Daynum<=7){
    console.log("Weekend")
}
else{
    console.log("invlaid Day no ")
}


// question 07 

let electriBill = 54
let billPerUnit 
if (electriBill>0 && electriBill<=50 ){
    billPerUnit=2
}
else if(electriBill >=51 && electriBill<=150){
    billPerUnit=4

}
else{
    billPerUnit=6
}
let totalBill = electriBill*billPerUnit
console.log(`the total electric bill is ${totalBill}`)



// question 08

let attendancePercentage  = 90
if(attendancePercentage>= 90){
    console.log("Excellent")
}
else if(attendancePercentage>=75 && attendancePercentage<=89){
    console.log("Good")
}
else if (attendancePercentage>=50 && attendancePercentage<=74){
    console.log("Satisfactory")
}else{
    "Poor"
}

// question 09 

let sub_1 = 88
let sub_2 = 78
let sub_3 = 50
if(sub_1>sub_2 && sub_1>sub_3){
    console.log(`Sub_1 ${sub_1}is  highest mark`)
}
else if (sub_2>sub_1 && sub_2>sub_3){
    console.log(`Sub_2 ${sub_2}is  highest mark`)
}else if(sub_3>sub_1 && sub_3>sub_2){
    console.log(`Sub_3 ${sub_3}is  highest mark`)
}

else{
    console.log("invalid")
}

// question 10 

let num_1   = 33 
if (num_1>=0){
    if(num%2==0){
        console.log("Positive Even")
    }else{
        console.log("Positve Odd")
    }

}
else if(num_1<0){
    if(num_1%2==0){
        console.log("Negative even")

    }
    else{
        console.log("Negative Odd")
    }
}else{
    console.log("Zero")
}

