names = ['jackson', 'jacque', 'jack']
queries = ['jack']

// for(let i=0; i<names.length; i++){
//     let split_name = names[i].split("")
//     for(let j=0; j<split_name.length; j++){
//     }
//     console.log("")
// }
function prefixSearch(names, queries) {
    let prefix_counter = 0;
    names.forEach((name) => {
        let prefix_counter = 0;
        let split_name = name.split("")
        queries.forEach((query) => {
        let split_query = query.split()
            if(split_query.length == split_name.length){
                console.log("Query and names match so cannot test.")
            }else {
                for(let i=0; i<split_query.length; i++){
                    if(split_query[i] == split_name[i]){
                        prefix_counter++ 
                    }
                }
                console.log(prefix_counter)
            }
        })
    })
    console.log(prefix_counter)
    return prefix_counter
}

prefixSearch(names, queries)



