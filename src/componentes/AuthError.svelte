<script>
    import { signOut } from '../App.svelte'
</script>

<main>
    <div class="modal fade" id="authError" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">You are not logged in.</h5>
                </div>
                <div class="modal-body">
                You will be redirected in order to perform authentication.
                </div>
                <div class="modal-footer">
                <button type="button" class="btn btn-primary" on:click={() => signOut()}>OK</button>
                </div>
            </div>
        </div>
    </div>
</main>