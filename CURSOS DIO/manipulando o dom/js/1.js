function changeMode(params) {
    changeClasses()
    
}
function changeClasses(params) {
    h1.classList.toggle("dark-mode")

    button.classList.toggle("dark-mode")

    footer.classList.toggle("dark-mode")

    body.classList.toggle("dark-mode")
}

function changeText() {
    const lightMode='Light Mode'
    const darkMode='Dark Mode'

    if (body.classList.contains("dark-mode")) {
        button.innerHTML=lightMode
        h1.innerHTML=darkMode+" ON"
        return
    }
    button.innerHTML=darkMode
    h1.innerHTML=lightMode+" ON"
}

const button=document.querySelector("#mode-selector")
button.addEventListener("click", changeMode)

const h1=document.querySelector("#page-title")

const body=document.querySelector("body")

const footer=document.querySelector("footer")

