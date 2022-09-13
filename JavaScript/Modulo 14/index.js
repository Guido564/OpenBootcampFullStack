const boton = document.querySelector('#btn')

boton.addEventListener('click', () => {
    alert('Ohhh has hecho click!')
})

$(() => {
    $('#btn-jq').click(() => {
        // $("h1").hide()
        $('h1').fadeOut()
    })

    $('#btn-jq').click(() => {
        // $("h1").show()
        $('h1').fadeIn()
        $('h1').css({ color: 'red' })
    })
})