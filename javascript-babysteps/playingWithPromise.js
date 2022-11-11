function generatePromise(age){
    return new Promise((resolve, reject)=>{
        if(age>18){
            resolve('Give Netflix subscription')
        }else{
            reject('Netflix - Subscription request rejected: ', age)
        }
    })
}

function createAccount(userAge){
    generatePromise(userAge).then(data => {
        console.log(data)
    }).catch(err => {
        console.log(err)
    })
}

createAccount(20)