// // JSON
// const student={
//     name: "Student",
//     age: 15,
//     subjects:["Maths","Science"],
// };


// //convert objects to JSON
// const studentJSON = JSON.stringify(student);
// console.log("JSON Format:",studentJSON);


// const studentObj = JSON.parse(studentJSON);
// console.log("Java script Object:",studentObj);

// function add(a,b){
//       return a+b
//     }
//     function sum(a,b,callback){
//         return callback(a,b)
//     }

//     let ans = sum(10,20,add)
//     console.log(ans)

async function CallApi(){
    let raw = await fetch(`https://randomuser.me/api`);
    let ans = await raw.json()

    console.log(ans)
    
}
CallApi()
