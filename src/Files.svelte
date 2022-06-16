<script>

    import jQuery from "jquery";

    let postVar;
    let fileVar;
    let files = ["Main.java", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", ]
    

    async function uploadFile() {
  let formData = new FormData(); 
  formData.append("file", fileupload.files[0]);
  await fetch('https://tranquil-brook-75958.herokuapp.com/upload', {
    method: "POST", 
    body: formData
  }); 
  }


  function downloadFile(name) {
     var req = new XMLHttpRequest();
     req.open("GET", "https://tranquil-brook-75958.herokuapp.com/download?filename=" + name, true);
     req.responseType = "blob";
     req.onload = function (event) {
         var blob = req.response;
         var fileName = req.getResponseHeader("name") //if you have the fileName header available
         var link=document.createElement('a');
         link.href=window.URL.createObjectURL(blob);
         link.download=name;
         link.click();
     };

     req.send();
 }


    
  </script>
  
  <div>
    




    <div class="shadow-lg p-3 mb-5 mt-5 bg-body rounded">
        <div class="container-fluid overflow-auto" style="height: 55vh">
        {#each files as file, index}
            <div class="card mr-3 mb-3" style="width: justify-content; display:inline-block;">
                <img src="https://icons.getbootstrap.com/assets/icons/file-earmark-text-fill.svg" class="card-img-top">
                <div class="card-body">
                    {file}
                    <p></p>
                    <div on:click={() => {downloadFile(file)}} class="btn btn-primary"><i class="bi bi-download"></i></div>
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