

export async function callAPI(method , dict)
{
    if(method == "getFilesList")
    {
        return {"status" : "accepted", "files" : [{"name" : "Main.java" , "id" : "21h09fh"} , {"name" : "Ficheiro 1" , "id" : "fnoi342fn"} , {"name" : "ficheiro 3" , "id" : "nf3io2n"}]};
    }
    const url = 'https://tranquil-brook-75958.herokuapp.com/' + method + "?";
    const esc = encodeURIComponent;
    const query = Object.keys(dict).map(k => `${esc(k)}=${esc(dict[k])}`).join('&');
    const res = await fetch(url+query);
    return await res.json();
}

export async function postAPI(method , dict)
{
    const url = 'https://tranquil-brook-75958.herokuapp.com/' + method;
    const res = await fetch(url , {
    'method' : 'POST',
    body: JSON.stringify(dict)});
    return await res.json();
}