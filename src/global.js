

export async function callAPI(method , dict)
{
        const res = await fetch('https://tranquil-brook-75958.herokuapp.com/login' , {
            method: 'GET',
            params : dict
        });

        return await res.json();
}