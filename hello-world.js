console.log("Hello World")

function generateCounter() {
    let count = 0;
    //
    function increaseCount() {
         count++;
         console.log(count);
    }
    return increaseCount;
}

var getFn = generateCounter();
getFn()
getFn()