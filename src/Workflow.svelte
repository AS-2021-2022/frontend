<script>
    import { afterUpdate } from "svelte";
    import {token, email , update_sidebard_flag} from "./stores/store.js";
    import { get } from "svelte/store";
    import {callAPI , downloadFile, postAPI} from "./global.js";
    export let workflowid;
    let cstep = 0;
    var last_id = -1;
    let state = "";
    const popovers = [];
    let createWorkflowFields = [];
    let apiResponse = undefined;
    let files

    function showPopover(index) {
        try {
            popovers[index].show()
        }
        catch {
            const exampleEl = document.getElementById('popover'+index);
            const popover = new bootstrap.Popover(exampleEl);
            popovers[index] = popover;
        
            popover.show();
        }
    }

    

    
    afterUpdate(async () => {
    
    if(last_id != workflowid)
    {
        createWorkflowFields = [];
        last_id = workflowid;
        if(workflowid == undefined) state = "write";
        else{
            state = "read";
            await getWorkflow();
        }
    }

    });

    async function createWorkflow()
    {
        let dict = {"token" : get(token) , "steps" : [] , "name" : ""};
        dict["name"] = document.getElementById("wname").value;
        for(let i=0;i<createWorkflowFields.length;i++)
        {
            let dest = document.getElementById("a"+i.toString()).value;
            let desc = document.getElementById("d"+i.toString()).value;

            dict["steps"].push({"id" : dest , "description" : desc});

        }
        let awnser = await postAPI("createWorkflow" , dict);

        if(awnser["status"] == "accepted")
        {
            //createWorkflowFields = [];
            //getWorkflow();
            update_sidebard_flag.set(true);
        }
        if(awnser["status"] == "rejected")
        {
            if(awnser["info"] != undefined) alert("Unable to submit workflow. Server response: " + awnser["info"]);
            else{
                alert("Unable to submit workflow");
            }
        }
    }

    async function getWorkflow()
    {
        var dict = {"token" : get(token), "id": workflowid};

        let answer = await callAPI("getWorkflow" , dict);

        if (answer["status"] == "accepted") {
            apiResponse = answer;
        }
        else{
            state = "write";
        }
    }

    async function incrementWorkflow()
    {
        cstep++;

        
            
            
        var fileid = await uploadFile();
        

        if(fileid != undefined)
        {
            let dict = {"token" : get(token) ,
                        "file"  : fileid ,
                        "id"    : workflowid};
            let awnser = await callAPI("incrementWorkflow" , dict);

            if(awnser["status"] == "accepted")
            {
                if (cstep > 1 && document.getElementById("popover" + String(cstep)).classList.contains("btn-outline-danger"))
                {
                    document.getElementById("popover" + cstep).classList.remove("btn-outline-danger");
                    document.getElementById("popover" + cstep).classList.add("btn-outline-success");
                }
                if (cstep > 1 && document.getElementById("popover" + (cstep)).classList.contains("btn-danger")) {
                    document.getElementById("popover" + cstep).classList.remove("btn-danger");
                    document.getElementById("popover" + cstep).classList.add("btn-success");
                }
                if (document.getElementById("popover" + (cstep-1)).classList.contains("btn-outline-success")) {
                    document.getElementById("popover" + (cstep-1)).classList.remove("btn-outline-success");
                    document.getElementById("popover" + (cstep-1)).classList.add("btn-outline-info");
                }
                if (document.getElementById("popover" + (cstep-1)).classList.contains("btn-success")) {
                    document.getElementById("popover" + (cstep-1)).classList.remove("btn-success");
                    document.getElementById("popover" + (cstep-1)).classList.add("btn-info");
                }
                alert("Workflow sucessfully incremented!");
                update_sidebard_flag.set(true);
                //getWorkflow(workflowid);
                afterUpdate.apply();
            }
            
        }
        
       
        
    }

    async function uploadFile()
    {
        let formData = new FormData();
        formData.append("file" , fileupload.files[0]);
        formData.append("token" , get(token));
        let awnser = await fetch('https://tranquil-brook-75958.herokuapp.com/upload', {
            method: "POST", 
            body: formData
        }); 

        

        awnser = await awnser.json();

        if(awnser["status"] == "accepted")
        {
            let fileid = awnser["id"];
            return fileid;
        }
        else{
            return undefined;
        }

    }

    

</script>

<main style="text-align:initial">

    {#if state == "read" && apiResponse != undefined}
        <div class="container-fluid mt-5" style="height: 11.5vh;  overflow-x: auto; overflow-y: hidden">

        <div class = "box">

            {#each apiResponse["steps"] as step , index}
            <div style="display: inline-block">
                {#if index < apiResponse["progress"]}
                    {#if step.id==get(email)}
                    <a tabindex="0" id="popover{index}" style="border-radius: 50%;" class="btn btn-lg btn-info" role="button" data-bs-toggle="popover" data-bs-placement="bottom" data-bs-trigger="focus" title="Assignee: {step.id}" on:click={() => showPopover(index)} data-bs-content="{step.description}">{index}</a>
                    {:else}
                    <a tabindex="0" id="popover{index}" style="border-radius: 50%;" class="btn btn-lg btn-outline-info" role="button" data-bs-toggle="popover" data-bs-placement="bottom" data-bs-trigger="focus" title="Assignee: {step.id}" on:click={() => showPopover(index)} data-bs-content="{step.description}">{index}</a>
                    {/if}
                {:else if index == apiResponse["progress"]}
                    {#if step.id==get(email)}
                    <a tabindex="0" id="popover{index}" style="border-radius: 50%;" class="btn btn-lg btn-success" role="button" data-bs-toggle="popover" data-bs-placement="bottom" data-bs-trigger="focus" title="Assignee: {step.id}" on:click={() => showPopover(index)} data-bs-content="{step.description}">{index}</a>
                    {:else}
                    <a tabindex="0" id="popover{index}" style="border-radius: 50%;" class="btn btn-lg btn-outline-success" role="button" data-bs-toggle="popover" data-bs-placement="bottom" data-bs-trigger="focus" title="Assignee: {step.id}" on:click={() => showPopover(index)} data-bs-content="{step.description}">{index}</a>
                    {/if}
                {:else}
                    {#if step.id==get(email)}
                    <a tabindex="0" id="popover{index}" style="border-radius: 50%;" class="btn btn-lg btn-danger" role="button" data-bs-toggle="popover" data-bs-placement="bottom" data-bs-trigger="focus" title="Assignee: {step.id}" on:click={() => showPopover(index)} data-bs-content="{step.description}">{index}</a>
                    {:else}
                    <a tabindex="0" id="popover{index}" style="border-radius: 50%;" class="btn btn-lg btn-outline-danger" role="button" data-bs-toggle="popover" data-bs-placement="bottom" data-bs-trigger="focus" title="Assignee: {step.id}" on:click={() => showPopover(index)} data-bs-content="{step.description}">{index}</a>
                    {/if}
                    {/if}
            </div>
            {#if index<(apiResponse["steps"].length-1)}
            <div class="mr-3 ml-3" style="display: inline-block"><h1><i class="bi bi-arrow-right"></i></h1></div>
            {/if}
                
            {/each}
            </div>
        </div>
        <div style="text-align:center">
            <div class="btn-group mt-3 ml-5" role="group" >
                <div class="upload-btn-wrapper">
                    <button class="btn btn-outline-primary">Choose a file</button>
                    <input id="fileupload" class="form-control" type="file" name="fileupload"/>
                </div>
                <button type="button" class="btn btn-outline-primary" on:click={async() => await incrementWorkflow()}>Advance</button>
            </div>
        </div>
            <br><br><br>
            <div class="shadow-lg p-3 mb-5 bg-body rounded">
            <div class="container-fluid overflow-auto" style="height: 55vh">
                {#each apiResponse["files"] as file, index}
                <div class="card mr-3 mb-3" style="width: justify-content; display:inline-block">
                    <img src="https://icons.getbootstrap.com/assets/icons/file-earmark-text-fill.svg" class="card-img-top">
                    <div class="card-body">
                        {file["name"]}
                        <p></p>
                        <div on:click={async () => {await downloadFile(file)}} class="btn btn-primary"><i class="bi bi-download"></i></div>
                    </div>
                </div>
                {/each}
                </div>
            </div>
    {:else if state == "write"}
        
            <div style = "display:block;">
                <div class = "name-box" style="text-align:center">
                    <div class = "field" style="width:fit-content;height:fit-content;text-align:center">Workflow name</div><p></p><input type="text" id="wname" name="assignee" placeholder="name">
                </div>
            {#each createWorkflowFields as field , index}
            
                <div class = "create-box">
                    <div class = "field" style="text-align:center">Step {index+1}</div><p></p>
                    <div class = "field" style="background-color:rgb(231, 231, 231);">Assignee: </div><input type="text" id="a{index}" name="assignee" placeholder="email@nsn.pt">

                    <p></p>
                    <div class = "field" style="background-color:rgb(231, 231, 231);">Description </div><p></p>
                    <div class = "field"  style = "background-color:inherit"><textarea id="d{index}" style="width:100%" placeholder="Description"></textarea></div>

                </div>
            {/each}


            <div class = "button-box" style="text-align:center; margin-top:15px;border-radius:0px">
                <button id="bnstep" class = "btn btn-lg btn-primary mb-3" style = "width:fit-content;margin-top:30px" on:click={() => {
                    createWorkflowFields.push({"assignee" : "" , "description" : ""});
                    createWorkflowFields = createWorkflowFields;

                }} >new step</button>

                <button id="bsubmit" class = "btn btn-lg btn-primary mb-3" style="width:fit-content;margin-top:30px"on:click={() => {

                    createWorkflow();

                }}>Submit</button>
            </div>
        </div>


    {/if}

    </main>


<style>

    .upload-btn-wrapper input[type=file] {
        font-size: 100px;
        position: absolute;
        left: 0;
        top: 0;
        opacity: 0;
    }

    .upload-btn-wrapper {
        position: relative;
        overflow: hidden;
        display: inline-block;
    }

    .field
    {
        
        background-color: white;
        width:fit-content + 20px;
        display:inline-block;
        height:fit-content + 10px;
        padding-left:30px;
        padding-right:30px;
        margin-top:30px;
        min-height:30px;
        font-size:24px;
    }

    .box
    {
        white-space:nowrap;
        text-align:center;
        height: fit-content;
    }

    .step
    {
        display:inline-block;
        width:200px;
        height:50px;
        margin-left:50px;
        margin-right:50px;
        background-color:grey;
    }

    .description
    {
        width:200px;
        height:100px;
    }

    .circle
	{
		height: 25px;
		width: 25px;
		background-color: rgb(123, 89, 89);
		border-radius: 50%;

	}

    .arrow {
    width: 50px;
    height: 25px;
    background: url("http:unsplash.it/400x300");
    }

    .name-box
    {
        box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset;
        background-color:rgb(231, 231, 231);
        width:40%;
        margin: 0 auto;
        padding-bottom:50px;
        margin-top:100px;
        height: fit-content;
        border-radius:20px;
    }

    .create-box
    {
        box-shadow: rgb(38, 57, 77) 0px 20px 30px -10px;
        width : 40%;
        margin: 0 auto;
        height: fit-content;
        padding-bottom:50px;
        margin-top:100px;
        background-color:rgb(231, 231, 231);
        min-height:300px;
        text-align:center;
        min-width: fit-content;
    }

    .button-box
    {
        box-shadow: rgb(91, 109, 128) 0px 20px 30px -10px;
        background-color:rgb(231, 231, 231);
        width:40%;
        margin: 0 auto;
        padding-bottom:50px;
        margin-top:100px;
        height: fit-content;
        border-radius:20px;

    }

</style>