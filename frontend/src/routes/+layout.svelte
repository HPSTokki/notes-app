<script lang="ts">
	import './layout.css';
	import Header from '$lib/components/Header.svelte';
	let { children } = $props();
</script>

<main class="flex min-h-screen flex-col">
	<header class="bg-yellow-300">
		<Header />
	</header>

	<section class="grow">
		{@render children()}
	</section>

	<footer>Footer</footer>
</main>
