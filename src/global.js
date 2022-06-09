

export async function callAPI(method , dict)
{
    const url = 'https://tranquil-brook-75958.herokuapp.com/' + method + "?";
    const esc = encodeURIComponent;
    const query = Object.keys(dict).map(k => `${esc(k)}=${esc(dict[k])}`).join('&');
    const res = await fetch(url+query);
    return await res.json();
}