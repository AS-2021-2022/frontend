<script>
	import { authenticated, jwt } from '../stores/auth'

	let email = '', password = '';

	async function login() {
		const res = await fetch('./login', {
			method: 'POST',
			body: JSON.stringify({
				'type': 'login',
				'params': {
				'email': email,
				'password': password
				}
			})
		})
		try {
			res = await res.json()
			if (res.status == 'accepted') {
				authenticated.set(true)
				token.set(res.token)
			}
			else {failed()}
		}
		catch {
			failed()
		}
    }

	async function failed() {
		document.getElementById('failed').classList.add('show')
	}
</script>

<div class="position-absolute top-50 start-50 translate-middle">
	<form on:submit|preventDefault={login}>
		<div class="mb-3">
			<input bind:value={email} type="email" class="form-control" id="email" placeholder="Email" required>
		</div>
		<div class="mb-3">
			<input bind:value={password} type="password" class="form-control" id="password" placeholder="Password" required>
		</div>
		<button type="submit" class="btn btn-primary d-grid col-12 mx-auto mb-3">Log In</button>
	</form>
	<div id="failed" class="alert alert-danger fade" role="alert">
		Could not authenticate. Please try again.
	</div>
</div>