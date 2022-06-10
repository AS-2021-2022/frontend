

export async function callAPI(method , dict)
{
    if (method=="getWorkflows") {
        return {"workflows": [{"name": "Workflow 0", "id": 0, "pending": true}, {"name": "Workflow 1", "id": 1, "pending": false}], "status": "accepted"}
    }
    if (method=="getWorkflow") {
        return {"status" : "accepted" , "name" : "workflow name" , "progress" : 1 ,
        "steps" : [{"assignee_id" : "user1" , "description" : "In condimentum cursus velit a tristique. Etiam mollis efficitur risus faucibus convallis. Cras ornare ultrices vestibulum. Nullam dapibus tempus metus quis facilisis. Ut interdum eu massa molestie cursus. "} , {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}],
        "files" : ["file.txt", "file.txt"]};
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