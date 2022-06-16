<script>

    import {callAPI} from "./global.js";
    import { afterUpdate } from "svelte";
    import { get } from "svelte/store";
    import {token} from "./stores/store.js";

    let postVar;
    let fileVar;
    let init_flag = false;
    let files = [];
    


    async function uploadFile() {
    let formData = new FormData();
    formData.append("file", fileupload.files[0]);
    await fetch('https://tranquil-brook-75958.herokuapp.com/upload', {
        method: "POST", 
        body: formData
    }); 
    }

    afterUpdate(async() => {

        //get files list
        if(init_flag == false)
        {
            let awnser = await callAPI("getFilesList" , {"token" : get(token)});
            if(awnser["status"] == "accepted")
            {
                files = awnser["files"];
                console.log(files);
            }
            init_flag = true;
        }
    });


  function downloadFile(file) {
     var req = new XMLHttpRequest();
     req.open("GET", "https://tranquil-brook-75958.herokuapp.com/download?" + "token=" + get(token) + "&id=" + file["id"], true);
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

    async function removeFile(file)
    {
        let awnser = await callAPI("removeFile" , {"token" : get(token) , "id" : file["id"]});
        if(awnser["status"] == "accepted")
        {
            files = files.filter((val) => {return val["id"] != file["id"]});
        }
    }
    
  </script>
  
  <div>
    




    <div class="shadow-lg p-3 mb-5 mt-5 bg-body rounded">
        <div class="container-fluid overflow-auto" style="height: 55vh">
        {#each files as file, index}
            <div class="card mr-3 mb-3" style="width: justify-content; display:inline-block;">
                <img src="https://icons.getbootstrap.com/assets/icons/file-earmark-text-fill.svg" class="card-img-top">
                <div class="card-body">
                    {file["name"]}
                    <p></p>
                    <div on:click={() => {downloadFile(file)}} class="btn btn-primary"><i class="bi bi-download"></i></div>
                    <div on:click={() => {removeFile(file)}} class="btn btn-danger"><i class="bi bi-trash"></i></div>
                </div>
            </div>    
        {/each}
        </div>
    </div>

    <!--Upload Form-->
    <div class = "uploadBox">
        <input id="fileupload" type="file" name="fileupload" /> 
        <button class = "btn btn-lg btn-primary mb-3"id="upload-button" on:click={()=>{uploadFile()}}> Upload </button>
    </div>
</div>

<style>

    .uploadBox
    {
        
        
    }


</style>