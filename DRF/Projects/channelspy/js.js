document.getElementById('').onclick = () =>{
    const meginputv = document.getElementById('').value
    wc.send(JSON.stringify({
        'mg':meginputv
    }))
}