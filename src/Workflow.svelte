<script>
    import { afterUpdate } from "svelte";
    import {token} from "./stores/store.js";
    import { get } from "svelte/store";
    import {callAPI} from "./global.js";
    export let workflowid;

    var last_id = -1;
    let state = "";
    const popovers = [];
    let createWorkflowFields = [{"assignee" : "" , "description" : ""} , {}];
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

    async function getWorkflow()
    {
        var dict = {"token" : get(token), "params": {"id": workflowid}};

        let answer = await callAPI("getWorkflow" , dict);

        console.log(answer)

        if (answer["status"] == "accepted") {
            apiResponse = answer;
        }
    }

    getWorkflow();


</script>


<main>
    {#if state == "read" && apiResponse != undefined}
        <div class="container-fluid" style="height: 11.5vh;  overflow-x: auto; overflow-y: hidden">

        <div class = "box">

            {#each apiResponse["steps"] as step , index}
            <div style="display: inline-block">
                {#if index < apiResponse["progress"]}
                
                <a tabindex="0" id="popover{index}" style="border-radius: 50%;" class="btn btn-lg btn-success" role="button" data-bs-toggle="popover" data-bs-placement="bottom" data-bs-trigger="focus" title="Assignee: {step.assignee}" on:click={() => showPopover(index)} data-bs-content="{step.description}">{index}</a>
                {:else}
                
                
                <a tabindex="0" id="popover{index}" style="border-radius: 50%;" class="btn btn-lg btn-danger" role="button" data-bs-toggle="popover" data-bs-placement="bottom" data-bs-trigger="focus" title="Assignee: {step.assignee}" on:click={() => showPopover(index)} data-bs-content="{step.description}">{index}</a>{/if}
            </div>
            {#if index<(apiResponse["steps"].length-1)}
            <div style="display: inline-block"><h1><i class="bi bi-arrow-right"></i></h1></div>
            {/if}
                
            {/each}
            </div>
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
            <div style = "text-align:center;">
            {#each createWorkflowFields as field}
                <div class="create-box">
                        <div>t1</div>
                        <p></p>
                        <div>t2</div>
                        
                    </div>
            {/each}
            </div>

    {/if}
</main>


<style>


    .assignee
    {
        display: block;
        text-align:left;
        float:left;
        margin-left:30px;
        width:200px;
        background-color: white;
    }

    .text
    {
        display: block;
        text-align:left;
        float:left;
        margin-left:30px;
        width:200px;
        background-color: white;
        min-height: 200px;
    }

    .box
    {
        white-space:nowrap;
        text-align:center;
        height: fit-content;
        background-color: aliceblue;
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
        background-color: red;
        display:block;
        width:500px;
        left:50%;
    }

</style>