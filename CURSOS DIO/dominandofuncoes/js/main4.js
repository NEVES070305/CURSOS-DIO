const name={
    age: 13,
    height:1.68,
}

function getName(params) {
    console.log(this.age)//o this se refere a algo pelo qual eu vou buscar, mas naquilo que eu vou buscar nao é explícito, cabendo ao call, chamá-lo
}

getName.call(name)


//Bind
const retornaNomes= function (params) {
    return this.nome;//Olha, essa função tem nome, nome é característica da função
}

let bruno= retornaNomes.bind({nome:"Bruno"})// vai lá na constante retornaNomes e dá valor a sua propriedade chhamda nome e atribui a variável bruno
console.log(bruno())