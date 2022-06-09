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
        "steps" : [{"assignee_id" : "id" , "description" : "description text"} , {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, {"assignee_id" : "id2" , "description" : "DESC2"}, ],
        "files" : ["file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt", "file.txt"]};
    }

    let apiResponse = getWorkflow();


</script>


<main>
    Workflow {workflowid}
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
</main>


<style>

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

</style>