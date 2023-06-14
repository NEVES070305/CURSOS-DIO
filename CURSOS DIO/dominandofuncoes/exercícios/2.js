function calculaIdade(anos) {
    return` Daqui a ${anos} anos, ${this.nome} terá ${this.idade+anos} anos de idade. `
}
const pessoa1={
    nome: "MARIA",
    idade:70,
}

console.log(calculaIdade.call(pessoa1,30))