<script>

	import {token , logged , role , email} from './stores/store.js';
	import {callAPI} from "./global.js";
	import { get} from 'svelte/store';

	



async function login () {

	document.getElementById("loading").style.display = "block"

    let user = document.getElementById("user").value;
    let pass = document.getElementById("pass").value;

	let result = await callAPI("login" , {"username" : user , "password" : pass});

    if(result["status"] == "accepted")
    {
	  token.set(result["token"]);
	  
	  //get user type
	  let type = await callAPI("getUserType" , {"token" : get(token)});

	  if(type["status"] == "accepted")
	  {
		role.set(type["type"]);   
		logged.set(true);
		email.set(result["email"]);
	  }
    }

	if(result["status"] == "rejected")
	{
		console.log("unable to login");
		document.getElementById('failed').classList.add('show')
	}

	document.getElementById("loading").style.display = "none"
}

</script>


<main>
    
	
    <div class="wrapper">
		
        <div class="form-signin"> 
			<div class = "title" style="border-bottom:3px solid white">NSN - Seguros</div>
			  
          <h2 class="form-signin-heading" style="text-align:center">Please login</h2>
          <input type="text" class="form-control" id="user" placeholder="Email Address" required="" autofocus="" />
          <input type="password" class="form-control" id="pass" placeholder="Password" required=""/>      

			<button class="btn btn-lg btn-primary btn-block mb-3" on:click={()=>{login();}}>
				<div class="d-flex align-items-center">
					Login
					<div id="loading" class="spinner-border ml-auto" role="status" style="display:none">
						<span class="visually-hidden"></span>
					</div>
				</div>
			</button>
		  <div id="failed" class="alert alert-danger fade" role="alert">
			Could not authenticate. Please try again.
		</div>
		</div>
		
      </div>

	
</main>



<style>
   
   .title
   {
    font-size:33px;
    text-align:center;
    margin-top:50px;
	
   }
 .wrapper {
	 margin-top: 80px;
	 margin-bottom: 80px;
}
 .form-signin {
	box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset;
	 border-radius:10px;
	 max-width: 380px;
	 padding: 15px 35px 45px;
	 margin: 0 auto;
	 background-color: rgb(244, 244, 244);
	 border: 1px solid rgba(0, 0, 0, 0.1);
	 
}
 .form-signin .form-signin-heading, .form-signin .checkbox {
	 margin-bottom: 30px;
}
 .form-signin .checkbox {
	 font-weight: normal;
}
 .form-signin .form-control {
	 position: relative;
	 font-size: 16px;
	 height: auto;
	 padding: 10px;
}
 .form-signin .form-control:focus {
	 z-index: 2;
}
 .form-signin input[type="text"] {
	 margin-bottom: -1px;
	 border-bottom-left-radius: 0;
	 border-bottom-right-radius: 0;
}
 .form-signin input[type="password"] {
	 margin-bottom: 20px;
	 border-top-left-radius: 0;
	 border-top-right-radius: 0;
}
 


</style>