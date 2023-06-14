//Se eu puser apenas uma variável, ela não poderá ser array
//com o "SPREAD" eu consigo por uma quantia toa grande quanto eu quiser ser variáveis como parâmetros, elas se tornaram arrays

function confereArgs(...args) {
    console.log(args.length)
}

confereArgs(1,2,3,3,4,5)


//Object Destructing
//Criei uma array
const user={
    id:"2",
}

//Criei uma função que fala assim ó: procura pelo parametro. Que parâmetro? O id da array que nos derem quando for chamado e devolto o valor da id
function userId({id}) {
    return id
}
console.log(userId(user))