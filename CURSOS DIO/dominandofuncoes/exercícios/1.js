const alunos=[
    {
        nome:"Joao",
        nota:5,
        turma:"18",
    },
    {
        nome:"Sofia",
        nota:9,
        turma:"18",
    },
    {
        nome:"Paulo",
        nota:6,
        turma:"20",
    }
]
function alunosAprovados(array, media) {
    let aprovados=[]
    for (let i = 0; i < array.length; i++)
     {
        const {nota,nome} = array[i];
        if (nota>=media) {
            aprovados.push(nome)
        }
    }
    return aprovados
}
console.log(alunosAprovados(alunos, 10))