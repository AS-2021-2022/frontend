<script>
    let postVar;
    let fileVar;
    let files = ["jeff", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", "jeff", ]
  
    
    
  </script>
  
  <div>
    <form enctype="multipart/form-data" action='https://tranquil-brook-75958.herokuapp.com/upload' method="POST">
        <input type="hidden"/>
        Choose a file to upload: <input name="file" type="file" /><br />
        <input type="submit" />
        </form>
    <div class="shadow-lg p-3 mb-5 mt-5 bg-body rounded">
        <div class="container-fluid overflow-auto" style="height: 55vh">
        {#each files as file, index}
            <div class="card mr-3 mb-3" style="width: justify-content; display:inline-block;">
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
</div>