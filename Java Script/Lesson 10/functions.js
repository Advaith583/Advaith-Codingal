// function sum(a,b){
//     return a+b
// }
 
// let sum2= function(a,b){
//     return a+b
// }
// let sum3= (a,b) => a+b

// let ans= sum(10,20)
// let ans1= sum2(18,20)
// let ans2= sum3(10,980)

// console.log(ans)
// console.log(ans1)
// console.log(ans2)

// try{
//     let num=10;
//     console.log(num/a);

// } catch (error){
//     console.log("An error has occured":error.msg);
// }

try{
    let json= '{"name":"John"}';
    let user= JSON.parse(json);
    console.log(user.name);

    let invalidjson="{name:'John'}";
    JSON.parse(invalidjson);


} catch(error){
    console.log("hey an error occured:", error.msg);
}