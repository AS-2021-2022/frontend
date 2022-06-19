<script>

    import {callAPI , downloadFile} from "./global.js";
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
        formData.append("token" , get(token));
        let awnser = await fetch('https://tranquil-brook-75958.herokuapp.com/upload', {
            method: "POST", 
            body: formData
        }); 
        awnser = await awnser.json();
        if(awnser["status"] == "accepted")
        {
            alert("File uploaded successfully!");
            getFilesList();
        }
    }

    async function getFilesList()
    {
        let awnser = await callAPI("getFilesList" , {"token" : get(token)});
        if(awnser["status"] == "accepted")
        {
            if(awnser["files"] != undefined) files = awnser["files"];
            else{
                files = [];
            }
            console.log(files);
        }
    }

    afterUpdate(async() => {

        //get files list
        if(init_flag == false)
        {
            await getFilesList();
            
            init_flag = true;
        }
    });




    async function removeFile(file)
    {
        let awnser = await callAPI("delete" , {"token" : get(token) , "fileID" : file["id"]});
        if(awnser["status"] == "accepted")
        {
            alert("File sucessfully eliminated!");
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
                    <div on:click={async () => {await downloadFile(file)}} class="btn btn-primary"><i class="bi bi-download"></i></div>
                    <div on:click={async () => {await removeFile(file)}} class="btn btn-danger"><i class="bi bi-trash"></i></div>
                </div>
            </div>    
        {/each}
        </div>
    </div>

    <!--Upload Form-->
    <div>
        <div class="btn-group" role="group">
            <div class="upload-btn-wrapper">
                <button class="btn btn-outline-primary">Choose a file</button>
                <input id="fileupload" class="form-control" type="file" name="fileupload"/>
            </div>
            <button class = "btn btn-outline-primary"id="upload-button" on:click={async ()=>{await uploadFile()}}>Upload</button>
        </div>
    </div>
</div>

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

    .uploadBox
    {
        
        
    }


</style>