// question 01

let Months = 12;
switch(Months) {
    case 1:
        console.log("31 Days")
        break;
    case 2:
        console.log("28 ays")
        break;
    case 3:
        console.log("31 Days")
        break;
    case 4:
        console.log("30 Days")
        break;
    case 5:
        console.log("31 Days")
        break;
    case 6:
        console.log("30 Days")
        break;
    case 7:
        console.log("31 Days")
        break;
    case 8:
        console.log("31 Days")
    case 9:
        console.log("30 Days")
    case 10:
        console.log("31 Days")
    case 11:
        console.log("31 Days")
    case 12:
        console.log("31 Days")
    default:
    console.log("invalid day")
}


// question 02

let char  = "a"
switch(char.toLowerCase()){
    case "a":
    case "b":
    case "c":
    case "i":
    case "0":
    case "U":
        console.log(`${char} is a vowel`)
        break
    default:
        if (char.toLowerCase()>="a" && char.toLowerCase()<="z"){
            console.log(`${char} is s Consosant`)
        }
        else{
            console.log(`${char} is not an alphabet letter`)
        }
}




// question 03

let num = 4
switch(num){
    case 1 || 2 :
        console.log("Winter")
            break
    case 3 || 4 :
        console.log("Summer")
            break
    default:
        console("invalid num")
}



// question 04 


let marks  = 50 
switch(true){
    case marks >=75:
        console.log("Distinction ")
        break
    case marks >=60 :
        console.log("1st class")
        break
    case marks >= 50 :
        console.log("2nd class")
        break
    case marks >= 35:
        console.log("3rd class")
        break
    case marks <35 :
        console.log("failed")
        break
    default :
        console("invalid")
    
}


// question 05 

let role  = "admin"
let action = "edit"
switch (role.toLowerCase){
    case admin:
        switch(action.toLowerCase){
            case create :
                console.log("resource created ")
                break
            case edit:
                console.log("edit resource")
                break
            case Delete:
                console.log("delete resource")
                break
            default:
                console.log("invalid")
        }
        break
        case user :
            console.log("LImited Access")
            break
        default:
            console(
                "invalid"
            )
}


// question 06


let fruit = "mango";

switch (fruit) {
  case "apple":
    console.log("Apple is red");
  case "mango":
    console.log("Mango is yellow");
  case "banana":
    console.log("Banana is yellow");
  default:
    console.log("Unknown fruit");
}

// Mango is yellow
// Banana is yellow
// Unknown fruit



// question 07 

let num_string  = flase 
switch(num_string){
    case 0 :
        console.log("integer")
        break
    case "0":
        console.log("string")
        break
    case false:
        console.log("boolean")
        break
    case null :
        console.log("null")
        break
    case undefined :
        console.log("undefined")
        break
    default :
        console.log("invalid")

}


// question 08 


let num_1 = 2
let num_2 = 3
let operators = "+"
let result 
switch (operators){
    case "+":
        result = num_1+num_2
        break
    case "-":
        result = num_2 - num_1
        break
    case "*":
        result = num_1*num_2
        break
    case "/":
        result = num_1/num_2
        break
    case "%":
        result = num_1%num_2
        break
    case "**":
        result = num_1**num_2
        break

    default:
        console.log("invalid")
}


// question 09

let date = 22
switch(true){
    case date>= 1 && date <=10:
        console.log("Beginning of the month")
        break
    case date>=11 && date<=20:
        console.log("Middle of the month ")
        break
    case date >=21 && date<=31:
        console.log("End of the month")
        break
    default:
        console.log("invalid")


}

// question 10


let category = "veg"
let size = "full"
switch(category){
    case veg :
        switch(size){
            case full :
                console.log("veg full 120 rs")
                break
            case half :
                console.log("veg full 220rs")
                break
        }
        break
    case non_veg :
        switch(size){
            case full :
                console.log("veg full 120 rs")
                break
            case half :
                console.log("veg full 220rs")
                break
        }
        break
    default:
        console.log("invalid")

}
