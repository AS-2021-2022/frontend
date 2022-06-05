<script>
    import { sidebarItems } from '../stores/content'

    let contentSidebarItems = []
	sidebarItems.subscribe(i => {contentSidebarItems = i})
</script>

<div class="col-2 overflow-auto" style="height:92.5vh">
    <ul class="nav flex-column">
        {#each contentSidebarItems as sidebarItem}
        <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#"><i class="bi bi-circle-fill"></i> {sidebarItem}</a>
        </li>
        {/each}
    </ul>
</div>