<script>
    import { afterUpdate } from "svelte";

    export let workflowid;
    var last_id = -1;

    const popovers = []

    function showPopover(index) {
        try {
            popovers[index].show()
        }
        catch {
            const exampleEl = document.getElementById('popover'+index)
            const popover = new bootstrap.Popover(exampleEl)
            popovers[index] = popover
            popover.show()
        }
    }

    
    afterUpdate(() => {
    
    if(last_id != workflowid)
    {
        last_id = workflowid;
    }

    });

    function getWorkflow()
    {
        return {"status" : "accepted" , "name" : "workflow name" , "progress" : 1 ,
        "steps" : [{"assignee_id" : "id" , "description" : "description text"} , {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, ],
        "files" : ["file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt"]};
    }

    let apiResponse = getWorkflow();


</script>


<main>
    Workflow {workflowid}
    
    <div class = "box">

        {#each apiResponse["steps"] as step , index}
            <div style="display: inline-block">
                {#if index < apiResponse["progress"]}
                
                <a tabindex="0" id="popover{index}" class="btn btn-lg btn-success" role="button" data-bs-toggle="popover" data-bs-placement="bottom" data-bs-trigger="focus" title="Iteração {index}" on:click={() => showPopover(index)} data-bs-content="{step.description}">{index}</a>
                {:else}
                
                
                <a tabindex="0" id="popover{index}" class="btn btn-lg btn-danger" role="button" data-bs-toggle="popover" data-bs-placement="bottom" data-bs-trigger="focus" title="Iteração {index}" on:click={() => showPopover(index)} data-bs-content="{step.description}">{index}</a>{/if}
            </div>
            <div style="display: inline-block">>>>>></div>

            
        {/each}
        </div>
        <br><br><br><br><br><br><br>
        <div class="container-fluid overflow-auto-y">
            {#each apiResponse["files"] as file, index}
            <div class="card" style="width: 10rem; display:inline-block">
                <img src="https://icons.getbootstrap.com/assets/icons/file-earmark-text-fill.svg" class="card-img-top">
                <div class="card-body">
                    <h5 class="card-title">{file}</h5>
                    <a href="#" class="btn btn-primary">Download</a>
                </div>
            </div>
            {/each}
            </div>

</main>


<style>

    .box
    {
        width: 95%;
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

</style>