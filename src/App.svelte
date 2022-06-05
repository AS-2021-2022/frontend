<script context='module'>
	import { authenticated, jwt } from './stores/auth'
    
    export function signOut() {
		jwt.set('')
		authenticated.set(false)
		page.set('home')
	}
</script>

<script>
	import Application from './componentes/Application.svelte';
	import Login from './componentes/Login.svelte'

	let auth;
	authenticated.subscribe(a => {auth = a})

	let token;
	jwt.subscribe(t => {token = t})
</script>

<svelte:head>
	<title>NSN</title>
	<link rel='icon' type='image/png' href='https://play-lh.googleusercontent.com/8ddL1kuoNUB5vUvgDVjYY3_6HwQcrg1K2fd_R8soD-e2QYj8fT9cfhfh3G0hnSruLKec'>
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2" crossorigin="anonymous"></script>
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.3/font/bootstrap-icons.css">
</svelte:head>

<main>
	{#if !auth}
	<Login></Login>
	{/if}
	{#if auth}
	<Application></Application>
	{/if}
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2" crossorigin="anonymous"></script>
</main>