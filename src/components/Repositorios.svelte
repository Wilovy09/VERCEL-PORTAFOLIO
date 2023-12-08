<script>
    import { onMount, onDestroy } from 'svelte';

    let repos = [];
    const url = 'https://api.github.com/users/wilovy09/repos';
    const getRepos = async () => {
        try {
            const response = await fetch(url);
            repos = await response.json();
        } catch (error) {
            console.error('Error fetching repos:', error);
        }
    };
    onMount(() => {
        getRepos();  
    });
</script>

<div class="p-4 min-h-[600px]" id="repositorios">
    <h1 class="text-center text-5xl font-bold pt-4">Repositorios</h1>
    <p class="text-center text-[#c0c0c0] pb-16">Github API</p>
    <section class="snap-x flex gap-4 p-4 overflow-x-auto" id="slider">
        {#each repos as repo}
            <div class="snap-center shrink-0 w-4/5 rounded max-w-[460px] overflow-x-hidden">
                <div class="bg-white rounded-xl text-black">
                    <div class="flex justify-center">
                        <img class="rounded-full w-20 mt-1" src="{repo.owner.avatar_url}" alt="Avatar">
                    </div>
                    <h1 class="text-center font-bold text-2xl">{repo.owner.login}</h1>
                    <br>
                    <h1 class="text-center uppercase font-semibold">{repo.name}</h1>
                    <p class="text-center mx-4">{repo.description}</p>
                    <div class="flex justify-center gap-6 pt-6">
                        <a href="{repo.html_url}" target="_blank">
                            <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-brand-github" width="35" height="35" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M9 19c-4.3 1.4 -4.3 -2.5 -6 -3m12 5v-3.5c0 -1 .1 -1.4 -.5 -2c2.8 -.3 5.5 -1.4 5.5 -6a4.6 4.6 0 0 0 -1.3 -3.2a4.2 4.2 0 0 0 -.1 -3.2s-1.1 -.3 -3.5 1.3a12.3 12.3 0 0 0 -6.2 0c-2.4 -1.6 -3.5 -1.3 -3.5 -1.3a4.2 4.2 0 0 0 -.1 3.2a4.6 4.6 0 0 0 -1.3 3.2c0 4.6 2.7 5.7 5.5 6c-.6 .6 -.6 1.2 -.5 2v3.5" /></svg>
                        </a>
                        {#if repo.homepage}
                            <a href="{repo.homepage}" target="_blank">
                                <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-circle-chevron-right" width="35" height="35" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M11 9l3 3l-3 3" /><path d="M3 12a9 9 0 1 0 18 0a9 9 0 0 0 -18 0z" /></svg>
                            </a>
                        {/if}
                    </div>
                </div>
            </div>
        {/each}
    </section>
</div>

<style>
    #slider {
        scroll-snap-type: x mandatory;
        overflow-x: scroll;
        scrollbar-width: none;
        -ms-overflow-style: none;
    }
    #slider::-webkit-scrollbar {
        display: none;
    }
</style>
