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


  async function downloadFile(file) {
     var req = new XMLHttpRequest();
     req.open("GET", "https://tranquil-brook-75958.herokuapp.com/download?" + "token=" + get(token) + "&fileID=" + file["id"], true);
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
                    <div on:click={async () => {await downloadFile(file)}} class="btn btn-primary"><i class="bi bi-download"></i></div>
                    <div on:click={async () => {await removeFile(file)}} class="btn btn-danger"><i class="bi bi-trash"></i></div>
                </div>
            </div>    
        {/each}
        </div>
    </div>

    <!--Upload Form-->
    <div class = "uploadBox">
        <input id="fileupload" type="file" name="fileupload" /> 
        <button class = "btn btn-lg btn-primary mb-3"id="upload-button" on:click={async ()=>{await uploadFile()}}> Upload </button>
    </div>
</div>

<style>

    .uploadBox
    {
        
        
    }


</style>