<script lang="ts">
	import AddNoteForm from '$lib/components/AddNoteForm.svelte';
	import { onMount } from 'svelte';
	import type { PageData } from './$types';
	import { createNotes, getNotes, deleteNotes } from '$lib/apis/notes';
	import type { ReadNote, CreateNote } from '$lib/apis/notes';

	let isOpen = $state(false);

	let { data } = $props<{ data: PageData }>();

	let notes: ReadNote[] = $derived(data.notes);

	async function loadNotes(search?: string) {
		notes = await getNotes(search);
	}

	async function makeNotes(data: CreateNote) {
		await createNotes(data);
		isOpen = false;
	}

	async function deleteNoteHandle(id: number) {
		await deleteNotes(id);
		await loadNotes();
	}

	onMount(() => {
		loadNotes();
	});

	function closeModal() {
		isOpen = false;
	}
</script>

<div class="flex justify-between p-4">
	<form method="POST" class="filter">
		<input
			class="btn border-green-600 bg-green-600 shadow-sm"
			type="checkbox"
			aria-label="Important"
		/>
		<input
			class="btn border-green-600 bg-green-600 shadow-sm"
			type="checkbox"
			aria-label="Warning"
		/>
		<input
			class="btn border-green-600 bg-green-600 shadow-sm"
			type="checkbox"
			aria-label="Standard"
		/>
		<input class="btn btn-square border-green-600 bg-green-600 shadow-sm" value="x" type="reset" />
	</form>
	<button
		class="btn w-45 border-green-900 bg-green-600 shadow-sm shadow-green-800 btn-primary hover:bg-green-300 hover:text-slate-600"
		onclick={() => (isOpen = true)}
	>
		+ Add Task
	</button>
</div>

{#if isOpen}
	<div class="modal-open modal">
		<div class="modal-box">
			<AddNoteForm onClose={closeModal} onSubmit={makeNotes} />
		</div>
	</div>
{/if}

<div class="flex gap-4 border-t border-t-slate-300 p-4">
	{#each notes as note (note.id)}
		<div class="card h-52 w-62 border border-green-600">
			<div class="card-body">
				<h1>
					{note.title}
				</h1>
				<h2 class="label text-green-300">
					{note.importance}
				</h2>
				<p>
					{note.description}
				</p>
				<button class="btn btn-warning" type="submit" onclick={() => deleteNoteHandle(note.id)}>
					Delete
				</button>
			</div>
		</div>
	{/each}
</div>
