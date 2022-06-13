<script>
    import { afterUpdate } from "svelte";
    import {token, email} from "./stores/store.js";
    import { get } from "svelte/store";
    import {callAPI , postAPI} from "./global.js";
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

    

    
    afterUpdate(() => {
    
    if(last_id != workflowid)
    {
        last_id = workflowid;
        if(workflowid == undefined) state = "write";
        else{
            state = "read";
            getWorkflow();
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
            createWorkflowFields = [];
            getWorkflow();
        }
        else{
            console.log("Rejected");
        }
    }

    async function getWorkflow()
    {
        var dict = {"token" : get(token), "id": workflowid};

        let answer = await callAPI("getWorkflow" , dict);

        console.log(answer)

        if (answer["status"] == "accepted") {
            apiResponse = answer;
        }
    }

    async function incrementWorkflow()
    {
        cstep++
        if (document.getElementById("popover" + (cstep)).classList.contains("btn-outline-danger")) {
            document.getElementById("popover" + cstep).classList.remove("btn-outline-danger");
            document.getElementById("popover" + cstep).classList.add("btn-outline-success");
        }
        if (document.getElementById("popover" + (cstep)).classList.contains("btn-danger")) {
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

        var dict = {"token" : get(token), "params": {"id": workflowid, "fileName": files[0].name}};
        console.log(files[0].name)
        console.log(dict)
        let answer = await callAPI("incrementWorkflow" , dict);
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
        <div class="mt-3">
            <input class="form-control form-control-sm" id="formFileSm" type="file" bind:files>
            <button type="button" class="btn btn-outline-primary mt-3" on:click={() => incrementWorkflow()}>Advance Workflow</button>
        </div>
            <br><br><br>
            <div class="shadow-lg p-3 mb-5 bg-body rounded">
            <div class="container-fluid overflow-auto" style="height: 55vh">
                {#each apiResponse["files"] as file, index}
                <div class="card mr-3 mb-3" style="width: justify-content; display:inline-block">
                    <img src="https://icons.getbootstrap.com/assets/icons/file-earmark-text-fill.svg" class="card-img-top">
                    <div class="card-body">
                        {file}
                        <p></p>
                        <a href="#" class="btn btn-primary"><i class="bi bi-download"></i></a>
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


            <div class = "button-box" style="text-align:center; margin-top:5px;border-radius:0px">
                <button class = "btn btn-lg btn-primary mb-3" style = "width:fit-content" on:click={() => {
                    createWorkflowFields.push({"assignee" : "" , "description" : ""});
                    createWorkflowFields = createWorkflowFields;

                }} >new step</button>

                <button  class = "btn btn-lg btn-primary mb-3" style="width:fit-content"on:click={() => {

                    createWorkflow();

                }}>Submit</button>
            </div>
        </div>


    {/if}

    </main>


<style>

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
        box-shadow: rgb(38, 57, 77) 0px 20px 30px -10px;
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