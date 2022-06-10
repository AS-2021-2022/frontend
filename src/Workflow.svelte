<script>
    import { afterUpdate } from "svelte";
    import {token} from "./stores/store.js";
    import { get } from "svelte/store";
    import {callAPI} from "./global.js";
    export let workflowid;

    var last_id = -1;
    let state = "";
    const popovers = [];
    let createWorkflowFields = [];
    let apiResponse = undefined;

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
        }
    }

    });

    async function createWorkflow()
    {
        let dict = {"steps" : [] , "name" : ""};
        dict["name"] = document.getElementById("wname").value;
        for(let i=0;i<createWorkflowFields.length;i++)
        {
            let dest = document.getElementById("a"+i.toString()).value;
            let desc = document.getElementById("d"+i.toString()).value;

            dict["steps"].push({"id" : dest , "description" : desc});

        }

        let awnser = await callAPI("createWorkflow" , dict);

        if(awnser["status"] == "accepted")
        {
            console.log("worked");
        }
    }

    async function getWorkflow()
    {
        var dict = {"token" : get(token), "params": {"id": workflowid}};

        let answer = await callAPI("getWorkflow" , dict);

        console.log(answer)

        if (answer["status"] == "accepted") {
            apiResponse = answer;
        }
    }

    async function incrementWorkflow()
    {
        var dict = {"token" : get(token), "params": {"id": workflowid}};

        let answer = await callAPI("incrementWorkflow" , dict);

        console.log(answer)
    }

    getWorkflow();


</script>


<main>
    {#if state == "read" && apiResponse != undefined}
        <div class="container-fluid mt-5" style="height: 11.5vh;  overflow-x: auto; overflow-y: hidden">

        <div class = "box">

            {#each apiResponse["steps"] as step , index}
            <div style="display: inline-block">
                {#if index < apiResponse["progress"]}
                
                <a tabindex="0" id="popover{index}" style="border-radius: 50%;" class="btn btn-lg btn-success" role="button" data-bs-toggle="popover" data-bs-placement="bottom" data-bs-trigger="focus" title="Assignee: {step.assignee}" on:click={() => showPopover(index)} data-bs-content="{step.description}">{index}</a>
                {:else}
                
                
                <a tabindex="0" id="popover{index}" style="border-radius: 50%;" class="btn btn-lg btn-danger" role="button" data-bs-toggle="popover" data-bs-placement="bottom" data-bs-trigger="focus" title="Assignee: {step.assignee}" on:click={() => showPopover(index)} data-bs-content="{step.description}">{index}</a>{/if}
            </div>
            {#if index<(apiResponse["steps"].length-1)}
            <div class="mr-3 ml-3" style="display: inline-block"><h1><i class="bi bi-arrow-right"></i></h1></div>
            {/if}
                
            {/each}
            </div>
        </div>
        <div class="mt-3">
            <input class="form-control form-control-sm" id="formFileSm" type="file">
            <button type="button" class="btn btn-outline-primary mt-3" on:click={() => incrementWorkflow()}>Increment</button>
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
                <div class = "field" style="background-color:rgb(231, 231, 231);">Workflow name: </div><input type="text" id="wname" name="assignee" placeholder="name">
            {#each createWorkflowFields as field , index}
            
                <div class = "create-box">

                    <div class = "field" style="background-color:rgb(231, 231, 231);">Assignee: </div><input type="text" id="a{index}" name="assignee" placeholder="email@nsn.pt">

                    <p></p>
                    <div class = "field" style="background-color:rgb(231, 231, 231);">Description: </div>
                    <div class = "field"  style = "background-color:inherit"><textarea id="d{index}" style="width:100%" placeholder="Description"></textarea></div>

                </div>
            {/each}
                <button on:click={() => {
                    createWorkflowFields.push({"assignee" : "" , "description" : ""});
                    createWorkflowFields = createWorkflowFields;

                }}>new step</button>

                <button on:click={() => {

                    createWorkflow();

                }}>Submit</button>
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

    .create-box
    {
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

</style>