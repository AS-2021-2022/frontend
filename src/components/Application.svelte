<script>
	import Chat from './Chat.svelte';
	import userid from './Chat.svelte';
    import Navbar from './Navbar.svelte';
    import AuthError from './AuthError.svelte';

    import { page } from '../stores/state'
    import { authenticated, jwt } from '../stores/auth'
import Sidebar from './Sidebar.svelte';

    let statePage
	page.subscribe(p => {statePage = p})

	var sidebar_title = "";
	let options = [];
	let selected_user = 0;
	function updateSideBar(type)
	{
		getOptions(type);
		switch(type)
		{
			case 'chat':
			sidebar_title = "chat";
			selected_user = 0;
			break;
			case 'tasks':
			sidebar_title = "tasks";
			break;
			case 'workflows':
			sidebar_title = "workflows";
			break;
			case 'files':
			sidebar_title = "files";
			break;
		}
	}
	function selected(index)
	{
		
		switch(statePage)
		{
			case 'chat':
			
			selected_user = options[index]["id"];
			
			break;
		}
	}
	function decodeColor()
	{
		for(let i=0;i<options.length;i++)
		{
			switch(statePage)
			{
				case 'chat':
				if(options[i]["status"] == "offline")
				{
					options[i]["color"] = "grey";
					delete options[i].status;
				}
				if(options[i]["status"] == "online")
				{
					options[i]["color"] = "green";
					delete options[i].status;
				}
				if(options[i]["status"] == "busy")
				{
					options[i]["color"] = "red";
					delete options[i].status;
				}
				break;
			}
		}
		console.log(options);
		options = options;
	}
	function getOptions(type) //send http request in order to get list of options (tasks, workflows , etc...)
	{
		
		options = [];
		switch(type)
		{
			case 'chat':
			options = [{"name": 'Jonh Doe' , "status": 'offline' , 'id' : 0xff} , {"name": 'Jane Doe',  "status":'online' , "id" : 0xf1} , {"name" : 'User3' , 'status' : "busy" , "id" : 0xf3}];
			decodeColor();
			break;
			case 'tasks':
			options = [{name: 'Tarefa 1' , color: 'red'} , {name: 'Tarefa 2',  color:'green'}];
			break;
			case 'workflows':
			options = [{name: 'Workflow 1' , color: 'red'} , {name: 'Workflow 2',  color:'green'}];
			break;
		}
	}
	
	function authError() {
		const authError = new bootstrap.Modal('#authError', {"backdrop": false, "keyboard": false})
		authError.show()
	}
</script>

<Navbar></Navbar>
<div class="container-fluid">
    <div class="row">
        <Sidebar></Sidebar>
        <div class="col-9">
            {#if (statePage=='chat')}
            Chat
            {/if}
            {#if (statePage=='workflows')}
            Workflows
            {/if}
        </div>
    </div>
</div>
<AuthError></AuthError>