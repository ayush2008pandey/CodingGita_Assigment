// question 01 

for (let i = 1 ; i<=15 ; i++){
    console.log(i)
}


// question 02 

for (let i =2 ; i<=40; i++){
    if (i%2==0)(
        console.log(i)
    )
}


// question 03 

for (let i = 1 ; i<=35 ; i++){
    if(i%2==1)(
        console.log(i)
    )
}



// question 04 


let total_Saving = 0
let dailySaving = 0 

for (let day = 1 ; day<=10 ; day++ ){
    dailySaving= day*10
    total_Saving+=dailySaving    
}
console.log(`total savings after10 days: ${total_Saving}`)



// question 05 

let num = 12 
for (let i =1 ; i<=10 ; i++){
    console.log(`${num} x ${i} = $[num*i]`)
}


// question 06 

let glassOfWater = 3
let glassOfWaterNextDAy = 0
for (let day = 1 ; day<=7; day++ ){
    glassOfWaterNextDAy = day*glassOfWater
    console.log(`Day${day} : ${day*glassOfWater} glasses`)    
}

// question 07 

let chocolateCost = 15
let NoChocolateCost  = 0
for (let chocolate = 1 ; chocolate<=10 ; chocolate++){
    NoChocolateCost = chocolateCost*chocolate
    console.log(`${chocolate} chocolate = ${NoChocolateCost}`)

}



// question 08 

let count = 0
for (let i=1 ;i<=30 ; i++){
    if (i%2==0){
        count+=i
    }
}
console.log(count)



// question 09


let pushUp = 5
let dailypushUp = 0
for(let day=1;day<=7 ;day++ ){
    dailypushUp =pushUp*day
    console.log(`Day ${day}: ${dailypushUp} push-ups`)
}


// question 10


let ticketCost = 150
let personTicketCost = 0
for(let person= 1 ;person <=8 ; person++){
    personTicketCost = ticketCost*person
    console.log(`${people} person: $${personTicketCost}`)
}