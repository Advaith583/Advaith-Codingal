class Person{
    constructor(name,age,skills){
        this.name=name
        this.age=age
        this.skills=skills
    }
    speak(){
        console.log(`${this.name}is speaking`)
    }
    Walk(){
        console.log(`${this.name}is walking`)
    }
    details(){
        console.log(`Name of the person is ${this.name} and age is ${this.age} and skills are ${this.skills}`)
    }
}
class smartPerson extends Person{
    Study(){
        console.log("8 hours of study every day")
    }
}
const human2=new Person("Advaith",15,"MERN")
const smarthuman2=new smartPerson("Advaith,15","Cricket")


human2.details()
human2.speak()