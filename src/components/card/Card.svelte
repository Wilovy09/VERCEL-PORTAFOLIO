<script>
    export let title = 'Titulo';
    export let description = 'Descripcion';
    export let img = 'https://unavatar.io/omfg_09';
    export let github = 'https://github.com/Wilovy09';
    export let web = '';
</script>

<div class="max-w-[350px] bg-white text-black rounded-xl">
    <img class="rounded-t-xl h-52 object-cover" src="{img}" alt="{title}">
    
    <div class="flex justify-between">
        <a class="p-2" href="{github}" target="_blank">
            <svg class="GITsvg" width="40" height="40" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round"><path stroke="none" d="M0 0h24v24H0z" fill="none"></path><path d="M9 19c-4.3 1.4 -4.3 -2.5 -6 -3m12 5v-3.5c0 -1 .1 -1.4 -.5 -2c2.8 -.3 5.5 -1.4 5.5 -6a4.6 4.6 0 0 0 -1.3 -3.2a4.2 4.2 0 0 0 -.1 -3.2s-1.1 -.3 -3.5 1.3a12.3 12.3 0 0 0 -6.2 0c-2.4 -1.6 -3.5 -1.3 -3.5 -1.3a4.2 4.2 0 0 0 -.1 3.2a4.6 4.6 0 0 0 -1.3 3.2c0 4.6 2.7 5.7 5.5 6c-.6 .6 -.6 1.2 -.5 2v3.5"></path></svg>
        </a>
        {#if web}
            <a class="p-2" href="{web}" target="_blank">
                <svg width="35" height="35" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round"><path stroke="none" d="M0 0h24v24H0z" fill="none"></path><path d="M9 15l6 -6"></path><path d="M11 6l.463 -.536a5 5 0 0 1 7.071 7.072l-.534 .464"></path><path d="M13 18l-.397 .534a5.068 5.068 0 0 1 -7.127 0a4.972 4.972 0 0 1 0 -7.071l.524 -.463"></path></svg>
            </a>
        {/if}
    </div>
  
    <div class="text-center pb-4">
        <h3 class="font-bold text-xl">{title}</h3>
        <p class="mx-2.5">{description}</p>
    </div>
  
</div>

<style>
    
</style>