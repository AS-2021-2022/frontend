<script>
	import { page, email } from '../stores/state'
	import { signOut } from '../App.svelte'

	let statePage
	page.subscribe(p => {statePage = p})

	let stateEmail
	email.subscribe(p => {stateEmail = p})

    function changePage(id) {
		document.getElementById(statePage + 'Nav').classList.remove('active')
		document.getElementById(id + 'Nav').classList.add('active')
		page.set(id)
	}

</script>

<nav class="navbar sticky-top navbar-expand-lg navbar-dark bg-primary">
	<div class="container-fluid">
		<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
			<span class="navbar-toggler-icon"></span>
		</button>
		<div class="collapse navbar-collapse" id="navbarSupportedContent">
			<ul class="navbar-nav">
				<li class="nav-item">
					<a id="homeNav" class="nav-link active" role="button" on:click={() => changePage('home')}><i class="bi bi-house-fill"></i></a>
				</li>
				<li class="nav-item">
					<a id="chatNav" class="nav-link" role="button" on:click={() => changePage('chat')}>Chat <i class="bi bi-arrow-right"></i></a>
				</li>
				<li class="nav-item">
					<a id="workflowsNav" class="nav-link" role="button" on:click={() => changePage('workflows')}>Workflows <i class="bi bi-arrow-right"></i></a>
				</li>
				<li class="nav-item">
					<a id="filesNav" class="nav-link" role="button" on:click={() => changePage('files')}>Files <i class="bi bi-arrow-right"></i></a>
				</li>
			</ul>
		</div>
		<ul class="navbar-nav ms-auto"><a id="emailNav" class="nav-link" role="button" >{stateEmail}</a></ul>
		<ul class="navbar-nav ms-auto">
			<li class="nav-item">
				<button id="signoutNav" type="button" class="btn btn-danger" on:click={() => signOut()}>Sign Out</button>
			</li>
		</ul>
	</div>
</nav>