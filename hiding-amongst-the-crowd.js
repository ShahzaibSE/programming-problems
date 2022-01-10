// What's Hiding Amongst the Crowd?

function detectWord(str) {
    var regex = /[a-z]/g
    console.log(`String: ${str}`)
    console.log(str.match(regex).join(""))
}

detectWord("UcUNFYGaFYFYGtNUH")