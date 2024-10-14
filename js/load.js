


function creatHeader(){
    let headContent = document.createTextNode("V O C A L A S S I S T A N T")
    let header = document.createElement("header")
        header.setAttribute("class", "bg-blue-500 h-20 text-white border-2 border-black")
    let heaDiv = document.createElement("div")
        heaDiv.setAttribute("class", "container mx-auto border-2 border-black text-xl italic font-bold mt-3 pt-2 pb-2 text-center rounded-3xl")
    //let headAside = document.createElement("aside")
    
    let body = document.querySelector("body")
    let main = document.querySelector("main")
        
        heaDiv.appendChild(headContent)
        header.appendChild(heaDiv)
        body.appendChild(header)
        document.body.insertBefore(header, main)
        console.log(header)
}creatHeader()



function creatFooter(){
    let footer = document.createElement("footer")
        footer.setAttribute("class", "bg-grey-800 text-white border-2 border-black")
    let footDiv = document.createElement("div")
        footDiv.setAttribute("class", "container mx-auto flex justify-center items-center border-2 border-black rounded-3xl bg-blue-400")
    let footAside = document.createElement("aside")
    let headImg = document.createElement("img")
        headImg.setAttribute("class", "rounded-full pl-2 pr-2")
        headImg.setAttribute("src", "/img/img_bot_ban.png")
        headImg.setAttribute("alt", "bot_ban")
    let body = document.querySelector("body")
        footAside.appendChild(headImg)
        footDiv.appendChild(footAside)
        footer.appendChild(footDiv)
        body.appendChild(footer)
        console.log(footer)
}creatFooter()