<script>
	import Chat from "./Chat.svelte";
	import userid from "./Chat.svelte";
	import taskid from "./Tasks.svelte";
	import workflowid from "./Workflow.svelte";
	import Home from "./Home.svelte"
	import Tasks from "./Tasks.svelte";
	import Login from "./Login.svelte";
	import Workflow from "./Workflow.svelte";
	import Files from "./Files.svelte";
	import {logged , role , token , email} from "./stores/store.js";
	import { get } from "svelte/store";
	import {callAPI} from "./global.js";


	

	let _logged;
	let show_sidebar = false;

	logged.subscribe(value => {
		_logged = value;
	});



	
	let options = [];

	let optionLatestID = -1;

	let selected_user	  = -1;
	let selected_task 	  = -1;
	let selected_workflow = -1;



	let nav_active = "home";
	function updateSideBar(type)
	{
		document.getElementById(nav_active).classList.remove("active");
		document.getElementById(type).classList.add("active");
		nav_active = type;

		getOptions(type);
		switch(type)
		{
			case 'chat':
			show_sidebar = true;
			selected_user = -1;
			break;

			case 'tasks':
			show_sidebar = true;
			selected_task = -1;
			break;

			case 'workflows':
			show_sidebar = true;
			selected_workflow = -1;
			break;

			case 'files':
			show_sidebar = false;
			break;

			case 'home':
				show_sidebar = false;
			break;
		}
		if(optionLatestID != -1)
			document.getElementById(optionLatestID.toString()).style.backgroundColor = "inherit";
		optionLatestID = -1;
	}

	function selected(index)
	{
		if(optionLatestID != -1) document.getElementById(optionLatestID.toString()).style.backgroundColor = "inherit";
		document.getElementById(index.toString()).style.backgroundColor = "grey";
		optionLatestID = index;
		if(index != 1000)
		{
			switch(nav_active)
			{
				case 'chat':
				selected_user = options[index]["id"];
				break;
				case 'tasks':
				selected_task = options[index]["id"];
				break;
				case 'workflows':
				selected_workflow = options[index]["id"];
			}
		}
	}

	async function getOptions(type) //send http request in order to get list of options (tasks, workflows , etc...)
	{	
		options = [];
		switch(type)
		{
			case 'chat':
			options = await callAPI("contacts" , {"token" : get(token)});
			options = decodeOptions('chat', options);
			break;

			case 'tasks':
			//options = await callAPI("getTasksList" , {"token" : get(token)});
			options = [{name: 'Tarefa 1' , color: 'red' , 'id' : 1} , {name: 'Tarefa 2',  color:'green' , 'id' : 2}];
			break;

			case 'workflows':
			options = await callAPI("getWorkflows" , {"token" : get(token)})
			options = decodeOptions('workflows', options)
			break;
		}
	}

	function decodeOptions(type , response)
	{
		let newOptions = [];
		if(type == 'chat')
		{
			for(let i=0;i<response["users"].length;i++)
			{
				let userColor = undefined;
				let userStatus = response["users"][i]["status"];
				if(userStatus == "ONLINE") userColor = "green";
				if(userStatus == "OFFLINE") userColor = "grey";
				newOptions.push({
					name: response["users"][i]["name"],
					id:	response["users"][i]["id"],
					"color": userColor
				});
			}
			for(let i=0;i<response["groups"].length;i++)
			{
				let group = response["groups"][i];
				newOptions.push({
					name: group["name"] ,
					id:   group["id"] ,
					"color": "white"
				});
			}
		}

		if(type == 'workflows')
		{
			for(let i=0;i<response["workflows"].length;i++)
			{
				let workflowColor = undefined;
				let pending = response["workflows"][i]["pending"];
				if(pending === false) workflowColor = "gray";
				if(pending === true) workflowColor = "green";
				newOptions.push({
					name: response["workflows"][i]["name"],
					id:	response["workflows"][i]["id"],
					"color": workflowColor
				});
			}
		}

		if(type == 'tasks')
		{
			for(let i=0;i<response["tasks"].length;i++)
			{
				let taskColor = "green";
				let task = response["tasks"][i];
				if(task["time_left"] < 120) "red";
				newOptions.push({
					name : task["name"],
					id   : task["id"] ,
					color: taskColor
				});
			}
		}
		return newOptions;
	}
	
	
</script>



<svelte:head>
	<title>NSN</title>
	<link rel='icon' type='image/png' href='https://icons.getbootstrap.com/assets/icons/person-workspace.svg'>
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.3.0/font/bootstrap-icons.css">

</svelte:head>

<main>
	{#if _logged === false}
	<Login></Login>
	{:else}
		<nav class="navbar navbar-expand-md navbar-dark bg-primary active">
			<a href="#" id="home" class="navbar-brand" on:click={() => updateSideBar('home')}><i class="bi bi-house"></i></a>
			<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbar6">
				<span class="navbar-toggler-icon"></span>
			</button>
			<div class="navbar-collapse collapse justify-content-stretch" id="navbar6">
				<ul class="navbar-nav">
					<li on:click={() => updateSideBar('chat')} class="nav-item" id="chat">
						<a class="nav-link" href="#">Chat<i class="bi bi-arrow-right"></i></a>
					</li>
					<li on:click={() => updateSideBar('tasks')} class="nav-item" id="tasks">
						<a class="nav-link " href="#" >Tasks<i class="bi bi-arrow-right"></i></a>
					</li>
					<li on:click={() => updateSideBar('workflows')} class="nav-item" id="workflows">
						<a class="nav-link " href="#">Workflows<i class="bi bi-arrow-right"></i></a>
					</li>
					<li on:click={() => updateSideBar('files')} class="nav-item" id="files">
						<a class="nav-link " href="#">Files<i class="bi bi-arrow-right"></i></a>
					</li>
				</ul>
				<ul class="navbar-nav ml-auto">
					<li class="nav-item">
						<a class="nav-link " href="#"> <i class="bi bi-envelope"></i>{get(email)}</a>
					</li>
					<li class="nav-item">
						<a class="nav-link" style="cursor:pointer" on:click={() => {logged.set(false);}}>Sign out <i class="bi bi-door-closed"></i></a>
					</li>
				</ul>
			</div>
		</nav>

		

		<div>
			{#if show_sidebar == true}
				<div style="width:280px;Text-align:left;float:left;background-color:gainsboro;">
					<div class="d-flex flex-column flex-shrink-0 p-3" style="width: 280px;height:92.5vh;">
						{#if nav_active == "tasks"}
							<div id = "1000" class = "sidebar-content" on:click={() => {selected(1000);selected_task = undefined}}>Create Task + </div>
						{/if}
						{#if get(role) == "MANAGER" && nav_active == "workflows"}
						<div id = "1000" class = "sidebar-content" on:click={() => {selected(1000);selected_workflow = undefined}}>Create Workflow + </div>
						{/if}
						{#each options as option , index}
						
						<div on:click={() => {selected(index)}}>
							<div id="{index}"class="sidebar-content">{option.name} <div class="circle" style="background-color:{option.color};"></div></div>
						</div>
						{/each}
						
					</div>
				</div>
			{/if}
			
			<div class="overflow-auto" style="width:calc(100% - {show_sidebar * 280}px);float:right;height:90vh;">
				{#if nav_active == "chat" && selected_user != -1}
						<Chat userid = {selected_user}></Chat>
				
				{:else if nav_active == "home"}

					<Home></Home>
				

				{:else if nav_active == "tasks" && selected_task != -1}

						<Tasks taskid = {selected_task}></Tasks>

				

				{:else if nav_active == "workflows" && selected_workflow != -1}
						<Workflow workflowid = {selected_workflow}></Workflow>

				{:else if nav_active == "files"}
						<Files></Files>

				{/if}

			</div>
		</div>

	
	{/if}

	<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.5/dist/umd/popper.min.js" integrity="sha384-Xe+8cL9oJa6tN/veChSP7q+mnSPaj5Bcu9mPX5F5xIGE0DVittaqT5lorf0EI7Vk" crossorigin="anonymous"></script>
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.min.js" integrity="sha384-kjU+l4N0Yf4ZOJErLsIcvOU2qSb74wXpOhqTvwVx3OElZRweTnQ6d31fXEoRD1Jy" crossorigin="anonymous"></script>
</main>

<style>
	
	main {
		
		padding: 0em;
		max-width: 240px;
		margin: 0 auto;
	}

	.active
	{
		background: black;
	}
	
	
	.navbar-nav > li{
  		padding-left:30px;
  		padding-right:30px;
	}

	.sidebar-content{
  		padding-top: 20px;
		padding-bottom: 20px;
		text-align:left;

	}
	.sidebar-content:hover{
		background-color: rgb(187, 187, 187);
		cursor:pointer;
	}

	.circle
	{
		height: 25px;
		width: 25px;
		background-color: #bbb;
		border-radius: 50%;
		display: inline-block;
		float:right;
		margin-right:10px;
		
	}

	.content
	{
		width:10%;
		
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>