if (true){
    let a = "Advaith"   
    a=20
    console.log(a)
}
if (true){
    const b = "Advaith"   
  
    console.log(a)
}
function parent(){
    var a=10
    function child(){
        var b=30
        console.log("printing the value of a from child:",a)
        function superchild(){
            console.log("Print function of b from super child:",b)
        }
        superchild()
    }
  console.log("Printing value of a from from parent function:",a)
    
  child()
}
parent()

function greet(){
    
}

   
     