import { get } from "svelte/store";
import {token} from "./stores/store.js";

export async function callAPI(method , dict)
{
    
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


export async function downloadFile(file) {
    var req = new XMLHttpRequest();
    req.open("GET", "https://tranquil-brook-75958.herokuapp.com/download?" + "token=" + get(token) + "&fileID=" + file["id"], true);
    req.responseType = "blob";
    req.onload = function (event) {
        var blob = req.response;
        var link=document.createElement('a');
        link.href=window.URL.createObjectURL(blob);
        link.download=file["name"];
        link.click();
    };

    req.send();
}