<script lang="ts">
	import AddNoteForm from '$lib/components/AddNoteForm.svelte';

	let isOpen = $state(false);

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
			<AddNoteForm onClose={closeModal} />
		</div>
	</div>
{/if}
